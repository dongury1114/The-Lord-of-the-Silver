class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result_x = collections.deque()
        if x == 0:
            result_x.append(0)

        result_y = collections.deque()
        if y == 0:
            result_y.append(0)

        count = 0

        def _DFS(decimal, result):
            if decimal == 0:
                return

            _DFS(decimal // 2, result)
            result.append(decimal % 2)

            return result

        if x != 0:
            result_x = _DFS(x, result_x)

        if y != 0:
            result_y = _DFS(y, result_y)

        if len(result_x) >= len(result_y):
            larger_length = len(result_x)
            smaller_length = len(result_y)

            for i in range(larger_length - smaller_length):
                result_y.appendleft(0)
        else:
            larger_length = len(result_y)
            smaller_length = len(result_x)

            for i in range(larger_length - smaller_length):
                result_x.appendleft(0)

        for i in range(larger_length):
            if result_x[i] != result_y[i]:
                count += 1

        return count


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = bin(x ^ y)

        return result.count('1')
