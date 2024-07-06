from Facade import JSONFacade

from model.Model import Model
from model.Node.Node import Node
from model.Connection import Connection

from parser.utils import create_node_from_module_with_JSON

import json

class JSONparser:
    def __init__(self, JSON_path: str, use_facade=True):
        self.json_path = JSON_path
        
        if use_facade:
            facade = JSONFacade(JSON_path)
            self.data = facade.simplify_json()
        else:
            self.data = json.load(open(self.json_path))
        
        self.JSON_connections = self.data['connections']
        self.JSON_nodes = self.data['nodes']
        
        self.connections = []
        self.nodes = []

    def parse(self):
        for JSON_node in self.JSON_nodes:
            self.nodes.append(self.__instantiate_node(JSON_node))
            
        for JSON_connection in self.JSON_connections:
           self.connections.append(self.__instantitate_connection(JSON_connection))
        
        return self.connections, self.nodes
    
    def create_model(self) -> Model:
        model = Model(self.nodes, self.connections)
        
        return model
    
    def __instantiate_node(self, node_params: dict) -> Node:
        return create_node_from_module_with_JSON(node_params)

    def __instantitate_connection(self, connection_params: dict) -> Connection:
        return Connection.from_json(connection_params)