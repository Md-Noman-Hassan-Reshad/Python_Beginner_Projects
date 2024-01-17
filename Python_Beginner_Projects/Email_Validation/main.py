# Test if the email address is valid or not in Python using email_validator
from email_validator import validate_email, EmailNotValidError

def check(email):
    try:
        v = validate_email(email)
        print("Valid E-mail")
        
    except EmailNotValidError as e:
        print(e)

check("my.ownsite@our-earth.org")
 
check("ankitrai326.com")