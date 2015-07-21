class ctx_mgr:
    def __init__(self, raising=True):
        print("Created new context manger object", id(self))
        self.raising = raising
    def __enter__(self):
        print("__enter__ called")
        cm = object()
        print("__enter return object id:", id(cm))
        return cm
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__called")
        if exc_type:
            print("An exception occurred")
            if self.raising:
                print("Re-raising exception")
            return not self.raising
        
from contextlib import contextmanager
@contextmanager
def ctx_man(raising=False):
    try:
        cm = object()
        print("Context manager returns:", id(cm))
        yield cm
        print("With concluded normally")
    except Exception as e:
        print("Exception", e, "raised")
        if raising:
            print("Re-raising exception")
            raise
