
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path

LOG_FILE = Path(__file__).with_name("security_logs.csv")
THRESHOLD = 4
WINDOW_SECONDS = 60

def analyze_logs():
    events = []

    with LOG_FILE.open(newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            events.append({
                "time": datetime.strptime(
                    row["timestamp"].strip(), "%Y-%m-%d %H:%M:%S"
                ),
                "ip": row["source_ip"].strip(),
                "user": row["username"].strip(),
                "status": row["status"].strip().upper()
            })

    print("=== SECURITY LOG ANALYSIS ===")
    print(f"Total events: {len(events)}")
    print(f"Failed logins: {sum(e['status'] == 'FAILED' for e in events)}")
    print(f"Successful logins: {sum(e['status'] == 'SUCCESS' for e in events)}")

    groups = defaultdict(list)
    for event in events:
        groups[(event["ip"], event["user"])].append(event)

    alerts = 0

    for (ip, user), records in groups.items():
        records.sort(key=lambda e: e["time"])
        failures = [e for e in records if e["status"] == "FAILED"]

        for index in range(len(failures) - THRESHOLD + 1):
            window = failures[index:index + THRESHOLD]
            elapsed = (window[-1]["time"] - window[0]["time"]).total_seconds()

            if elapsed <= WINDOW_SECONDS:
                alerts += 1
                print(f"\n[ALERT] Possible password guessing")
                print(f"Source IP: {ip}")
                print(f"Target account: {user}")
                print(f"{THRESHOLD} failed logins within {elapsed:.0f} seconds")

                later_success = any(
                    e["status"] == "SUCCESS"
                    and window[-1]["time"] < e["time"]
                    <= window[-1]["time"]
                    + __import__("datetime").timedelta(seconds=WINDOW_SECONDS)
                    for e in records
                )
                if later_success:
                    print("WARNING: Successful login followed failed attempts")
                break

    if alerts == 0:
        print("\nNo threshold-based alerts detected.")

if __name__ == "__main__":
    analyze_logs()
