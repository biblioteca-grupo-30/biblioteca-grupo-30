from django.core.mail import send_mail
from django.conf import settings


def send_mail_on_change(instance, book_title, disponibility, **kwargs):
    send_mail(
        subject=f'Oba! O livro {book_title} está {disponibility}',
        message=f'A disponibilidade do livro {book_title} está {disponibility}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['recipient_email@example.com'],
    )
