class Model:
    def __init__(self) -> None:
        self.nodes = []
        self.connections = []
        self.model_code = None
        self.json = None

    def add_node(self, node):
        self.nodes.append(node)

    def add_connection(self, connection):
        self.connections.append(connection)

    def get_nodes(self):
        return self.nodes

    def get_connections(self):
        return self.connections

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_json(self):
        return self.json

    def set_json(self, json):
        self.json = json

    def __str__(self):
        return "Model: " + str(self.model) + " Nodes: " + str(self.nodes) + " Connections: " + str(self.connections)