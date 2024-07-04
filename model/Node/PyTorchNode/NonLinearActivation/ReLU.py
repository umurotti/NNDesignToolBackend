from model.Node.PyTorchNode.PyTorchNode import PyTorchNode

class ReLU(PyTorchNode):
    
    def __init__(self, id: str, node_full_class_name: str, node_type_name: str, custom_name: str,
                inplace: bool) -> None:
        PyTorchNode.__init__(self, id, node_full_class_name, node_type_name, custom_name)
        self.inplace = inplace
        
    def build_constructor(self) -> str:
        return f"self.{self.custom_name} = torch.nn.ReLU({self.inplace})"
    
    def build_forward(self):
        pass