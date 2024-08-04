""" This module contains the inject decorator. """
import inspect
from functools import wraps
from inspect import signature
from core.contracts.container import Container as ContractContainer
from core.container import Container


def inject(func):
    """Injects dependencies to a function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        container: ContractContainer = Container.get_instance()
        param_types = signature(func).parameters

        args_dict = {param_name: arg for param_name, arg in zip(param_types.keys(), args)}

        for param_name, param_type in param_types.items():
            if param_name == 'self':
                continue
            if param_name not in kwargs and param_name not in args_dict:
                if param_type.annotation is not inspect.Parameter.empty:
                    kwargs[param_name] = container.make(param_type.annotation)
                else:
                    raise ValueError(f"No annotation provided for parameter '{param_name}'")

        return func(*args, **kwargs)

    return wrapper
