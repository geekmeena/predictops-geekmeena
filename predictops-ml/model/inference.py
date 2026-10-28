import numpy as np
from time_rcd import TimeRCDDetector

detector = TimeRCDDetector.from_pretrained(
    variant="multi",
    device="cpu",
)


def calculate_anomaly_score(window):
    scores = detector.predict(window)
    return round(float(np.asarray(scores).reshape(-1)[-1]), 5)
