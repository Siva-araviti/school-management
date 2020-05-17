from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_email(subject, html_content, to, from_email=settings.EMAIL_HOST_USER):
    msg = EmailMultiAlternatives(subject=subject, from_email=from_email, to=to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()