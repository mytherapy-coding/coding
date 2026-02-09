export function findCenter(edges: number[][]): number {
  const [a, b] = edges[0];
  const [c, d] = edges[1];

  if (a === c || a === d) return a;
  return b;
}

import { findCenter } from "./findCenter";

function test_findCenter() {
  console.log(findCenter([[1, 2], [2, 3], [4, 2]]), "== 2");
  console.log(findCenter([[1, 3], [2, 3], [3, 4]]), "== 3");
  console.log(findCenter([[5, 1], [5, 2], [5, 3], [5, 4]]), "== 5");
  console.log(findCenter([[10, 7], [7, 2]]), "== 7");
  console.log(findCenter([[100, 1], [50, 100], [100, 3]]), "== 100");
  console.log(findCenter([[8, 9], [9, 1], [2, 9]]), "== 9");
}

test_findCenter();
