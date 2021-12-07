def help(arg):
    if (arg == 'list'):
        print('Help list')

    elif (arg == 'login'):
        print('Help login')

    elif (arg == 'lost'):
        print('Help lost')

    elif (arg == 'send'):
        print('Help send')
    else:
        print(f'Invalid argument {arg} for help command ')