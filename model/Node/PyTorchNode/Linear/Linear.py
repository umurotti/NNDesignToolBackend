from model.Node.PyTorchNode.PyTorchNode import PyTorchNode

class Linear(PyTorchNode):
    
    def __init__(self, id: str, node_full_class_name: str, node_type_name: str, custom_name: str,
                in_features: int, out_features: int, bias: bool) -> None:
        PyTorchNode.__init__(self, id, node_full_class_name, node_type_name, custom_name)
        self.in_features = in_features
        self.out_features = out_features
        self.bias = bias
        
    def build_constructor(self) -> str:
        return f"self.{self.custom_name} = torch.nn.Linear({self.in_features}, {self.out_features}, {self.bias})"
    
    def build_forward(self) -> list:
        return super().build_forward()