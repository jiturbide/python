from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        str0 = " ".join(strs)
        print("->", str0, "<-")
        return str0

    def decode(self, s: str) -> List[str]:
        if "" == s:
            return []
        elif s == " ":
            return [""]
        else:
            return s.split()

if __name__ == "__main__":
    s = Solution()
    e = s.encode([])
    r = s.encode(e)

    e = s.encode([""])
    r = s.encode(e)
