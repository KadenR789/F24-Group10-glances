import unittest
from unittest.mock import patch
from email_alert import send_email_alert
from stats import GlancesStats

class TestEmailAlert(unittest.TestCase):

    @patch('email_alert.smtplib.SMTP')
    def test_send_email_alert(self, mock_smtp):
        # Arrange
        subject = "Test Subject"
        body = "Test Body"
        to_email = "test@example.com"

        # Act
        send_email_alert(subject, body, to_email)

        # Assert
        mock_smtp.assert_called_once_with("smtp.gmail.com", 587)
        instance = mock_smtp.return_value
        instance.starttls.assert_called_once()
        instance.login.assert_called_once_with("glances.alerts@gmail.com", "ljze wmtq mefx ortu")
        instance.sendmail.assert_called_once()

    @patch('stats.psutil.cpu_percent', return_value=95)
    @patch('stats.send_email_alert')
    def test_cpu_threshold_alert(self, mock_send_email, mock_cpu_percent):
        # Arrange
        stats = GlancesStats()

        # Act
        stats.check_critical_and_alert()

        # Assert
        mock_send_email.assert_called_once_with(
            subject="Critical Alert: CPU Usage Threshold Exceeded",
            body="The CPU usage has reached a critical level: 95%",
            to_email="YT1953ca@yahoo.com"
        )

    @patch('stats.psutil.virtual_memory')
    @patch('stats.send_email_alert')
    def test_memory_threshold_alert(self, mock_send_email, mock_virtual_memory):
        # Arrange
        mock_virtual_memory.return_value.percent = 95
        stats = GlancesStats()

        # Act
        stats.check_critical_and_alert()

        # Assert
        mock_send_email.assert_called_once_with(
            subject="Critical Alert: Memory Usage Threshold Exceeded",
            body="The memory usage has reached a critical level: 95%",
            to_email="YT1953ca@yahoo.com"
        )

if __name__ == '__main__':
    unittest.main()
