print('Create account with us')
username = input('Enter your username: ')
password = input('Enter your password: ')

print('Your account has been created successfully')
print('Login now! ')

username2 = input('Enter username: ')
password2 = input('Enter password: ')

if username == username2 and password == password2:
    print('Login successfully')
else:
    print('Invalid credentials')