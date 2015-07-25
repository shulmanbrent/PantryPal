from django.core.mail import send_mail

def send_emails():
    send_mail('I love', 'using sendgrid', 'shulmanbrent@gmail.com', ['shulmanbrent@yahoo.com'], fail_silently=False)
