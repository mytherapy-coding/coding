export function reversePrefix(word: string, ch: string): string {
  const idx = word.indexOf(ch);
  if (idx === -1) return word;
  return word.slice(0, idx + 1).split("").reverse().join("") + word.slice(idx + 1);
}

import { reversePrefix } from "./reversePrefix";

function test_reversePrefix() {
  console.log(reversePrefix("abcdefd", "d"), "== dcbaefd");
  console.log(reversePrefix("hello", "l"), "== lleho");
  console.log(reversePrefix("hello", "z"), "== hello");
  console.log(reversePrefix("abc", "c"), "== cba");
  console.log(reversePrefix("a", "a"), "== a");
  console.log(reversePrefix("xyz", "x"), "== xyz"); // reversing only 'x' does nothing
}

test_reversePrefix();
