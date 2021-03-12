# Regan 
# Program 3 - Loops And If Conditions
# February 4th, 2021

# A program written in Python that requests a password from the user and then asks for their name. Dependant
# on what name is input, a different result may show

password = 'Hello'
name = 'Barney'

while True:
    p: str = input('Password? ')
    if p == password:
        break

print('Welcome to the second half of the program!')
n = input('What is your name? ')
if n in ['Madonna', 'Cher']:
    print('May I have your autograph, please?')
elif n == name:
    print('What a great name!')
else:
    print('{0}, that’s a nice name.'.format(n))
