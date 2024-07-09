from model.Node.PyTorchNode.PyTorchNode import PyTorchNode

class AvgPool2d(PyTorchNode):
    
    def __init__(self, id: str, node_full_class_name: str, node_type_name: str, custom_name: str,
                kernel_size: int, stride: int, padding: int, ceil_mode: bool, count_include_pad: bool, divisor_override: int) -> None:
        PyTorchNode.__init__(self, id, node_full_class_name, node_type_name, custom_name)

        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.ceil_mode = ceil_mode
        self.count_include_pad = count_include_pad
        self.divisor_override = divisor_override
        
    def build_constructor(self) -> str:
        return f"self.{self.custom_name} = torch.nn.AvgPool2d({self.kernel_size}, {self.stride}, {self.padding}, {self.ceil_mode}, {self.count_include_pad})"
    
    def build_forward(self) -> list:
        return super().build_forward()