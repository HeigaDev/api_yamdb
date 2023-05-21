from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail


def sending_mail(user):
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        subject="YaMDb registration",
        message=f"Your confirmation code: {confirmation_code}",
        from_email=None,
        recipient_list=[user.email],
    )
