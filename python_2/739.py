class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0 for item in temperatures]
        stack = list()
        for i in xrange(len(temperatures)):
            while True:
                if len(stack) == 0:
                    break
                if temperatures[i] <= stack[-1][1]:
                    break
                result[stack[-1][0]] = i - stack[-1][0]
                stack.pop()

            # first in Big, last in Small
            # Because item is smaller one by one
            stack.append((i, temperatures[i]))
        return result


def __main__():
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    o = Solution()
    result = o.dailyTemperatures(temperatures)
    print result


if __name__ == '__main__':
    __main__()

