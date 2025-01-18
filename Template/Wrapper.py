import random

class Wrapper:
    BASE = random.randint(1, 1e9)
    
    def __init__(self, value):
        self.value = value
    
    def __hash__(self):
        return hash(self.value ^ self.BASE)
    
    def __eq__(self, other):
        return isinstance(other, Wrapper) and self.value == other.value