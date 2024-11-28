import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_alert(subject, body, to_email):
    # Gmail SMTP server details
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # TLS port

    # Replace these values with your Gmail account details
    sender_email = "glances.alerts@gmail.com"  # Your dedicated Gmail account for alerts
    sender_password = "ljze wmtq mefx ortu"  # App Password generated for this Gmail account

    # Construct the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS encryption for security
        server.login(sender_email, sender_password)  # Login with your app password
        server.sendmail(sender_email, to_email, msg.as_string())  # Send the email
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")