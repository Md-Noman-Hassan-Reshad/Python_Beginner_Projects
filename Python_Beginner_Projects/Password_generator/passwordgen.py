# Password generator using Python
import random

char = """0123456789 !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"""

length = 8

password = ""
for _ in range(length):
    password += password.join(random.choice(char))
print(password.strip())

# This is the short form
password = "".join(random.choice(char) for _ in range(length))
print(password.strip())

# Also can use this
p = "".join(random.sample(char, length))
print(p)

'''
xD2wM49`
)|RV,lDH
8W|)7:Be
'''