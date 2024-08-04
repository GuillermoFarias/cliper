"""Container module."""
import inspect
from core.contracts.container import Container as ContainerContract


class Container(ContainerContract):
    """App container."""
    __instance = None
    __bindings = {}
    __resolving = set()  # Set to keep track of currently resolving classes

    @staticmethod
    def get_instance():
        """Gets the instance of the container."""
        if Container.__instance is None:
            Container.__instance = Container()
        return Container.__instance

    def has(self, key):
        """Check if the container has a binding."""
        return key in self.__bindings

    def bind(self, key, cls):
        """Link a class to the container."""
        _key = f"{key.__module__}.{key.__qualname__}"
        if not self.has(_key):
            self.__bindings[_key] = cls

    def singleton(self, cls, instance):
        """Register a singleton object."""
        key = f"{cls.__module__}.{cls.__qualname__}"
        if not self.has(key):
            self.__bindings[key] = instance

    def make(self, cls):
        """Obtains an instance from the container."""
        if isinstance(cls, type):  # cls es una clase
            key = f"{cls.__module__}.{cls.__qualname__}"
            if key in self.__bindings:
                binding = self.__bindings[key]
                if isinstance(binding, type):
                    return self.__resolve(binding)
                else:
                    return binding
            else:
                return self.__resolve(cls)
        else:  # cls es una instancia
            key = f"{cls.__class__.__module__}.{cls.__class__.__qualname__}"
            if key in self.__bindings:
                return self.__bindings[key]
            raise ValueError(f"Instance of '{key}' is not registered in the container.")

    def __resolve(self, cls):
        """Resolve class dependencies and create an instance."""
        # Verificar si `cls` es una instancia en lugar de una clase
        if not isinstance(cls, type):
            return cls

        key = f"{cls.__module__}.{cls.__qualname__}"

        if key in self.__resolving:
            raise ValueError(f"Circular dependency detected for class '{key}'")

        if key == 'inspect._empty':
            return cls

        self.__resolving.add(key)
        try:
            # Obtener parámetros del constructor
            try:
                sig = inspect.signature(cls.__init__)
            except ValueError:
                # Clase no tiene constructor explícito
                return cls()

            params = sig.parameters

            # Preparar argumentos para el constructor de la clase
            args = []
            kwargs = {}
            for param_name, param in params.items():
                if param_name == 'self':
                    continue
                # Verificar si el parámetro tiene un valor por defecto
                if param.default is param.empty:
                    # Resolver la dependencia
                    dependency_key = f"{param.annotation.__module__}.{param.annotation.__qualname__}"
                    resolved_dependency = self.__resolve(
                        self.__bindings.get(dependency_key, param.annotation)
                    )
                    # Verificar el tipo de parámetro
                    if param.kind in (param.POSITIONAL_ONLY, param.POSITIONAL_OR_KEYWORD):
                        args.append(resolved_dependency)
                    elif param.kind == param.KEYWORD_ONLY or param.kind == param.POSITIONAL_OR_KEYWORD:
                        kwargs[param_name] = resolved_dependency
                else:
                    kwargs[param_name] = param.default

            # Crear una instancia de la clase
            return cls(*args, **kwargs)
        finally:
            self.__resolving.remove(key)
