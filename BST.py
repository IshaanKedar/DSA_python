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
'''As a senior backend engineer at Jovian, you are tasked with
developing a fast in-memory data structure to manage profile information
(username, name and email) for 100 million users. It should allow the following
operations to be performed efficiently:

1. Insert the profile information for a new user.
2. Find the profile information of a user, given their username
3. Update the profile information of a user, given their usrname
4. List all the users of the platform, sorted by username

You can assume that usernames are unique.'''

class User:  #blueprint to create objects
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print('user created')

    def intro_self(self, guest_name):
        print("hi {}, i'm {} contact me at {} for info".format(guest_name, self.name, self.email))

    def __repr__(self):
        return "User(username = {}, name = {}, email = {})".format(self.username,self.name,self.email)
    def __str__(self):
        return self.__repr__()
    
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com' )
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com' )
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left),TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left)+TreeNode.size(self.right)
    
    def traverse_in_order(self):
        if self is None:
            return []
        return (TreeNode.traverse_in_order(self.left)+ [self.key] + TreeNode.traverse_in_order(self.right))
    
    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return   

        # If the node is a leaf 
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        # If the node has children
        TreeNode.display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        TreeNode.display_keys(self.left,space, level+1)   

    def find_node(node, key):
        """Finds a node in the BST with the given key."""
        if node is None:
            return None
        if node.key == key:
            return node
        left_result = TreeNode.find_node(node.left, key)
        return left_result if left_result else TreeNode.find_node(node.right, key)

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)

    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    @staticmethod    
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node


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



tree3 = TreeNode.parse_tuple((('aakash','biraj','hemanth'),'jadesh',('siddhant','sonakshi','vishal')))

print(is_bst(tree3))


#storing key value pairs using BST

class BSTnode():
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


tree = BSTnode(jadhesh.username, jadhesh)
print(tree.key,tree.value)
tree.left = BSTnode(biraj.username, biraj)
tree.left.parent = tree
tree.right = BSTnode(sonaksh.username, sonaksh)
tree.right.parent = tree

tree.left.left = BSTnode(aakash.username, aakash)
tree.left.left.parent = tree.left
tree.left.right = BSTnode(hemanth.username, hemanth)
tree.left.right.parent = tree.right
tree.right.left = BSTnode(siddhant.username, siddhant)
tree.right.left.parent = tree.right
tree.right.right = BSTnode(vishal.username, vishal)
tree.right.right.parent = tree.right
TreeNode.display_keys(tree)

#function to insert new node in bst

def insert(node, key, value):
    if node is None:
        node = BSTnode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node

def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key<node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)
    

node = find(tree, 'hemanth')

print(node.key, node.value)

def update (node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value

def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)
     

'''Balanced Binary Trees
QUESTION 14: Write a function to determine if a binary tree is balanced.

Here's a recursive strategy:

Ensure that the left subtree is balanced.
Ensure that the right subtree is balanced.
Ensure that the difference between heights of left subtree and right subtree is not more than 1.'''

def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1
    height = 1 + max(height_l, height_r)
    return balanced, height

print(is_balanced(tree))
