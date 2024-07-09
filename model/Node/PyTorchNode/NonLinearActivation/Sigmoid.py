from model.Node.PyTorchNode.PyTorchNode import PyTorchNode

class Sigmoid(PyTorchNode):
    
    def __init__(self, id: str, node_full_class_name: str, node_type_name: str, custom_name: str) -> None:
        PyTorchNode.__init__(self, id, node_full_class_name, node_type_name, custom_name)
        
    def build_constructor(self) -> str:
        return f"self.{self.custom_name} = torch.nn.Sigmoid()"
    
    def build_forward(self) -> list:
        return super().build_forward()