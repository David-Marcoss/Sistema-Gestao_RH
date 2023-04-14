from celery import shared_task
from apps.core.email import send_mail_template
from .models import Empresa

@shared_task
def envia_email(id,email,template_name):

    empresas = Empresa.objects.get(id=id)
    departamentos= empresas.departamentos.all()
    

    subject = f'Relatorio Departamentos da empresa: {empresas}'

    context = {'empresa':empresas,'departamentos':departamentos}
    
    if email:
        send_mail_template(subject, template_name, context, [email])
    
    return True