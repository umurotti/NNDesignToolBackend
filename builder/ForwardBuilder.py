from abc import ABC, abstractmethod

from model_code.CodeBlock import CodeBlock

class ForwardBuilder(ABC):
    
    @abstractmethod
    def build_forward(self) -> str:
        pass
    