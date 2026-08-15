class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class TreeMap:

    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        # if self.root is None:
        #     self.root = new_node
        #     return

        def insert_helper(current, k, v) -> Node:
            if current is None: 
                return TreeNode(k, v)

            if k < current.key:
                current.left = insert_helper(current.left, k, v)
            elif k > current.key: 
                current.right = insert_helper(current.right, k, v)
            else:
                # same key, override the value 
                current.value = v
            
            return current

        self.root = insert_helper(self.root, key, val)

    def get(self, key: int) -> int:
        
        def get_helper(current, key) -> int:
            if current is None:
                return -1
            if current.key == key:
                return current.value
            elif current.key < key:
                return get_helper(current.right, key)
            else:
                return get_helper(current.left, key)

        return get_helper(self.root, key)


    def getMin(self) -> int:
        if self.root is None:
            return -1
        current = self.root
        while current.left != None:
            current = current.left
        
        return current.value


    def getMax(self) -> int:
        if self.root is None:
            return -1
        current = self.root
        while current.right != None:
            current = current.right

        return current.value


    def remove(self, key: int) -> None:
        def get_min(current):
            while current.left != None:
                current = current.left
            return current

        def remove_helper(current, key) -> TreeNode:
            if current is None:
                return None
            if key < current.key:
                # remove from left
                current.left = remove_helper(current.left, key)
            elif key > current.key:
                # remove from right
                current.right = remove_helper(current.right, key)
            else: # if current.key == key:
                if current.left is None:
                    return current.right
                if current.right is None:
                    return current.left
 
                # both alive 
                next_node = get_min(current.right)

                current.key = next_node.key
                current.value = next_node.value
                current.right = remove_helper(current.right, current.key)
            
            return current

        self.root = remove_helper(self.root, key)

    def getInorderKeys(self) -> List[int]:
        result = []
        
        def find_keys(current):
            if current is None:
                return 
            find_keys(current.left)
            result.append(current.key)
            find_keys(current.right)

        find_keys(self.root)
        return result


