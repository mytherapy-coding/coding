export function countConsistentStrings(allowed: string, words: string[]): number {
  const allowedSet = new Set(allowed);
  let count = 0;

  for (const word of words) {
    let ok = true;
    for (const ch of word) {
      if (!allowedSet.has(ch)) {
        ok = false;
        break;
      }
    }
    if (ok) count++;
  }

  return count;
}


