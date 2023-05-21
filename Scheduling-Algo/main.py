from class_dependencies_graph import AcyclicTopologicalGraph
import pandas as pd 

finals = []
num_days = 4
num_blocks_per_day = 5

room_df = pd.read_csv('data.csv')

# Assign ids to all graphs in each block per day (1a - 5e)
# Numbers (1 - 5) reprsent Monday to Friday
# Letters (a - e) represent the 5 time blocks per day
for i in range(num_days):
  for j in range(num_blocks_per_day):
    # Create object instance
    graph = AcyclicTopologicalGraph()

    # Increment letter and attach to graph id
    letter = chr(ord('a') + j)
    graph.id = str(i + 1) + letter

    # Append graph to finals list 
    finals.append(graph)
    # finals[counter + i - 1].print_id()  # Check id of graph elements 

# Insert the classes that need to be scheduled in each block
finals[0].insert("A", "Math", "101", 300, "Dr. Smith", None, location="")
finals[0].insert("B", "Physics", "201", 50, "Dr. Johnson", "A", location="")
finals[0].insert("C", "Math", "201", 50, "Dr. Smith", "B", location="")

finals[1].insert(1, "A", "Math", "101", 300, "Dr. Smith", None, location="")
finals[1].insert(2, "B", "Physics", "201", 50, "Dr. Johnson", "A", location="")
finals[1].insert(3, "C", "Math", "201", 50, "Dr. Smith", "B", location="")


# Iterate through the whole finals list (1a - 5e) with each containing an object
for i in range(num_days * num_blocks_per_day):
  # Get the number of classes to schedule 
  num_classes_to_schedule = len(finals[i].graph)

  # If there are no classes to schedule, break
  if (num_classes_to_schedule == 0): break

  for j in range(num_classes_to_schedule):
    # Get max class size 
    max_course_size = finals[i].get_max_course_size()

    # Get max room size
    max_room_size = room_df["Capacity"].max()

    # Assign the room with the higheset class size
    max_room_size_name = room_df.loc[room_df['Capacity'].idxmax(), 'Classroom List']

    # If first column with max capacity can fit class size, the max size class can fit into the max size room
    if (int(max_room_size) > int(max_course_size)):
      # Assign the room with the higheset class size
      location = room_df.loc[room_df['Capacity'].idxmax(), 'Classroom List']

      # Get the node and data of the deleted node 
      # Appends deleted node in graph_loc
      (max_class_size_node, max_class_size_data) = finals[i].remove_node_with_max_class_size()

      # Assign the location to graph storing nodes with locations
      finals[i].set_location(max_class_size_node, location)

      # Re-define data frame with the first row
      room_df = room_df.iloc[1:]
  
  finals[i].print_nodes_loc()



# finals[0].print_nodes()

# Generalized 
# for i in range(num_days * num_blocks_per_day):
#   num_classes_to_schedule = len(finals[i].graph)
#   print(num_classes_to_schedule)
#   if (num_classes_to_schedule == 0): break

#   for j in range(num_classes_to_schedule):
#       # Get the node and data of the deleted node 
#       max_class_size_node, max_class_size_data = remove_node_with_max_class_size(finals[j])
      
#       max_class_size = max_class_size_data['class_size']
#       max_room_size = room_df["Capacity"].max()
#       # print(max_class_size, max_room_size)
#       # max_room_size = room_df.at[0, "Capacity"]

#     # If first column with max capacity can fit class size, can fit class
#       if (max_room_size >= max_class_size):
#         # Assign the room with the higheset class size
#         location = room_df.loc[room_df['Capacity'].idxmax(), 'Classroom List']

#         # Assign the location to the node 
#         finals[j].graph[max_class_size_node]['location'] = location
#         print(finals[j].print_nodes())

#         # Rededine data frame with the first row
#         room_df = room_df.iloc[1:]



