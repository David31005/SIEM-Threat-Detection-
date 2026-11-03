
import unittest
from datetime import datetime, timedelta

from detect_threats import detect_alerts


class TestSIEMDetection(unittest.TestCase):

    def make_event(self, seconds, status, ip="192.0.2.45", user="admin"):
        return {
            "time": datetime(2026, 10, 30, 9, 15, 0) + timedelta(seconds=seconds),
            "ip": ip,
            "user": user,
            "status": status,
        }

    def test_brute_force_detection(self):
        events = [
            self.make_event(0, "FAILED"),
            self.make_event(5, "FAILED"),
            self.make_event(10, "FAILED"),
            self.make_event(15, "FAILED"),
        ]
        alerts = detect_alerts(events)
        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["severity"], "HIGH")
        self.assertEqual(alerts[0]["risk_score"], 75)
        self.assertEqual(alerts[0]["mitre_attack"], ["T1110"])

    def test_success_after_brute_force(self):
        events = [
            self.make_event(0, "FAILED"),
            self.make_event(5, "FAILED"),
            self.make_event(10, "FAILED"),
            self.make_event(15, "FAILED"),
            self.make_event(20, "SUCCESS"),
        ]
        alerts = detect_alerts(events)
        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["severity"], "CRITICAL")
        self.assertEqual(alerts[0]["risk_score"], 95)
        self.assertEqual(alerts[0]["type"], "BRUTE_FORCE_WITH_SUCCESS")
        self.assertIn("T1078", alerts[0]["mitre_attack"])

    def test_normal_login_activity(self):
        events = [
            self.make_event(0, "SUCCESS"),
            self.make_event(10, "FAILED"),
            self.make_event(20, "SUCCESS"),
        ]
        self.assertEqual(detect_alerts(events), [])

    def test_failures_outside_window(self):
        events = [
            self.make_event(0, "FAILED"),
            self.make_event(30, "FAILED"),
            self.make_event(70, "FAILED"),
            self.make_event(110, "FAILED"),
        ]
        self.assertEqual(detect_alerts(events), [])

    def test_separate_accounts(self):
        events = [
            self.make_event(0, "FAILED", user="admin"),
            self.make_event(5, "FAILED", user="admin"),
            self.make_event(10, "FAILED", user="employee"),
            self.make_event(15, "FAILED", user="employee"),
        ]
        self.assertEqual(detect_alerts(events), [])


if __name__ == "__main__":
    unittest.main()
  
