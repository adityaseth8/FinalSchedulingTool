from class_dependencies_graph import AcyclicTopologicalGraph
import pandas as pd 

finals = []
num_days = 4
num_blocks_per_day = 5
num_classes_per_block = 5
counter = 0
graph_count = 0 


room_df = pd.read_csv('data.csv')
all_course_graph = AcyclicTopologicalGraph()

# Assign ids to all graphs in each block per day (1a - 5e)
# Numbers (1 - 5) reprsent Monday to Friday
# Letters (a - e) represent the 5 time blocks per day
for i in range(num_days):
  for j in range(num_blocks_per_day):
    # Create object instance for each new time block per day 
    graph = AcyclicTopologicalGraph()

    # Increment letter and attach to graph id
    letter = chr(ord('a') + j)
    graph.id = str(i + 1) + letter

    # Append graph to finals list 
    finals.append(graph)
    # finals[counter + i - 1].print_id()  # Check id of graph elements 

ecs_courses_df = pd.read_csv('w23courses_filtered.csv')
ecs_courses_df = ecs_courses_df.reset_index()

# finals[0].insert("A", "Math", "101", 300, "Dr. Smith", None, location="")
# finals[0].insert("B", "Physics", "201", 50, "Dr. Johnson", "A", location="")
# finals[0].insert("C", "Math", "201", 50, "Dr. Smith", "B", location="")

# finals[1].insert(1, "A", "Math", "101", 300, "Dr. Smith", None, location="")
# finals[1].insert(2, "B", "Physics", "201", 50, "Dr. Johnson", "A", location="")
# finals[1].insert(3, "C", "Math", "201", 50, "Dr. Smith", "B", location="")


# Iterate through all rows of the ECS course data frame
for index, row in ecs_courses_df.iterrows():
  course_name = row['Subj'] + " " + row['Crse']
  dept = row['Subj']
  crn = row['CRN']
  course_size = row['Cap_x']
  professor = row['Instructor']
  
  # Assign dependency to the correct courses
  # Will not assign dependency for some courses because we don't have MAT data
  if course_name == "ECS 17":
    # MAT 016A { can be concurrent } or MAT 017A { can be concurrent } or MAT 021A { can be concurrent }
    dependency = None
  elif course_name == "ECS 20":
    # MAT 016A C- or better or MAT 017A C- or better or MAT 021A C- or better
    dependency = None
  elif course_name == "ECS 032A":
    dependency = None
  elif course_name == "ECS 032B":
    dependency = 'ECS 032A'
  elif course_name == "ECS 34":
    # ECS 032C C- or better; or Consent of Instructor.
    dependency = "ECS 032C"
  elif course_name == "ECS 036A":  
    dependency = None
  elif course_name == "ECS 036B":
    dependency = "ECS 036A"
  elif course_name == "ECS 036C":
    dependency = "ECS 036B"
  elif course_name == "ECS 98":
    # dependency = "Consent of instructor"]
    continue
  elif course_name == "ECS 116":
    # dependency = "ECS 032B"]
    continue
  elif course_name == "ECS 120":
    dependency = "ECS 020"
  elif course_name == "ECS 122A":
    #  ECS 020; (ECS 060 or ECS 032B or ECS 036C)
    dependency = "ECS 20", "ECS 036C"
  elif course_name == "ECS 122B":
    # ECS 122A; (ECS 060 or ECS 034 or ECS 036C)
    dependency = "ECS 122A", "ECS 036C"
  elif course_name == "ECS 132": 
    dependency = "ECS 20", "ECS 036B"
  elif course_name == "ECS 140A": 
    dependency = "ECS 50", "ECS 20"
  elif course_name == "ECS 150": 
    #  (ECS 034 or ECS 036C or ECS 060); (ECS 154A or EEC 170)
    dependency = "ECS 036C", "ECS 154A"
  elif course_name == "ECS 152A": 
    dependency = "ECS 036C", "ECS 132"
  elif course_name == "ECS 154B":
    dependency = "ECS 154A"
  else:
    continue

  # Insert the the graph containing all courses
  # all_course_graph.insert(course_name, dept, crn, course_size, professor, dependency, location="")

  # Insert to the finals list courses that are read in from the df
  if len(finals[graph_count].graph) != num_classes_per_block:
    finals[graph_count].insert(course_name, dept, crn, course_size, professor, dependency, location="")
  else:
    graph_count += graph_count

# Insert into a branch of 5 nodes into a block (I.e: Insert classes that have a chain of prereqs)
# all_course_graph.print_nodes()
# while (len(finals[graph_count] != num_classes_per_block)):
#   list_of_dependencies = all_course_graph.search_node_with_dependencies()
#   for item in list_of_dependencies:
    # Insert item into finals[graph_count]

# Iterate through the whole finals list (1a - 5e) with each containing an object
# The block of the final determines that course's final time 
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
