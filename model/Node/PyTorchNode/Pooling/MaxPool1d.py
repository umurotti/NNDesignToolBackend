from model.Node.PyTorchNode.PyTorchNode import PyTorchNode

class MaxPool1d(PyTorchNode):
    
    def __init__(self, id: str, node_full_class_name: str, node_type_name: str, custom_name: str,
                kernel_size: int, stride: int, padding: int, dilation: int, return_indices: bool, ceil_mode: bool) -> None:
        PyTorchNode.__init__(self, id, node_full_class_name, node_type_name, custom_name)

        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.dilation = dilation
        self.return_indices = return_indices
        self.ceil_mode = ceil_mode
        
    def build_constructor(self) -> str:
        return f"self.{self.custom_name} = torch.nn.MaxPool1d({self.kernel_size}, {self.stride}, {self.padding}, {self.dilation}, {self.return_indices}, {self.ceil_mode})"
    
    def build_forward(self) -> list:
        return super().build_forward()