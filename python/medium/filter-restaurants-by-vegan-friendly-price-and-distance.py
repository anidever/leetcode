from typing import List


class Solution:
    def filterRestaurants(
        self,
        restaurants: List[List[int]],
        veganFriendly: int,
        maxPrice: int,
        maxDistance: int,
    ) -> List[int]:
        def isValid(resto):
            if maxPrice >= resto[3]:
                if maxDistance >= resto[4]:
                    if not veganFriendly:
                        return True
                    return resto[2] == veganFriendly

        valids = [resto for resto in restaurants if isValid(resto)]
        return [
            resto[0]
            for resto in sorted(valids, key=lambda x: (x[1], x[0]), reverse=True)
        ]
