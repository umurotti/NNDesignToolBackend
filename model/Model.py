from model.Node.Node import Node
from model_code.ModelCode import ModelCode

class Model:
    def __init__(self) -> None:
        self.nodes = []
        self.connections = []
        self.model_code = None
        self.in_node = None
        self.out_node = None
        self.topological_order = []
        self.node_hash_map = self.__create_hash_map()
        self.critical_path = []

    def generate_model_code(self) -> ModelCode:
        code = ModelCode()
        
        # 1. Add imports
        code.add_imports()
        # 2. Add class definition
        code.add_class_definition()
        # 3. Add constructor
        code.add_constructor(self)
        # 4. Add forward
        code.add_forward(self)
        
        return code
    
    def topological_sort(self, mode='khan') -> list:
        
        def khan(start_node: Node):
            """
            Kahn's algorithm for topological sorting of nodes in a directed acyclic graph (DAG).

            Returns:
            list: A list of nodes in topologically sorted order if the graph is a DAG.
                If the graph contains a cycle, the function will return None.
            """
            # L: List that will contain the sorted elements
            L = []
            # S: List of all nodes with no incoming edge
            S = []

            # Create a copy of in_degree to avoid modifying the original
            in_degree_copy = {node.id: node.in_degree for node in self.nodes}

            # Initialize S with start node
            S.append(start_node)

            # while S is not empty
            while S:
                # remove a node n from S
                n = S.pop()
                # add n to L
                L.append(n)
                
                # for each node m with an edge from n to m
                for m in n.next_nodes:
                    # decrement the in-degree of m in the copy
                    in_degree_copy[m] -= 1
                    # if m has no other incoming edges then
                    if in_degree_copy[m] == 0:
                        # insert m into S
                        S.append(self.node_hash_map[m])

            if len(L) == len(self.nodes):
                return L  # a topologically sorted order
            else:
                return None  # Graph has a cycle
        
        def dfs():
            pass
        
        if mode == 'khan':
            return khan(self.in_node)
        elif mode == 'dfs':
            return dfs(self.in_node)
        else:
            return None
    
    def find_critical_path(self) -> list:
        """
        Find the critical path in a directed acyclic graph (DAG) using the topological order of the nodes.
        
        Parameters:
        None
        
        Returns:
        list: A list of nodes that form the critical path in the graph.
        
        Description:
        The critical path is the longest path in the graph from the input node to the output node.
        This path is used to determine the maximum time it will take to complete the process.
        The critical path is calculated by finding the longest path from the input node to the output node.
        """
        
        # Initialize the critical path
        critical_path = []
        
        # Find the topological order of the nodes
        if self.topological_order == []:
            self.topological_order = self.topological_sort()
        
        # If the topological order is None, the graph contains a cycle
        if self.topological_order is None:
            return None
        
        # Initialize the distance to each node as 0
        distance = {node.id: 0 for node in self.nodes}
        predecessor = {node.id: None for node in self.nodes}
        
        # Iterate over the nodes in topological order
        for node in self.topological_order:
            # Iterate over the next nodes of the current node
            for next_node in node.next_nodes:
                # Update the distance to the next node
                if distance[next_node] < distance[node.id] + 1:
                    distance[next_node] = distance[node.id] + 1
                    predecessor[next_node] = node.id
        
        # Find the node with the maximum distance (end node of the critical path)
        end_node_id = max(distance, key=distance.get)
        
        # Backtrack to find the nodes that form the critical path
        while end_node_id is not None:
            critical_path.insert(0, self.node_hash_map[end_node_id])
            # Mark the node as critical
            critical_path[0].is_critical = True
            end_node_id = predecessor[end_node_id]
        
        return critical_path
    
    def set_model_code(self, model_code):
        self.model_code = model_code
    
    def set_in_node(self, in_node):
        self.in_node = in_node
        
    def set_out_node(self, out_node):
        self.out_node = out_node
        
    def set_nodes(self, nodes):
        self.nodes = nodes
        self.node_hash_map = self.__create_hash_map()
        
    def set_topological_order(self, topological_order):
        self.topological_order = topological_order
        
    def set_critical_path(self, critical_path):
        self.critical_path = critical_path
        
    def set_connections(self, connections):
        self.connections = connections
    
    def set_prev_nodes(self):
        for connection in self.connections:
            self.node_hash_map[connection.to_node].prev_nodes.append(self.node_hash_map[connection.from_node])
    
    def set_next_nodes(self):
        for connection in self.connections:
            self.node_hash_map[connection.from_node].next_nodes.append(self.node_hash_map[connection.to_node])
    
    def fill_prev_next_nodes(self):
        self.set_prev_nodes()
        self.set_next_nodes()
      
    def __create_hash_map(self) -> dict:
        hash_map = {}
        for node_i in self.nodes:
            hash_map[node_i.id] = node_i
        
        return hash_map
    
    def __str__(self) -> str:
        return f"Model with {len(self.nodes)} nodes and {len(self.connections)} connections."