# import time
# from functools import wraps

# def timer(func):
#     # @wraps(func) to preserve metadata of original function
#     def wrapper(*args, **kwargs):          # accept any args so decorator is generic
#         start = time.time()                # BEFORE calling the function
#         result = func(*args, **kwargs)     # call original function
#         end = time.time()                  # AFTER calling the function
#         print(f"{func.__name__} took {end - start:.4f} seconds")
#         return result
#     return wrapper

# @timer
# def long_running_function():
#     # time.sleep(2)
#     return "Function complete!"

# print(long_running_function())

def decorator(func):
    def wrapper():
        print("WRAPPER CALLED")
        return func()
    # print("DECORATOR CALLED")
    return wrapper

@decorator
def test():
    print("ORIGINAL FUNCTION")

# print(test)
test()
