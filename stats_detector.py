import numpy as np

def detect_anomalies(data, threshold=3):
    # Simple Z-score anomaly detection
    mean = np.mean(data)
    std = np.std(data)
    z_scores = [(x - mean) / std for x in data]
    return [abs(z) > threshold for z in z_scores]
