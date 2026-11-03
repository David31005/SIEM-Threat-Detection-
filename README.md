SIEM Threat Detection | Security Log Analysis

Cybersecurity SOC Analyst Portfolio Project

Analyst: David Jeffries
Focus: Security Monitoring | Threat Detection | Log Analysis | Incident Investigation
Tools: Python | CSV | GitHub
Project Type: Hands-On Cybersecurity Lab
Environment: Simulated Security Events

⸻

Project Overview

This project demonstrates a Security Information and Event Management (SIEM)-style investigation using simulated authentication logs.

The objective is to identify suspicious login activity, investigate potential brute-force attempts, analyze security events, and document findings using a structured SOC Analyst workflow.

This project provides practical experience with security event analysis, threat detection, and incident documentation relevant to entry-level cybersecurity positions.

Investigation Objectives

* Analyze authentication logs for suspicious activity.
* Identify repeated failed login attempts.
* Investigate potential brute-force behavior.
* Review source IP addresses and login patterns.
* Document security findings and possible risks.
* Recommend appropriate security response actions.

Tools and Technologies

Tool	Purpose
Python	Security log analysis and threat detection
CSV	Storage of simulated authentication events
GitHub	Version control and project documentation
Markdown	Incident reporting and investigation notes

Investigation Methodology

Step 1: Review Security Logs

Examine simulated authentication records to identify successful and unsuccessful login attempts.

Step 2: Identify Suspicious Activity

Look for repeated failed authentication attempts, unusual login patterns, and potentially suspicious source IP addresses.

Step 3: Analyze Security Events

Use Python to review the security logs and identify patterns that may warrant further investigation.

Step 4: Assess Potential Threats

Evaluate whether the observed activity could indicate password guessing, brute-force attempts, or unauthorized access attempts.

Step 5: Document Findings

Record investigation results, potential security risks, and recommended response actions.

Detection Approach

The investigation focuses on identifying indicators such as:

* Multiple failed login attempts.
* Repeated authentication activity from the same source IP.
* Unusual authentication patterns.
* Potential brute-force behavior.

These indicators require investigation and do not automatically confirm a successful attack.

Recommended Incident Response

When suspicious authentication activity is detected, recommended actions include:

1. Validate the security alerts and supporting log evidence.
2. Review the source IP address and affected accounts.
3. Check for successful logins following failed attempts.
4. Escalate potentially compromised accounts for investigation.
5. Recommend account protection measures where appropriate.
6. Document findings and continue monitoring.

Project Files

* detect_threats.py — Python security detection script.
* security_logs.csv — Simulated security event dataset.
* incident_report.md — Security incident investigation report.
* README.md — Project documentation.

Skills Demonstrated

* SOC Alert Investigation
* Security Log Analysis
* SIEM-Style Monitoring
* Threat Detection
* Python Scripting
* Authentication Event Analysis
* Incident Documentation
* Security Risk Assessment
* Incident Response Recommendations

Project Limitations

This is an educational cybersecurity project using simulated security logs.

The investigation demonstrates detection and analysis techniques but does not represent a confirmed real-world security incident or production SIEM deployment.

About the Analyst

David Jeffries

Aspiring Cybersecurity SOC Analyst with a completed Google Cybersecurity Professional Certificate and hands-on experience building security monitoring, threat detection, and incident investigation projects.

GitHub: https://github.com/David31005

Cybersecurity Portfolio: https://github.com/David31005/cybersecurity-portfolio

LinkedIn: https://www.linkedin.com/in/david-jeffries001

⸻

This project is part of my cybersecurity portfolio demonstrating practical skills for entry-level SOC Analyst and Security Analyst positions.

## Future Security Improvements

- Add automated alerts for repeated failed login attempts.
- Expand detection rules to identify suspicious administrator activity.
- Add timestamps and severity levels to security alerts.
- Improve incident response documentation and investigation workflows.
- Test detection accuracy using additional simulated security logs.


## Security Incident Response Checklist

This checklist provides a structured workflow for investigating suspicious authentication activity in the simulated SIEM environment.

