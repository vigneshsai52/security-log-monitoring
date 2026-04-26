# Security Log Aggregation & Anomaly Detection System

Lightweight SIEM-inspired security monitoring project built using Python and AWS security log concepts. Designed to simulate centralized log analysis, anomaly detection, and alerting workflows used in real-world cloud security environments.

## Overview

This project focuses on detecting suspicious login activity and abnormal access behavior by processing log events and generating alerts. It demonstrates practical understanding of security monitoring, log pipelines, IAM event analysis, and incident detection.

## Features

* Centralized log analysis workflow
* Detect repeated failed login attempts
* Identify suspicious IP addresses
* Simulate IAM privilege escalation alerts
* Detect unusual access activity patterns
* Generate security alert reports
* Log parsing and anomaly detection using Python
* Ready for dashboard integration

## Tech Stack

* Python
* Bash
* AWS CloudWatch Logs (concept)
* AWS CloudTrail (concept)
* IAM
* SNS Alerts (concept)
* Log Analysis

## Security Use Cases

* Brute force login detection
* Unauthorized access attempts
* Suspicious IP monitoring
* Privilege escalation detection
* Security event aggregation
* Incident response support

## Project Architecture

CloudTrail / VPC Logs
↓
Central Log Storage
↓
Python Detection Engine
↓
Alert Report / Notifications
↓
Dashboard Monitoring

## Files Included

* log_monitor.py → Main detection script
* sample_logs.txt → Sample security log data
* README.md → Project documentation

## Run Project

python log_monitor.py

## Sample Output

=== Security Alert Report ===
Suspicious IP: 192.168.1.10 | Failed Attempts: 3
Suspicious IP: 10.0.0.5 | Failed Attempts: 3

## Future Improvements

* Real AWS CloudWatch integration
* SNS email alerts
* Grafana dashboard metrics
* Threat scoring engine
* GeoIP suspicious location detection
* Web-based SOC dashboard

## Resume Highlights

* Built lightweight SIEM prototype for centralized security monitoring
* Developed Python scripts for anomaly detection and suspicious IAM activity
* Simulated cloud security workflows using AWS logging concepts
* Generated proactive alerts for suspicious login behavior

## Author

Vignesh Sai
