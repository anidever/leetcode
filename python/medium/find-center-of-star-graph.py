# question can be found at leetcode.com/problems/find-center-of-star-graph

class Solution(self, edges: List[List[int]]]) -> int:
    seen = set()
    # flattening is not really necessary but you know ..
    flattened = [item for sublist in edges for item in sublist]
    for item in flattened:
        if item not in seen:
            seen.add(item)
        else:
            return item

    for edge in edges:
        for item in edge:
            if item not in seen:
                seen.add(item)
            else:
                return item
