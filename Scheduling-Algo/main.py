from class_dependencies_graph import AcyclicTopologicalGraph
from room_capacity_data_scrape import RoomCapacity

finals = []
num_days = 5
num_blocks_per_day = 5
counter = 0

graph = AcyclicTopologicalGraph()
room_data = RoomCapacity()

for i in range(num_days):
  for j in range(num_blocks_per_day):
    letter = chr(ord('a') + j)
    graph.id = str(i + 1) + letter
    finals.append(graph)
    # finals[counter + i - 1].print_id()  # Check id of graph elements 

finals[0].insert("A", "Math", "101", 300, "Dr. Smith")
finals[0].insert("B", "Physics", "201", 50, "Dr. Johnson", "A")
finals[0].insert("C", "Math", "201", 50, "Dr. Smith", "B")


