"""
Class based dict allowing tuple and sparse data
"""

class array:
    
    def __init__(self, M, N, Z):
        #"Create a list long enough to hold M*N elements"
        "Create an M-element list of N-element row lists."
        #self._data = [0] * M * N
        #self._data = sys_array.array("i", [0] * M * N)
        # 
        # putting aside the flattened 3d and attempting
        # the last taught approach
        #
        self._data = {}
        self._rows = M
        self._cols = N
        self._flos = Z
            
    def __getitem__(self, key):
        "Returns the approperate element for a two-element subsscript tubple"
        row, col, flo = self._validate_key(key)
        #return self._data[row*self._cols+col]
        try:
            return self._data[row, col, flo]
        except KeyError:
            return 0
    
    def __setitem__(self, key, value):
        "Sets the appropriate element for a two element subscript tuple"
        row, col, flo = self._validate_key(key)
        #self._data[row*self._cols+col] = value
        self._data[row, col, flo] = value
        
    def _validate_key(self, key):
        """Validates a key against the array's shape, returning good tuples
        Raises KeyError on propblems."""
        row, col, flo = key
        if (0 <= row < self._rows and 0 <= col < self._cols and 0 <= flo < self._flos):
            return key
        raise KeyError("Subscript out of range")