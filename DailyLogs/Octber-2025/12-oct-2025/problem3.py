def require_admin(func):
    def wrapper(*args, **kwargs):
        user = kwargs.get('user')
        if user != 'admin':
            raise PermissionError("Access denied: Admins only")
        return func(*args, **kwargs)
    return wrapper

@require_admin
def delete_server(*args, **kwargs):
    print("Server deleted!")

delete_server(user='admin')      
delete_server(user='guest')      
