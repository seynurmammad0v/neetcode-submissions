class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = {}

        for c in s1:
            counter[c] = counter.get(c, 0) + 1

        l = 0
        curr_counter = {}
        matches = 0

        for r in range(len(s2)):

            # Add right character
            if s2[r] in counter:
                curr_counter[s2[r]] = curr_counter.get(s2[r], 0) + 1

                if curr_counter[s2[r]] == counter[s2[r]]:
                    matches += 1
                elif curr_counter[s2[r]] == counter[s2[r]] + 1:
                    matches -= 1

            # Shrink window
            if r - l + 1 > len(s1):
                if s2[l] in counter:
                    if curr_counter[s2[l]] == counter[s2[l]]:
                        matches -= 1

                    curr_counter[s2[l]] -= 1

                    if curr_counter[s2[l]] == counter[s2[l]]:
                        matches += 1

                l += 1

            if matches == len(counter):
                return True

        return False
