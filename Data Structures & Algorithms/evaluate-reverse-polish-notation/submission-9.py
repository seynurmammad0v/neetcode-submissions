class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        operators = {'/','*','+','-'}
        for t in tokens:
            if t in operators:
                s = nums.pop()
                f = nums.pop()
                nums.append(calculate(f,s,t))
                
            else:
                nums.append(int(t))     
        
        return nums[0]

def calculate(first, second, t):
    match t:
        case '/':
            return int(first/second)
        case '*':
            return first*second
        case '+':
            return first+second
        case '-':
            return first-second