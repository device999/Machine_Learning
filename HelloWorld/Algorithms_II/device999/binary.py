class TreeNode:

    def __init__(self,x):
        self.value = x
        self.rightNode = None
        self.leftNode = None

def generate_tree(numbers):
    if not numbers:
        return None
    middle = len(numbers)//2
    node = TreeNode(numbers[middle])
    node.leftNode = generate_tree(numbers[:middle])
    node.rightNode = generate_tree(numbers[middle+1:])
    return node

def show_nodes(binary_tree):
    if not binary_tree:
        return
    print("|"+str(binary_tree.value)+"|" )
    print("Left node = "+str( show_nodes(binary_tree.leftNode)), end="")   
    print("Right node = "+str(show_nodes(binary_tree.rightNode)), end="")
    

if __name__=="__main__":
    numbers = [1,2,3,4,5,6,7]
    tree = generate_tree(numbers)
    show_nodes(tree)
    
    
