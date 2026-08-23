class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        return "".join(encoded)

    # 9#sests5#aafsad 
    def decode(self, s: str) -> List[str]:
        decoded = []
        index = 0
        while index < len(s):
            start = index
            while s[index] != "#":
                index+=1
            lenght = int(s[start:index])
            index+=1
            newIndex = index+lenght 
            word = s[index:newIndex]
            decoded.append(word)
            index = newIndex
        return decoded




