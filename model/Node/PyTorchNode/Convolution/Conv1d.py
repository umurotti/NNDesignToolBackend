from model.Node.PyTorchNode.PyTorchNode import PyTorchNode
from enum import Enum

class PaddingMode(Enum):
    ZEROS = 0
    REFLECT = 1
    REPLICATE = 2
    CIRCULAR = 3
    
    def __str__(self):
        return self.name.lower()
    
class Conv1d(PyTorchNode):
    
    def __init__(self, id: str, node_full_class_name: str, node_type_name: str, custom_name: str,
                 in_channels: int, out_channels: int, kernel_size: int, stride: int, padding: int, dilation: int, groups: int, bias: bool, padding_mode: str) -> None:
        PyTorchNode.__init__(self, id, node_full_class_name, node_type_name, custom_name)
        
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.dilation = dilation
        self.groups = groups
        self.bias = bias
        self.padding_mode = str(PaddingMode(padding_mode))
        
    def build_constructor(self) -> str:
        return f"self.{self.custom_name} = torch.nn.Conv1d({self.in_channels}, {self.out_channels}, {self.kernel_size}, {self.stride}, {self.padding}, {self.dilation}, {self.groups}, {self.bias}, \'{self.padding_mode}\')"
    
    def build_forward(self) -> list:
        return super().build_forward()