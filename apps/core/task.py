
from celery import shared_task
from apps.core.email import send_mail_template


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def envia_email(request,subject,context,template_name):
    
    if request.user.email:
        send_mail_template(subject, template_name, context, [request.user.email,])
    
    return True
