# E-mail validation using regex
import re

pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

def check(email):
    if re.fullmatch(pattern, email):
        print("Valid E-mail")
    else:
        print("Invalid E-mail")

email = "ankitrai326@gmail.com"
check(email)
 
email = "my.ownsite@our-earth.org"
check(email)
 
email = "ankitrai326.com"
check(email)