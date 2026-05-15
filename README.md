# Bug Verification & Data Validation System

## What it does

Parses log files, detects suspicious login patterns, flags anomalies using statistical methods.

## Statistical Anomaly Detection

Uses Z-score method to flag values beyond threshold.

**Code:** See `stats_detector.py`

## Threshold Tuning

**Day 1:** Threshold = 2.0 → Too many false positives (batch jobs)

**Day 2:** Threshold = 4.0 → Missed some real issues

**Day 3:** Threshold = 3.0 + Friday night whitelist → Best balance

**Result:** ~70% reduction in manual review time.

## The Friday False-Positive Fix

**Problem:** Friday night batch jobs triggered alerts every week.

**Fix:** Added time-window whitelist for known batch windows (22:00-23:59 Friday).

## Run

```bash
python log_monitor.py
```

## Output

- Flagged events with rule triggers
- Compliance summary for QA review
