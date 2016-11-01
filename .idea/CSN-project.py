print("Welcome to our login menu")
loop = 'true'
while(loop == 'true'):
    username = input('Username please: ')
    password = input('Password please: ')
    if(username == 'Rutger' and password == 'Malamuth1'):
        print('Logged in as ' + username)
        loop = 'false'
        loop1 = 'true'
        while(loop1 == 'true'):
            command = input(username + '()  >  > ')
            if(command == 'exit' or command == 'Exit'):
                break
            else:
                print("'" + command + ' is not a valid command!')
    else:
        print('Invalid credentials')
