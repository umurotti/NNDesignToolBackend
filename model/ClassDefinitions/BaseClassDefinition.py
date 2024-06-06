from builders.ClassDefinitionBuilder import ClassDefinitionBuilder

class BaseClassDefinition(ClassDefinitionBuilder):
    
    def __init__(self, class_name: str = "MyClass", extends: str = "torch.nn.Module") -> None:
        super().__init__()
        self.class_name = class_name
        self.extends = extends
        
    def build_class_definition(self) -> str:
        return  f"class {self.class_name}({self.extends})"
