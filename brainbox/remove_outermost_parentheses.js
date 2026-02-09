function removeOuterParentheses(s) {
  let result = "";
  let balance = 0;

  for (const ch of s) {
    if (ch === "(") {
      if (balance > 0) result += ch;
      balance++;
    } else {
      balance--;
      if (balance > 0) result += ch;
    }
  }

  return result;
}


// -------------------- TESTS --------------------

function test_removeOuterParentheses() {
  console.log(removeOuterParentheses("(()())(())"), "== ()()()");
  console.log(removeOuterParentheses("(()())(())(()(()))"), "== ()()()()(())");
  console.log(removeOuterParentheses("()()"), "== ");
  console.log(removeOuterParentheses("((()))"), "== (())");
  console.log(removeOuterParentheses("(()(()))"), "== ()(())");
}

test_removeOuterParentheses();
