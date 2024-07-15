import numpy as np
import copy

class array:
    def __init__(self, keys_list : list, values : np.ndarray = None):
        self.keys_list = keys_list
        if values is not None:
            assert values.shape == self.shape
        self.values = np.zeros(self.shape) if values is None else copy.deepcopy(values)
    
    def __str__(self): return str(self.values)
    def __repr__(self): return repr(self.values)
    @property
    def shape(self):
        return tuple(len(k) for k in self.keys_list)
    
    def str2index(self, keys):
        indice = tuple(key_list.index(key) for key, key_list in zip(keys, self.keys_list))
        return indice

    def __setitem__(self, keys, v):
        assert len(keys) == len(self.shape)
        indice = self.str2index(keys)
        self.values[indice] = v
    
    def __getitem__(self, keys):
        assert len(keys) == len(self.shape)
        indice = self.str2index(keys)
        return self.values[indice]
    
    def copy(self):
        keys_list = copy.deepcopy(self.keys_list)
        values = copy.deepcopy(self.values)

        return type(self)(keys_list, values)