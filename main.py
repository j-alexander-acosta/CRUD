

clients = 'pablo,ricardo,'
clients = clients.capitalize()

def create_client(client_name):
    global clients
    client_name = client_name.capitalize()

    if client_name not in clients:
        clients += client_name
        _add_coma()
    else:
        print('Client already in the client\'s list')


def list_clients():
    global clients
    print(clients)

def update_client(client_name, update_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', update_name + ',')
    else:
        print('Client not in clients list')

def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print('Client not in clients list')

def _add_coma():
    global clients

    clients += ','

def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today? ')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch clients')

def _get_client_name():
    return input('What is the client name? ')

if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command =='D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the new client name? ')
        update_client(client_name, updated_client_name)
        list_clients()
    else:
        print('Invalid command')