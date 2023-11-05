from email.message import EmailMessage
import ssl
import smtplib
from .  import account_password

def send_email(reciever, details):
    email_sender='sofis64.developer@gmail.com'
    email_password=account_password.password
    email_reciever=f"{reciever[0]}, {reciever[1]}"
    subject = f"Shuttle Reservation Confirmation"
    body=f"""Dear {details['fname']},

We are thrilled to confirm that your shuttle reservation has been successfully booked. Below are the details of your reservation:

    From: {details['from']}
    To: {details['to']}
    Date: {details['date']}
    Passengers: {details['passengers']}
    Suitcases: {details['suitcases']}
    Pick-up Hour: {details['hour']}
    Pick-up Details: {details['pickup_details']}
    Drop-off Details: {details['dropoff_details']}

Thank you for choosing us as your transportation service. We're committed to providing you with a safe and comfortable journey to your destination. Should you have any questions or need to make any changes to your reservation, please don't hesitate to contact us.

We look forward to serving you and ensuring you have a smooth and enjoyable travel experience.

Safe travels!

Best regards,

Costa Rica Authentic
+506 85714708
www.crauthentic.com
"""
    em=EmailMessage()
    em['From']=email_sender
    em['to']=email_reciever
    em['subject']=subject
    em.set_content(body)

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp: 
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender, email_reciever,em.as_string())
    return "Email Sent!"