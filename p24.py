class NodeNaive: # not tested
    def __init__(self, value, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.value = value
        self._locked = False
    
    def is_locked(self):
        return self._locked

    def lock(self): # question is ambiguous, only look at descendants to lock
        if self.is_locked():
            raise RuntimeWarning("Node already locked")

        def descendants_locked(node):
            if node.is_locked():
                return True
    
            if node.left and node.right:
                return descendants_locked(node.left) \
                    or descendants_locked(node.right)
            elif node.left and not node.right:
                return descendants_locked(node.left)
            elif not node.left and node.right:
                return descendants_locked(node.right)
            else: # not node.left and not node.right
                return False

        if not descendants_locked(self):
            self._locked = True
        
        return self.is_locked()

    def unlock(self): # question is ambiguous, only look at ancestors to unlock
        if not self.is_locked():
            raise RuntimeWarning("Node already unlocked")
        
        current = self
        while current:
            if current.is_locked():
                break
            current = current.parent
        
        if not current: # traversal to root successful
            self._locked = False
        
        return not self._locked

class Node: # not tested
    def __init__(self, value, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.value = value
        self.locked_descendants_count = 0
        self._locked = False
    
    def is_locked(self):
        return self._locked

    def lock(self): # question is ambiguous, look at both descendants and ancestors
        if self.is_locked():
            raise RuntimeWarning("Node already locked")

        current = self
        while current:
            if current.is_locked():
                break
            current = current.parent

        if not current and self.locked_descendants_count == 0: # traversal to root successful
            self._locked = True
        
        current = self.parent
        while current:
            current.locked_descendants_count += 1
            current = current.parent
        
        return self.is_locked()

    def unlock(self): # question is ambiguous, look at both descendants and ancestors
        if not self.is_locked():
            raise RuntimeWarning("Node already unlocked")
        
        current = self
        while current:
            if current.is_locked():
                break
            current = current.parent
        
        if not current and self.locked_descendants_count == 0: # traversal to root successful
            self._locked = False
        
        current = self.parent
        while current:
            current.locked_descendants_count -= 1
            current = current.parent

        return not self._locked