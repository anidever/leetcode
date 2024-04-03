class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0

        maxDepthOfChildren = 0
        for child in root.children:
            depth = self.maxDepth(child)
            maxDepthOfChildren = max(maxDepthOfChildren, depth)

        return maxDepthOfChildren + 1


class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        
        if not root.children:
            return 1
        
        height = [self.maxDepth(node) for node in root.children]
        
        return max(height) + 1
        