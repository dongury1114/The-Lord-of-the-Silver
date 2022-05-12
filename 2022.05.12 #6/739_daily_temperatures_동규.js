temperatures = [73, 74, 75, 71, 69, 72, 76, 73];

// >>[1,1,4,2,1,1,0,0]

/**
 * @param {number[]} T
 * @return {number[]}
 */
var dailyTemperatures = function (T) {
  const stack = [];

  T.forEach((temperature, index) => {
    while (stack.length && T[stack[stack.length - 1]] < temperature) {
      const toBeReplacedIndex = stack.pop();
      T[toBeReplacedIndex] = index - toBeReplacedIndex; // replace with index inplace
    }
    stack.push(index);
  });

  while (stack.length) {
    T[stack.pop()] = 0;
  }

  return T;
};

// python code: Time limit
// class Solution:
//     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
//         ans = [0] * len(temperatures)

//         for i in range(len(temperatures)):
//             for j in range(i+1, len(temperatures)):
//                 if temperatures[j] > temperatures[i]:
//                     ans[i] = j-i
//                     break
//         return ans
