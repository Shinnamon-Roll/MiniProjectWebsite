def log(msg):
    def decorator(func):
        def wrapper():
            func(msg)

        return wrapper
    return decorator


@log("loading...")
def fetchData(msg):
    print(msg)

fetchData()