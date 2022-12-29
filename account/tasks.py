from celery import shared_task
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse


# @shared_task
# def send_email_letter(email: str, subject: str, message: str):
#     send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
#
#
# @shared_task
# def send_email(request):
#     subject = request.POST.get('subject', '')
#     message = request.POST.get('message', '')
#     from_email = settings.EMAIL_HOST_USER
#     if subject and message and from_email:
#         try:
#             send_mail(subject, message, from_email, ['admin@example.com'])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
