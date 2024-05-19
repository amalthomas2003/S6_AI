*BFS SEARCH*

Use undirected graph if possible,output  BFS implementation on directed graph  will depend only on 
the starting node and direction of nodes and will skip node if no connection exist in foreward direction
N.B this is not coding error, it is how it is


Make a dictionary named graph
key : all nodes
values: neighbours of a particular node

add starting node to the queue
pop the first node in queue and add it to visited.

find all neightbours of the popped node and add it to queue if they are not in visited nor in queue

repet this steps until all nodes are visited