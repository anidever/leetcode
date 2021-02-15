# question can be found on leetcode.com/problems/license-key-formatting/


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        clean = S.replace("-", "").upper()
        length = len(clean)
        mod = length % K
        result = clean[:mod]
        for idx in range(mod, length, K):
            result += "-" + clean[idx : idx + K]

        return result[1:] if not mod else result
