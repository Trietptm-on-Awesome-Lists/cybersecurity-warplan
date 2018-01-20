class Solution(object):

    def calPoints(self, ops):
        """
        Integer is a valid score
        C means cancel last score
        + means add the last two valid scores
        D means double the last score
        at any time need to keep two valid scores
        :type ops: List[str]
        :rtype: int
        """
        scores_stack = []
        score_sum = 0
        for val in ops:
            if is_int(val):
                scores_stack.append(int(val))
            elif val == "C":
                ignore_item = scores_stack.pop()
            elif val == "D":
                scores_stack.append(2*scores_stack[-1])
            elif val == "+":
                scores_stack.append(scores_stack[-1] + scores_stack[-2])

        return (sum(scores_stack))

def is_int(num):
    try:
        num = int(num)
        return True
    except ValueError:
        return False

sol = Solution()

arr = ["5","2","C","D","+"]
arr = ["5","-2","4","C","D","9","+","+"]
res = sol.calPoints(arr)
print(res)
