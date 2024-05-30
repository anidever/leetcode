class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s:
            return 0

        counter = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            right_char, left_char = s[right], s[left]
            counter[right_char] = counter.get(right_char, 0) + 1

            while right >= left and len(counter) > k:
                counter[left_char] -= 1
                if counter[left_char] == 0:
                    del counter[left_char]
                left += 1

            longest = max(longest, right - left + 1)

        return longest