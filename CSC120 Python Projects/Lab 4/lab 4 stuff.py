username = input('please enter a username: ')
if len(username) < 5 or len(username) > 16:
    print('Invalid username')
else:
    print('Valid username')
