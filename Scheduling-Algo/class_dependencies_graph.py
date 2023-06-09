class AcyclicTopologicalGraph:
    def __init__(self):
        self.graph = {}
        self.graph_loc = {}
        self.first_node = None

    def set_location(self, node, location):
        # self.graph_loc[0]['location'] = location
        self.graph_loc[node]['location'] = location

    def get_graph(self):
        return self.graph

    def get_graph_loc(self):
        return self.graph_loc

    def get_graph_loc_items(self):
        return self.graph_loc.items()
    
    def get_max_course_size(self):
        max_size = max(data['class_size'] for data in self.graph.values())
        return max_size
    
    def get_relevant_info(self):
        relevant_info = []
        for node, data in self.graph.items():
            info = {
                'course_number': data['course_number'],
                'professor': data['professor'],
                'location': data['location']
            }
            print(node)
            print(info)
            relevant_info.append((node, info))

        return relevant_info

    def insert(self, node, department, course_number, class_size, professor, *dependencies, location):
        if node in self.graph:
            # print(f"Node '{node}' already exists in the graph.")
            return

        if self.first_node is None:
            self.first_node = node

        self.graph[node] = {
            'department': department,
            'course_number': course_number,
            'class_size': class_size,
            'professor': professor,
            'dependencies': list(dependencies),
            'location': location
        }

        # if self.has_cyclic_dependencies(node):
        #     del self.graph[node]
        #     print(f"Inserting node '{node}' creates a cyclic dependency. Node removed.")
        #     return

        print(f"Node '{node}' inserted successfully.")

    # def has_cyclic_dependencies(self, node, visited=None, stack=None):
    #     if visited is None:
    #         visited = set()
    #     if stack is None:
    #         stack = set()

    #     visited.add(node)
    #     stack.add(node)

    #     for dependency in self.graph[node]['dependencies']:
    #         if dependency not in visited:
    #             if self.has_cyclic_dependencies(dependency, visited, stack):
    #                 return True
    #         elif dependency in stack:
    #             return True

    #     stack.remove(node)
    #     return False

    def print_nodes(self):
        print(self.graph.items())

    def print_nodes_loc(self):
        # print(self.loc_list)
        print(self.graph_loc.items())

    def print_nodes_by_criteria(self, criteria, value):
        matching_nodes = [node for node, data in self.graph.items() if data.get(criteria) == value]
        for node in matching_nodes:
            print(f"Node: {node}")
            print(f"Department: {self.graph[node]['department']}")
            print(f"Course Number: {self.graph[node]['course_number']}")
            print(f"Professor: {self.graph[node]['professor']}")
            print(f"Class Size: {self.graph[node]['class_size']}")
            print(f"Location: {self.graph[node]['location']}")
            print()
      
    def print_nodes_without_edges(self):
        nodes_without_edges = [node for node, data in self.graph.items() if not data['dependencies']]
        for node in nodes_without_edges:
            print(f"Node: {node}")
            print(f"Department: {self.graph[node]['department']}")
            print(f"Course Number: {self.graph[node]['course_number']}")
            print(f"Professor: {self.graph[node]['professor']}")
            print(f"Class Size: {self.graph[node]['class_size']}")
            print(f"Location: {self.graph[node]['location']}")
            print()

    def remove_node_with_max_class_size(self):
        # Check if valid graph
        if len(self.graph) == 0:
            print("The graph is empty.")
            exit("Not enough classes to schedule")

        # "Delete" the node with the max class size from the graph
        sorted_nodes = sorted(self.graph.items(), key=lambda x: x[1]['class_size'], reverse=True)
        max_class_size_node, max_class_size_data = sorted_nodes[0]

        # Append the deleted node into graph_loc
        # self.loc_list.append(sorted_nodes[0])

        self.graph_loc.update({max_class_size_node: max_class_size_data})

        # Delete the node from the dependency node 
        del self.graph[max_class_size_node]

        # Remove all dependencies of the "deleted" node
        for node, data in self.graph.items():
            dependencies = data['dependencies']
            if max_class_size_node in dependencies:
                # self.graph[node].dependencies.remove(max_class_size_node)
                self.graph[node]['dependencies'].remove(max_class_size_node)

        print(f"Node '{max_class_size_node}' with the maximum class size {max_class_size_data['class_size']} removed from the graph.")
    
        return sorted_nodes[0]

    # Returns a list containing a node with no outgoing edges and four other nodes that are contained through dependencies
    def search_node_with_dependencies(self):
        node_with_dependencies = []

        for _ in range(len(self.graph)):
            nodes_without_edges = [node for node, data in self.graph.items() if not data['dependencies']]

            if not nodes_without_edges:
                break

            selected_node = nodes_without_edges[0]
            node_with_dependencies.append(selected_node)

            dependencies = self.graph[selected_node]['dependencies']
            node_with_dependencies.extend(dependencies[:4])  # Assuming at most 4 dependencies

            del self.graph[selected_node]

        return node_with_dependencies

    
        
# def remove_node_with_max_class_size(graph):
#     # Check if valid graph
#     if len(graph.graph) == 0:
#         print("The graph is empty.")
#         exit("Not enough classes to schedule")
    
#     # "Delete" the node with the max class size from the graph
#     sorted_nodes = sorted(graph.graph.items(), key=lambda x: x[1]['class_size'], reverse=True)
#     max_class_size_node, max_class_size_data = sorted_nodes[0]
#     # Set the location of deleted node
#     # del graph.graph[max_class_size_node]

#     # Remove all dependencies of the "deleted" node
#     for node, data in graph.graph.items():
#         dependencies = data['dependencies']
#         if max_class_size_node in dependencies:
#           dependencies.remove(max_class_size_node)

#     print(f"Node '{max_class_size_node}' with the maximum class size {max_class_size_data['class_size']} removed from the graph.")
    
#     return sorted_nodes[0]

# # finals = []
# # num_days = 5
# # num_blocks_per_day = 5
# # counter = 0

# # graph = AcyclicTopologicalGraph()

# # for i in range(num_days):
# #   for j in range(num_blocks_per_day):
# #     letter = chr(ord('a') + j)
# #     graph.id = str(i + 1) + letter
# #     finals.append(graph)
# #     finals[counter + i - 1].print_id()  # Check id of graph elements 
    
# # finals[0].insert("A", "Math", "101", 300, "Dr. Smith")
# # finals[0].print_id()

# # graph.insert("A", "Math", "101", 300, "Dr. Smith")
# # graph.insert("B", "Physics", "201", 50, "Dr. Johnson", "A")
# # graph.insert("C", "Math", "201", 50, "Dr. Smith", "A")
# # graph.insert("D", "Chemistry", "201", 200, "Dr. Smith", "A")
# # graph.insert("E", "Biology", "201", 100, "Dr. Adams", "D")

# # graph.print_nodes()
# # graph.print_nodes_without_edges()
# # graph.print_nodes_by_criteria("department", "Math")

# # remove_node_with_max_class_size(graph)

# # graph.print_nodes()