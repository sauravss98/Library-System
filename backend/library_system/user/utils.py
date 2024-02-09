import random
from django.core.mail import send_mail

def generate_random_numbers():
    """
    A function to generate random 6 digit number
    """
    # Generate 6 random numbers between 0 and 9
    return random.randint(000000, 999999)

def generate_otp():
    """
    A function to generate random 6 digit number
    """    
    random_numbers = generate_random_numbers()
    return random_numbers

def send_otp_mail(otp,email):
    """
    Function to send the otp mail
    """
    send_mail(
            'Subject here',
            f'Your OTP is: {otp}',
            'sauravsuresh171@gmail.com',
            [email],
            fail_silently=False,  # Set it to True to suppress exceptions
            auth_user=None,
            auth_password=None,
            connection=None,
            html_message=None,
        )