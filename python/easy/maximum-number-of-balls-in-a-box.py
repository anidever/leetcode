# question can be found on leetcode.com/problems/maximum-number-of-balls-in-a-box


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        hashmap = {}
        for num in range(lowLimit, highLimit + 1):
            count = 0
            while num:
                count += num % 10
                num //= 10
            if count in hashmap:
                hashmap[count] += 1
            else:
                hashmap[count] = 1

        return max(hashmap.values())
