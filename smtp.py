import smtplib

# Set up the SMTP server and login credentials
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'tonijesse034@gmail.com'
smtp_password = '@Tuwei619'

# Set up the email content
from_address = 'tonijesse034@gmail.com.com'
to_address = 'agerjesse6@gmail.com'
subject = 'Hello from Python!'
message = 'This is a test email.'

# Connect to the SMTP server
smtp_obj = smtplib.SMTP(smtp_server, smtp_port)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login(smtp_username, smtp_password)

# Send the email
email_content = f"Subject: {subject}\n\n{message}"
smtp_obj.sendmail(from_address, to_address, email_content)

# Disconnect from the SMTP server
smtp_obj.quit()
