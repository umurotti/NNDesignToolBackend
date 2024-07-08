from builder.ClassDefinitionBuilder import ClassDefinitionBuilder
from builder.ImportsBuilder import ImportsBuilder
from model.ClassDefinition.BaseClassDefinition import BaseClassDefinition
from model.Import.BaseImports import BaseImports

from model_code.CodeBlock import CodeBlock

class ModelCode:
    def __init__(self) -> None:
        self.imports = None
        self.class_definition = None
        self.constructor = None
        self.forward = None

    def add_imports(self, imp: ImportsBuilder = BaseImports()):
        self.imports = imp.build_imports()
    
    def add_class_definition(self, class_definition: ClassDefinitionBuilder = BaseClassDefinition()):
        self.class_definition = class_definition.build_class_definition()
    
    def add_constructor(self, model):
        constructor_lines = []
        
        # Call parent constructor
        constructor_lines.append("super().__init__()")
        
        # Iterate over the nodes in the topological order
        for node in model.topological_order:
            # Build the constructor for the node
            constructor_lines.append(node.build_constructor())
            
        self.constructor = CodeBlock("def __init__(self)", constructor_lines)
            
    def add_forward(self, model):
        forward_lines = []
        
        # Iterate over the nodes in the topological order
        for node in model.topological_order:
            # Build the forward function for the node
            for line in node.build_forward():
                forward_lines.append(line)
            forward_lines.append("")
            
        self.forward = CodeBlock("def forward(self, x)", forward_lines)
    
    def save_script(self, save_path : str = "./my_model.py"):
        print(self.imports)
        body = CodeBlock(self.class_definition, [self.constructor, "", self.forward])
        print(body)
        
        with open(save_path, 'w') as file:
            file.write(self.imports)
            file.write(str(body))