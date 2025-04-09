'''Binary Search Tree (BST)
A binary search tree or BST is a binary tree that satisfies the following conditions:

1. The left subtree of any node only contains nodes with keys less than the node's key
2. The right subtree of any node only contains nodes with keys greater than the node's key

I follows from the above conditions that every subtree of a binary search tree must also be a
binary search tree.

QUESTION 8: Write a function to check if a binary tree is a binary search tree
(BST).

QUESTION 9: Write a function to find the maximum key in a binary tree.

QUESTION 10: Write a function to find the minimum key in a binary tree.'''
class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

# helper function to conver tuple with structure(left_subtree, key, right_subtree)

tree_tuple = ((1,3,None),2,((None, 3,4),5,(6,7,8)))

def parse_tuple(data):
    if isinstance(data,tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

def traverse_in_order(node):
    if node is None:
        return []
    return (traverse_in_order(node.left)+[node.key]+traverse_in_order(node.right))

def tree_height(node):
    if node is None:
        return 0
    return 1+max(tree_height(node.left),tree_height(node.right))

def node_count(node):
    if node is None:
        return 0
    return 1+(node_count(node.left)+node_count(node.right))

tree2 = parse_tuple(tree_tuple)



def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r and 
                   (max_l is None or node.key > max_l)and(min_r is None or node.key < min_r))
    
    min_key = min(remove_none([min_l,node.key,min_r]))
    max_key = max(remove_none([max_l,node.key,max_r]))

    return is_bst_node, min_key, max_key

print(is_bst(tree2))

tree3 = parse_tuple((('aakash','biraj','hemanth'),'jadesh',('siddhant','sonakshi','vishal')))

print(is_bst(tree3))