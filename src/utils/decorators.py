def salvar_historico(func):
    """
    Decorator to save the history of function calls.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Logic to save the history of the function call
        # For example, you could log the function name and arguments
        print(f"Function {func.__name__} called with args: {args}, kwargs: {kwargs}")
        return result
    return wrapper
