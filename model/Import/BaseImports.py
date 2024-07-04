from builder.ImportsBuilder import ImportsBuilder
from model_code.CodeBlock import CodeBlock

class BaseImports(ImportsBuilder):
    
    def __init__(self, imports: list = ["import torch"]) -> None:
        super().__init__()
        self.imports = imports

    def build_imports(self) -> str:
        str = ""
        for imp in self.imports:
            str += imp + "\n"
        return str
        