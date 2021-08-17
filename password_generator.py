import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all = lower + upper + digits + symbols

temp = random.sample(all,10)
password = "".join(temp)
print(password)