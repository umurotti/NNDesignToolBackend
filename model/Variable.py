class Variable:
    def __init__(self, in_name, out_name, scheme = None):
        self.scheme = scheme
        self.in_name = in_name
        self.out_name = out_name
        
    def __str__(self) -> str:
        return f"from_{self.in_name}_to_{self.out_name}"