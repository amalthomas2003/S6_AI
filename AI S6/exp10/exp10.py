class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children or []

def minimax(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or not node.children:
        return node.value
    
    if maximizingPlayer:
        maxEval = float('-inf')
        for child in node.children:
            eval = minimax(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  
        return maxEval
    else:
        minEval = float('inf')
        for child in node.children:
            eval = minimax(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  
        return minEval

def create_tree(depth, leaf_values):
    def create_node(current_depth, index):
        if current_depth == depth:
            return Node(value=leaf_values[index])
        left_child = create_node(current_depth + 1, 2 * index)
        right_child = create_node(current_depth + 1, 2 * index + 1)
        return Node(children=[left_child, right_child])
    
    return create_node(0, 0)
depth = int(input("Enter the depth of the tree: "))
num_leaf_nodes = 2 ** depth
leaf_values = []
for i in range(num_leaf_nodes):
    value = int(input(f"Enter value for leaf node {i+1}: "))
    leaf_values.append(value)
root = create_tree(depth, leaf_values)
optimal_value = minimax(root, depth, alpha=float('-inf'), beta=float('inf'), maximizingPlayer=True)
print(f"The optimal value is: {optimal_value}")
