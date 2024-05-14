from abc import ABC, abstractmethod

from model_code.CodeBlock import CodeBlock

class ImportsBuilder(ABC):
    
    @abstractmethod
    def build_imports(self) -> CodeBlock:
        pass
    