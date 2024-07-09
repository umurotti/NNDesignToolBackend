from model.Node.PyTorchNode.PyTorchNode import PyTorchNode

class ConvTranspose2d(PyTorchNode):
    
    def __init__(self, id: str, node_full_class_name: str, node_type_name: str, custom_name: str,
                 in_channels: int, out_channels: int, kernel_size: int, stride: int, padding: int, output_padding: int, groups: int, bias: bool, dilation: int) -> None:
        PyTorchNode.__init__(self, id, node_full_class_name, node_type_name, custom_name)
        
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.output_padding = output_padding
        self.groups = groups
        self.bias = bias
        self.dilation = dilation
        
    def build_constructor(self) -> str:
        return f"self.{self.custom_name} = torch.nn.ConvTranspose2d({self.in_channels}, {self.out_channels}, {self.kernel_size}, {self.stride}, {self.padding}, {self.output_padding}, {self.groups}, {self.bias}, {self.dilation})"
    
    def build_forward(self) -> list:
        return super().build_forward()