import functools


user = {'name': 'karim',
        'role': 'admin'}
staff = {'name': 'amia',
         'role': 'dev'}

def make_secure(func):
    @functools.wraps(func)
    def get_secure(*args, **kwargs):
        if user['role'] == 'admin':
            return func(*args, **kwargs)
        else:
            return "Not authorized to perform this action"
    return get_secure

@make_secure
def get_password(panel):
    return '1234'

print(get_password)