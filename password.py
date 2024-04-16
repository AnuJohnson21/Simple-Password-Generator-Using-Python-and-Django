print('Password Generator')

import random
import string
l=int(input('enter the length of password:'))

characters=string.ascii_letters
characters+=string.digits
characters+=string.punctuation

password=('')

for i in range(1, l+1):
    next_character=random.choice(characters)
    password+=next_character

print('Your password is:', password)




