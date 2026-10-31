# SIEM-Threat-Detection-
beginner cyber security project investigating suspicious authentication logs and documenting potential brute-force activity
SIEM-Style Threat Detection & Security Log Analysis

Cybersecurity Portfolio Project | SOC Analyst Training

Author: David Jeffries
GitHub: David31005
Project Type: Security Monitoring & Incident Investigation
Experience Level: Entry-Level Cybersecurity


## 1. Project Overview

This project demonstrates fundamental cybersecurity skills by analyzing simulated authentication logs to identify suspicious login activity.

The investigation focuses on a fictional healthcare organization that experienced multiple failed login attempts followed by a successful login to a privileged administrator account.

The objective is to identify potentially malicious behavior, analyze available evidence, assess security risks, and recommend appropriate incident response actions.

Note: This is a simulated, manual security log investigation. No production SIEM platform or real organization was accessed.

## 2. Project Objectives

Analyze authentication logs for suspicious activity.
Identify repeated failed login attempts.
Recognize potential password-guessing and brute-force attack patterns.
Examine successful logins following failed authentication attempts.
Document investigation findings.
Recommend security improvements.

## 3. Tools and Technologies

| Tool / Concept | Purpose |
|---|---|
| GitHub | Project documentation and version control |
| CSV Files | Authentication log data |
| Security Log Analysis | Identify unusual login patterns |
| Incident Response | Document and assess suspicious events |
| Access Control | Evaluate account protection |
| SIEM Concepts | Understand security event monitoring 


## 4. Investigation Scenario

A fictional healthcare organization identified unusual authentication activity involving its administrator account.

Multiple failed login attempts occurred within seconds, followed by a successful authentication from the same source IP address.

This pattern raised concerns about potential unauthorized access.

The investigation was conducted using a simulated authentication dataset.

## 5. Security Log Evidence

The following suspicious authentication events were identified in the simulated dataset:

| Timestamp | Source IP | Account | Status |
|---|---|---|---|
| 09:15:01 | 192.0.2.45 | admin | FAILED |
| 09:15:04 | 192.0.2.45 | admin | FAILED |
| 09:15:08 | 192.0.2.45 | admin | FAILED |
| 09:15:12 | 192.0.2.45 | admin | FAILED |
| 09:15:17 | 192.0.2.45 | admin | SUCCESS |

All IP addresses are fictional documentation examples.



## 6. Investigation Findings

- **Total Authentication Events:** 8
- **Failed Login Attempts:** 5
- **Successful Logins:** 3
- **Suspicious Source IP:** 192.0.2.45
- **Targeted Account:** admin

Suspicious Behavior Identified

Four failed login attempts occurred within approximately 11 seconds.

Five seconds after the fourth failed attempt, the same source IP successfully authenticated to the administrator account.

This pattern is consistent with possible password guessing or brute-force activity.

However, successful authentication alone does not prove that an attacker compromised the account.

Additional investigation would be required.

## 7. Security Risk Assessment

Initial Investigation Priority: High

The activity warrants prompt investigation because it involves a privileged account and repeated authentication failures.

Potential risks include:

Unauthorized administrator access.
Exposure of sensitive organizational information.
Privilege misuse.
Unauthorized configuration changes.
Further compromise of connected systems.
These are potential consequences, not confirmed outcomes of the simulated incident.

## 8. Recommended Security Actions

Immediate Investigation

Verify whether the administrator recognizes the successful login.
Review available multi-factor authentication records.
Examine the source device and authentication context.
Investigate account activity following successful authentication.
Escalate the incident if evidence suggests unauthorized access.
Preventive Security Controls

Implement multi-factor authentication.
Configure appropriate account lockout or rate-limiting controls.
Enable alerts for repeated failed authentication attempts.
Monitor privileged account activity.
Review password policies and account permissions.
Maintain centralized authentication logging.

## 9. Incident Response Workflow

Identification: Detect repeated failed login attempts.

Analysis: Review timestamps, source IP addresses, account names, and authentication outcomes.

Containment: If compromise is suspected, consider revoking sessions, disabling access temporarily, and resetting credentials according to organizational procedures.

Recovery: Restore secure account access after verifying account ownership and reviewing relevant activity.

Documentation: Record evidence, findings, limitations, and recommended actions.

## 10. Skills Demonstrated

This project demonstrates introductory knowledge of:

Security event monitoring
Authentication log analysis
Suspicious activity identification
Incident triage
Brute-force attack indicators
Security risk assessment
Incident response documentation
Technical communication
GitHub project documentation

## 11. Project Files

security_logs.csv — Simulated authentication events used in the investigation.

incident_report.md — Investigation findings, security assessment, and recommendations.

README.md — Project overview, methodology, and technical documentation.

## 12. Investigation Limitations

This project uses a small, fictional authentication dataset.

The investigation does not include actual SIEM ingestion, endpoint telemetry, network packet captures, or verification of user identity.

The evidence supports identifying suspicious activity but does not establish confirmed unauthorized access or data theft.

## 13. Conclusion

This project provided practical experience reviewing security logs, recognizing suspicious authentication patterns, and documenting a potential security incident.

The investigation demonstrates foundational SOC Analyst skills and provides a starting point for more advanced security monitoring projects involving SIEM platforms, automated alerting, and threat detection.


