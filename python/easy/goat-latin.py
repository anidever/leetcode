class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = "aeiouAEIOU"
        result = []
        for idx, char in enumerate(S.split()):
            if char[0] in vowels:
                result.append(char + "ma" + ("a" * (idx + 1)))
            else:
                result.append(char[1:] + char[0] + "ma" + ("a" * (idx + 1)))

        return " ".join(result)
