import time

def logging(func):
    """print spent time and return value"""
    def clocked(*args):
        start_time = time.perf_counter()
        returned = func(*args)
        end_time = time.perf_counter() - start_time
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        # print('[%0.8fs] %s(%s) -> %r' % (end_time, name, arg_str, returned))
        print("===============logging_func===============")
        print(f"[{time.perf_counter() - start_time:0.8f}s] {name}({arg_str}) -> {returned}")
        return returned
    return clocked

def show_details(func):
    """print function information"""
    def clocked(*args):
        start_time = time.perf_counter()
        returned = func(*args)
        end_time = time.perf_counter() - start_time
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print("==================function info.==================")
        print(f"function name         : {name}")
        print(f"function arguments    : {arg_str}")
        print(f"function spending time: {end_time:0.8f}s")
        print(f"function return       : \n{returned}")
        return returned
    return clocked
