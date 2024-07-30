from typing import Collection

class ParameterDescriptor:
    def __init__(self,
                 name: str = None,
                 dtype: str = None,
                 default = None):
        self._data = dict()
        self["name"] = name
        self["type"] = dtype
        self["default"] = default
        return

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getitem__(self, key):
        return self._data[key]

    def __delitem__(self, key):
        del self._data[key]

class NodeDescriptor:
    def __init__(self,
                 name: str,
                 module: str,
                 parameters: Collection[ParameterDescriptor],
                 num_inputs: int = 1,
                 num_outputs: int = 1,
                 important_parameters: Collection[str] = None,
                 required_parameters: Collection[str] = None):
        self._data = dict()
        self["name"] = name
        self["module"] = module
        self["parameters"] = parameters
        self["num_inputs"] = num_inputs
        self["num_outputs"] = num_outputs
        self["important_parameters"] = important_parameters
        self["required_parameters"] = required_parameters

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        if key not in self._data.keys():
            raise KeyError(f"{key} is not a valid key")
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]