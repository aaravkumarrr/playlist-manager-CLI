import datetime

def log_action(func):
    def wrapper(*args, **kwargs):
        print("action occurred at ", datetime.datetime.now())
        return func(*args,**kwargs)
    return wrapper