class CodeBlock():
    def __init__(self, head, block) -> None:
        self.head = head
        self.block = block
        
    def __str__(self, indent=""):
        result = indent + str(self.head) + ":\n"
        indent += "    "
        for block in self.block:
            if isinstance(block, CodeBlock):
                result += block.__str__(indent)
            else:
                result += indent + block + "\n"
        return result