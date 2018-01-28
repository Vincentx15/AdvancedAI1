#!/bin/bash 

#######  SETUP #######

# Currently in some directory like /Fristname Lastname_ID_assignsubmission_file_/ (named so automatically by Moodle)

# Print to see the name 
#echo $PWD

# Students have *not* renamed the zip file or added a subfolder, so, simply:
#unzip lab3.zip

# Copy back in the original tasks (with changes to the parameters)
#cp ~/tmp/run_task1.py .
#cp ~/tmp/generate_graph.py .
#cp ~/tmp/run_task2.py .

#######  TASK 1 #######

# Generate a new graph
python3 generate_graph.py

# Run the task -- check the result
python3 run_task1.py | grep "Path:"

# Revise the code
vim astar.py

#######  TASK 2 #######

# Run the task -- check the result
python3 run_task2.py | grep "Loss per test instance:"

# Compile the graph and have a look at it
dot probability_tree_exploration.dot -Tpdf -o probability_tree_exploration.pdf
evince probability_tree_exploration.pdf

# Finally, revise the code
vim cc.py
