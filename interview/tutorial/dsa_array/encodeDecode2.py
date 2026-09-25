from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        # Edge case [] -> ""
        # ["",""] -> 0#0#

        if strs is None or len(strs) == 0:
            return ""

        whole_str = ""

        for s in strs:
            len_str = len(s)
            encoded_str = self.transform(s)
            whole_str += str(len_str) + "#" + encoded_str

        return whole_str

    def decode(self, s: str) -> List[str]:
        if s is None or len(s) == 0:
            return []

        strs_to_process = s.split("#")
        to_read = int(strs_to_process[0])
        decoded_list = []
        idx = 1
        while idx < len(strs_to_process):
            not_decoded = strs_to_process[idx][0:to_read]
            decoded_str = self.restore(not_decoded)

            str_to_read = strs_to_process[idx][to_read:len(strs_to_process[idx])]        
            #print(to_read, ",", not_decoded, ",", decoded_str, ",", str_to_read, "," )

            decoded_list.append(decoded_str)
            idx += 1
            if idx < len(strs_to_process):
                to_read = int(str_to_read)

        return decoded_list

    def transform(self, s: str) -> str:
        return s

    def restore(self, s: str) -> str:
        return s

if __name__ == '__main__':
    print("Start of the program")

    testCases = [
        ([], []),
        (["", "", ""], ["", "", ""]),
        (["Hello", "world", "1234"], ["Hello", "world", "1234"]),
        (["#"], ["#"])
    ]
    sol = Solution()
    for input, expected in testCases:
        result = sol.decode(sol.encode(input))
        if result == expected:
            print("Pass", input, result)
        else:
            print("Fail", input, result, expected)
