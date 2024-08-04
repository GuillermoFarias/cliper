""" Config reader class. """
import os
import importlib.util
from typing import Any, Union, List


class Config:
    """Config reader class."""

    def __init__(self, config_dir: str):
        """Constructor."""
        self.config_dir = config_dir

    def _load_module(self, module_name: str) -> Any:
        """Load a Python module."""
        module_path = os.path.join(self.config_dir, f"{module_name}.py")
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def _get_value(self, obj: Any, keys: List[str]) -> Any:
        """Get the value of the concatenated key."""
        for key in keys:
            if isinstance(obj, dict):
                obj = obj.get(key, None)
            elif isinstance(obj, list):
                try:
                    index = int(key)
                    obj = obj[index]
                except (IndexError, ValueError):
                    obj = None
            elif hasattr(obj, key):
                obj = getattr(obj, key)
            else:
                obj = None
            if obj is None:
                break
        return obj

    def get(self, module_name: str, key: str = None) -> Union[str, dict, list, None]:
        """Get the value of the concatenated key."""
        module = self._load_module(module_name)
        if key is None:
            value = module.__dict__
        else:
            keys = key.split('.')
            value = self._get_value(module, keys)

        return value
