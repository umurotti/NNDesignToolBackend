from model.Node import Node
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

            Parameters:
            start_node (Node): The starting node for the algorithm. This should be a node with no incoming edges
                            or the initial node from where the sorting begins.

            Returns:
            list: A list of nodes in topologically sorted order if the graph is a DAG.
                If the graph contains a cycle, the function will return None.

            Description:
            Kahn's algorithm works by repeatedly removing nodes with no incoming edges (in-degree of 0)
            and appending them to the sorted list. For each removed node, the in-degree of its neighbors
            is decreased. If a neighbor's in-degree becomes 0, it is added to the list of nodes to process.
            This continues until all nodes are processed or a cycle is detected.

            Example:
            Suppose we have a graph with the following edges:
            A -> C, B -> C, C -> E, B -> D, D -> F, E -> F, E -> H, F -> G
            
            The topological sort would be something like:
            B -> A -> D -> C -> E -> H -> F -> G
            
            Internal Working:
            - Initialize an empty list `L` to store the topologically sorted nodes.
            - Initialize a stack `S` and append the start node.
            - While the stack is not empty, pop a node from the stack, add it to `L`.
            - For each neighbor of the current node, remove the edge from the current node to the neighbor.
            If the neighbor has no other incoming edges, append it to the stack.
            - After processing all nodes, if the length of `L` equals the total number of nodes, return `L`.
            Otherwise, return None indicating a cycle in the graph.
            """
            
            # L: Empty list that will contain the sorted elements
            L = []
            # S: Set of all nodes with no incoming edge
            S = []
            # Add the starting node to the stack
            S.append(start_node)
            
            # while S is not empty do
            while len(S) > 0:
                # remove a node n from S
                n = S.pop()
                # add n to L
                L.append(n)
                
                # for each node m with an edge e from n to m do
                for m in n.next_nodes:
                    # remove edge e from the graph
                    n.next_nodes.remove(m)
                    self.node_hash_map[m].prev_nodes.remove(n.id)
                    # if m has no other incoming edges then
                    if len(self.node_hash_map[m].prev_nodes) == 0:
                        # insert m into S
                        S.append(self.node_hash_map[m])

            if len(L) == len(self.nodes):
                return L # a topologically sorted order
            else:
                return None # Graph has a cycle
        
        def dfs():
            pass
        
        if mode == 'khan':
            return khan(self.in_node)
        elif mode == 'dfs':
            return dfs(self.in_node)
        else:
            return None
        
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
        
    def set_connections(self, connections):
        self.connections = connections
        
    def __create_hash_map(self) -> dict:
        hash_map = {}
        for node_i in self.nodes:
            hash_map[node_i.id] = node_i
        
        return hash_map
    
    def __str__(self) -> str:
        return f"Model with {len(self.nodes)} nodes and {len(self.connections)} connections."