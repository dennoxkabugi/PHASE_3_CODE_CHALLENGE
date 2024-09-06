class ApplyDecorator:
    def __call__(self, func):
        def decorator_func(*args, **kwargs):
            print("Decorator Applied")
            return func(*args, **kwargs)
        return decorator_func

apply_decorator = ApplyDecorator()

def sample_function():
    print("Function is executed")

decorated_function = apply_decorator(sample_function)

decorated_function()