import time
import atexit
import colorama
from functools import wraps

def time_function(func):
    total_time = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal total_time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        total_time += elapsed
        return result

    def print_time_local():
        print_time(func.__name__, total_time)

    atexit.register(print_time_local)
    return wrapper

def average_time_function(func):
    total_time = 0
    calls = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal total_time, calls
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        total_time += end_time - start_time
        calls += 1
        return result

    def print_avg():
        if calls > 0:
            avg_time = total_time / calls
            print_average_time(func.__name__, avg_time, calls, round(total_time, 5))

    atexit.register(print_avg)
    return wrapper

def get_nice_time(func_name, time):
    if time < 1:  # Less than 1 second
        time_str = f"{time * 1000:.2f} ms"
    elif time < 60:  # Less than 1 minute
        time_str = f"{time:.2f} s"
    elif time < 3600:  # Less than 1 hour
        minutes = int(time // 60)
        seconds = int(time % 60)
        time_str = f"{minutes} min {seconds} s"
    else:  # 1 hour or more
        hours = int(time // 3600)
        minutes = int((time % 3600) // 60)
        seconds = int(time % 60)
        time_str = f"{hours} h {minutes} min {seconds} s"

    return time_str

def print_time(func_name, time):
    time_str = get_nice_time(func_name, time)
    print(f"{colorama.Fore.YELLOW}Execution time of '{func_name}': {time_str}{colorama.Style.RESET_ALL}")

def print_average_time(func_name, avg_time, calls, total_time):
    time_str = get_nice_time(func_name, avg_time)
    print(f"{colorama.Fore.YELLOW}Average execution time of '{func_name}': {total_time} s ({calls} calls {time_str} each){colorama.Style.RESET_ALL}")
