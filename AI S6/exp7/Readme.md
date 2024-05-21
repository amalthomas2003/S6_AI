*A * Algorithm*

graph is taken as dictionary
heruistic value is take as dictionary ( key is node and value is heurestic value)

take initial node (start node) , distance from start node to current node( 0 first time ) and path in priority queue

priority is determined based on new_cost + herurestic value

the neighbours of node with the highest prority is explored next(ie pop(0)):

if the selected node is goal node break and exit code

else traverse through all possible neighbours of the current node

if a neightbour is not in cost dictionary , or if the new distance (or cost) to reach the neighbour is less than previous distance to reach that node the value is updated in cost dictionary

        then the priority queue is appended with new values of the updated node