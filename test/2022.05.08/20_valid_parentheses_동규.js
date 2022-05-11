function solution(s) {
  const stack = [];
  const closeToOpen = {
    ")": "(",
    "]": "[",
    "}": "{",
  };
  for (let c of s) {
    if (closeToOpen[c]) {
      if (stack.length > 0 && closeToOpen[c] === stack[stack.length - 1]) {
        stack.pop();
      } else {
        return false;
      }
    } else {
      stack.push(c);
    }
  }
  return stack.length === 0;
}

let s = "()[]{}";
console.log(solution(s));
