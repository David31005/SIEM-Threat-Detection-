# Advanced SIEM Threat Detection 2.0

![SIEM Security Tests](https://github.com/David31005/SIEM-Threat-Detection-/actions/workflows/siem-tests.yml/badge.svg)

**Python | Security Monitoring | Threat Detection | MITRE ATT&CK | GitHub Actions | CI/CD**

## Project Overview

Advanced SIEM Threat Detection 2.0 is a Python-based cybersecurity portfolio project that analyzes simulated authentication logs to identify suspicious login activity.

The project demonstrates detection engineering, security event analysis, risk classification, automated testing, and structured security reporting.

**Environment:** Simulated security events  
**Language:** Python 3.11  
**Automation:** GitHub Actions  
**Testing:** Python unittest

This is a SIEM-style detection simulation, not a production SIEM deployment.

## Key Features

- Automated CSV security log analysis
- Brute-force detection using configurable thresholds
- Detection of successful logins following repeated failures
- High and Critical severity classification
- Demonstration risk scores of 75 and 95
- MITRE ATT&CK technique references
- Structured JSON alert reporting
- Automated Python unit tests
- GitHub Actions CI/CD testing
- Basic validation and skipping of malformed log records

## Project Architecture

```text
security_logs.csv
       |
       v
detect_threats.py
       |
       v
Authentication Event Analysis
       |
       v
Brute-Force Detection
       |
       v
Severity and Risk Classification
       |
       v
security_alerts.json
       |
       v
Security Investigation
```

GitHub Actions separately runs the unit tests, executes the detection engine, and uploads the JSON report as an artifact.

## Repository Files

| File | Description |
|------|-------------|
| detect_threats.py | Python detection engine |
| security_logs.csv | Simulated authentication events |
| test_detect_threats.py | Automated unit tests |
| incident_report.md | Security investigation documentation |
| README.md | Project documentation |
| .github/workflows/siem-tests.yml | CI/CD testing workflow |

The detection script generates security_alerts.json when executed.

## Detection Rules

### Rule 1: Brute-Force Authentication Attempt

**Condition:** Four failed logins from the same source IP against the same account within 60 seconds.

**Severity:** HIGH  
**Risk score:** 75  
**MITRE ATT&CK:** T1110 — Brute Force

### Rule 2: Successful Login Following Brute Force

**Condition:** A successful login occurs within 60 seconds after the qualifying failed-login sequence.

**Severity:** CRITICAL  
**Risk score:** 95  
**MITRE ATT&CK references:**
- T1110 — Brute Force
- T1078 — Valid Accounts

The T1078 reference is an investigation hypothesis; a successful login alone does not confirm account compromise.

Risk scores are demonstration values, not calibrated probabilities.

## Sample Detection Results

For the eight-event simulated dataset, the expected output is:

```text
=== ADVANCED SIEM THREAT DETECTION 2.0 ===
Total events: 8
Failed logins: 5
Successful logins: 3
Alerts generated: 1

[ CRITICAL ] BRUTE_FORCE_WITH_SUCCESS | 192.0.2.45 | admin | score=95

JSON report: security_alerts.json
```

### Investigation Summary

**Source IP:** 192.0.2.45  
**Target account:** admin  
**Failed attempts:** 4  
**Successful login:** 2026-10-30 09:15:17  
**Classification:** Critical simulated authentication alert

The IP address belongs to a documentation-only address range and is used here as test data.

**Recommended investigation:** Review related authentication events, verify whether the login was authorized, examine account activity, and follow the organization's incident response procedures.

## Automated Security Testing

The project includes five Python unit tests:

1. Brute-force detection
2. Successful login after repeated failures
3. Normal login activity without alerts
4. Failed logins outside the detection window
5. Separation of authentication events by account

Run the tests locally:

```bash
python -m unittest discover -v
```

Run the detection engine:

```bash
python detect_threats.py
```

The script uses Python standard-library modules and requires no external Python packages.

## GitHub Actions CI/CD

The GitHub Actions workflow automatically:

1. Checks out the repository.
2. Sets up Python 3.11.
3. Runs the automated unit tests.
4. Executes the SIEM detection script.
5. Uploads the generated JSON security alerts as an artifact.

**Workflow:** .github/workflows/siem-tests.yml

The workflow runs on pushes, pull requests, and manual dispatch.

## Limitations and Future Improvements

This project is a controlled security simulation.

Current limitations:
- Processes CSV files rather than live SIEM event streams
- Uses fixed thresholds and demonstration risk scores
- Detects one qualifying sequence per IP/account group
- Does not confirm that a successful login represents compromise

Planned improvements:
- Additional detection rules and test coverage
- Configurable thresholds and severity scoring
- Expanded MITRE ATT&CK mappings
- Detection performance evaluation
- Security dashboards and alert visualization

## Skills Demonstrated

**SOC Analysis:** Authentication log review, suspicious activity detection, and incident investigation.

**Detection Engineering:** Python detection logic, threshold-based rules, risk classification, and structured alert generation.

**Security Automation:** Automated unit testing, GitHub Actions, and CI/CD workflow development.

**Security Frameworks:** MITRE ATT&CK technique mapping and incident response documentation.

## Author

**David Jeffries**  
Aspiring SOC Analyst | Cybersecurity Portfolio

[GitHub Profile](https://github.com/David31005)  
[LinkedIn](https://www.linkedin.com/in/david-jeffries001)

---


