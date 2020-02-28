class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

    #if the value being inserted is less than the root value, we will go to the left
        if value < self.value:            

    #if there is nothing to the left
            if self.left is None:

     # create node with new binary tree
                self.left = BinarySearchTree(value)
                
    #if there is already something to the left, recurse
            else:    
                self.left.insert(value)

    #if the value being inserted is greater than the root value, we will go to the right
        if value >= self.value:

    #if there is nothing to the right
            if self.right is None:

    # create node with new binary tree
                self.right = BinarySearchTree(value)
                
    #if there is already something to the right, recurse
            else:    
                self.right.insert(value)

            
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

    #if the target == value, return true
        if target == self.value:
            return True
        
    #if the target is less than the value, we will go to the left
        elif target < self.value:
            
    #if there is nothing to the left, return false
            if self.left is None:
                return False

     #if there is already something to the left, recurse
            else:
                return self.left.contains(target)

    #if the target is greater than the value, we will go to the right
        elif target > self.value:

    #if there is nothing to the right, return false
            if self.right is None:
                return False
    #if there is already something to the right, recurse
            else:
               return self.right.contains(target)
        else:
            return False
        
        
        

        

    # Return the maximum value found in the tree
    def get_max(self):
    
    #if there is nothing to the right, return the value
        if self.right is None:
            return self.value

    #if there is something to the right, recurse
        else:
            return self.right.get_max()



    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
   
   #if there is something to the left
        if self.left:
            self.left.for_each(cb)

    #if there is something to the right
        if self.right:
            self.right.for_each(cb)
        