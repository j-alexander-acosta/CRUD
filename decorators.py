PASSWORD = '12345'

def password_required(func):
    def wrapper():
        password = input('Cual es tu contrasena: ')

        if password == PASSWORD:
            return func()
        else:
            print('La contrasena es incorrecta')

    return wrapper

@password_required
def needs_password():
    print('La contrasena es correcta')


def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper

@upper
def say_my_name(name):
    return ('Hola, {}'.format(name))


if __name__ == '__main__':
    print(say_my_name('Alex'))