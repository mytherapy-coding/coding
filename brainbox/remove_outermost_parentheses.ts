export function removeOuterParentheses(s: string): string {
  let result = "";
  let balance = 0;

  for (const ch of s) {
    if (ch === "(") {
      if (balance > 0) result += ch; // keep only if not outermost
      balance++;
    } else {
      balance--;
      if (balance > 0) result += ch; // keep only if not outermost
    }
  }

  return result;
}

import { removeOuterParentheses } from "./removeOuterParentheses";

function test_removeOuterParentheses() {
  console.log(removeOuterParentheses("(()())(())"), "== ()()()");
  console.log(removeOuterParentheses("(()())(())(()(()))"), "== ()()()()(())");
  console.log(removeOuterParentheses("()()"), "== ");
  console.log(removeOuterParentheses("((()))"), "== (())");
  console.log(removeOuterParentheses("(()(()))"), "== ()(())");
}

test_removeOuterParentheses();
