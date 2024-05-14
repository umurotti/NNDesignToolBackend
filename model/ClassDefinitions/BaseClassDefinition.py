from builders.ClassDefinitionBuilder import ClassDefinitionBuilder
from model_code.CodeBlock import CodeBlock

class BaseClassDefinition(ClassDefinitionBuilder):
    
    def __init__(self, class_name: str, extends: str) -> None:
        super().__init__()
        self.class_name = class_name
        self.extends = extends
        
    def build_class_definition(self):
        return CodeBlock().add_line(f"class {self.class_name}({self.extends}):")
