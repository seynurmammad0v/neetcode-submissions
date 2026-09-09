class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        arr = []

        for i, p in enumerate(position):
            arr.append((position[i], speed[i]))

        arr.sort(reverse=True)

        stack = []

        for pos, spd in arr:
            ttd = (target - pos) / spd

            if stack and stack[-1] >= ttd:
                continue

            stack.append(ttd)

        return len(stack)