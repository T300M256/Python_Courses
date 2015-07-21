"""
Class based dict allowing tuple and sparse data
"""

"""
def array(M,N):
    "Create an M-element list of N-element row lists."
    rows = []
    for _ in range(M):
        rows.append([0] * N)
    return rows
"""

class array:
    
    def __init__(self, M, N):
        #"Create a list long enough to hold M*N elements"
        "Create an M-element list of N-element row lists."
        #self._data = [0] * M * N
        #self._data = sys_array.array("i", [0] * M * N)
        self._data = {}
        self._rows = M
        self._cols = N
            
    def __getitem__(self, key):
        "Returns the approperate element for a two-element subsscript tubple"
        row, col = self._validate_key(key)
        #return self._data[row*self._cols+col]
        try:
            return self._data[row, col]
        except KeyError:
            return 0
    
    def __setitem__(self, key, value):
        "Sets the appropriate element for a two element subscript tuple"
        row, col = self._validate_key(key)
        #self._data[row*self._cols+col] = value
        self._data[row, col] = value
        
    def _validate_key(self, key):
        """Validates a key against the array's shape, returning good tuples
        Raises KeyError on propblems."""
        row, col = key
        if (0 <= row < self._rows and 0 <= col < self._cols):
            return key
        raise KeyError("Subscript out of range")