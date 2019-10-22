command = ''
started = False

while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('car already started')
        else:
            started = True
            print('car started')
    elif command == 'stop':
        if not started:
            print('car already stopped')
        else:
            started = False
            print('car stopped')
    elif command == 'help':
        print('start - start the car')
        print('stop - stop the car')
        print('help')
        print('quit')
    elif command == 'quit':
        break
    else:
        print('wrong command')
