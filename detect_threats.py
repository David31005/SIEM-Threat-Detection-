
import csv
import json
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

LOG_FILE = Path(__file__).with_name("security_logs.csv")
ALERT_FILE = Path(__file__).with_name("security_alerts.json")
THRESHOLD = 4
WINDOW_SECONDS = 60


def load_events(path=LOG_FILE):
    events = []
    with Path(path).open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        required = {"timestamp", "source_ip", "username", "status"}
        if not required.issubset(set(reader.fieldnames or [])):
            raise ValueError("CSV must contain timestamp, source_ip, username, status")
        for line_number, row in enumerate(reader, start=2):
            try:
                timestamp = datetime.strptime(row["timestamp"].strip(), "%Y-%m-%d %H:%M:%S")
                ip = row["source_ip"].strip()
                user = row["username"].strip()
                status = row["status"].strip().upper()
                if not ip or not user or status not in {"FAILED", "SUCCESS"}:
                    raise ValueError("Invalid IP, username, or status")
                events.append({"time": timestamp, "ip": ip, "user": user, "status": status})
            except (ValueError, AttributeError, TypeError) as error:
                print(f"[SKIPPED] CSV line {line_number}: {error}")
    return events


def detect_alerts(events):
    groups = defaultdict(list)
    for event in events:
        groups[(event["ip"], event["user"])].append(event)

    alerts = []
    for (ip, user), records in groups.items():
        records.sort(key=lambda item: item["time"])
        failures = [event for event in records if event["status"] == "FAILED"]
        if len(failures) < THRESHOLD:
            continue

        for index in range(len(failures) - THRESHOLD + 1):
            window = failures[index:index + THRESHOLD]
            elapsed = (window[-1]["time"] - window[0]["time"]).total_seconds()
            if elapsed > WINDOW_SECONDS:
                continue

            last_failure = window[-1]["time"]
            success = next((event for event in records
                            if event["status"] == "SUCCESS"
                            and last_failure < event["time"] <= last_failure + timedelta(seconds=WINDOW_SECONDS)), None)
            severity = "CRITICAL" if success else "HIGH"
            score = 95 if success else 75
            alerts.append({
                "type": "BRUTE_FORCE_WITH_SUCCESS" if success else "BRUTE_FORCE_ATTEMPT",
                "severity": severity,
                "risk_score": score,
                "source_ip": ip,
                "username": user,
                "failed_attempts": THRESHOLD,
                "window_seconds": WINDOW_SECONDS,
                "first_failure": window[0]["time"].isoformat(sep=" "),
                "last_failure": last_failure.isoformat(sep=" "),
                "successful_login": success["time"].isoformat(sep=" ") if success else None,
                "mitre_attack": ["T1110", "T1078"] if success else ["T1110"],
                "note": "Simulated detection; investigate before treating as confirmed compromise."
            })
            break
    return alerts


def main():
    events = load_events()
    alerts = detect_alerts(events)
    print("=== ADVANCED SIEM THREAT DETECTION 2.0 ===")
    print(f"Total events: {len(events)}")
    print(f"Failed logins: {sum(e['status'] == 'FAILED' for e in events)}")
    print(f"Successful logins: {sum(e['status'] == 'SUCCESS' for e in events)}")
    print(f"Alerts generated: {len(alerts)}")
    for alert in alerts:
        print(f"[ {alert['severity']} ] {alert['type']} | {alert['source_ip']} | {alert['username']} | score={alert['risk_score']}")
    ALERT_FILE.write_text(json.dumps(alerts, indent=2) + "\n", encoding="utf-8")
    print(f"JSON report: {ALERT_FILE.name}")


if __name__ == "__main__":
    main()
  
