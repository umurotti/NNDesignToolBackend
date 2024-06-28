from model.Model import Model
from model.Node import Node
from model.Connection import Connection

from parser.utils import create_node_from_module_with_JSON, graphify

import json

class JSONparser:
    def __init__(self, JSON_path: str):
        self.json_path = JSON_path
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
        
        graphify(self.nodes, self.connections)
        
        return self.connections, self.nodes
    
    def create_model(self) -> Model:
        model = Model()
        
        model.set_nodes(self.nodes)
        model.set_connections(self.connections)
        model.set_in_node(self.get_in_node())
        model.set_out_node(self.get_out_node())
        
        #model.fill_prev_next_nodes()
        
        return model
    
    def __instantiate_node(self, node_params: dict) -> Node:
        return create_node_from_module_with_JSON(node_params)

    def __instantitate_connection(self, connection_params: dict) -> Connection:
        return Connection.from_json(connection_params)
    
    def get_in_node(self):
        for node in self.nodes:
            if node.node_type_name == 'In':
                return node
            
    def get_out_node(self):
        for node in self.nodes:
            if node.node_type_name == 'Out':
                return node
    
    