
// -------------------------
// Solution
// -------------------------
export function minOperations(nums: number[], k: number): number {
  const sum = nums.reduce((a, b) => a + b, 0);
  return sum % k;
}

// -------------------------
// Tests
// -------------------------
const tests: { nums: number[]; k: number; expected: number }[] = [
  { nums: [3, 9, 7], k: 5, expected: 4 },
  { nums: [1, 2, 3], k: 3, expected: 0 },
  { nums: [100, 200, 300], k: 7, expected: (100 + 200 + 300) % 7 },
  { nums: [10], k: 6, expected: 10 % 6 },
  { nums: [4, 4], k: 5, expected: (4 + 4) % 5 },
  { nums: [0, 0, 0], k: 4, expected: 0 },
  { nums: [5, 11, 14], k: 6, expected: (5 + 11 + 14) % 6 },
];

tests.forEach(({ nums, k, expected }) => {
  const result = minOperations(nums, k);
  console.log(`nums=${JSON.stringify(nums)}, k=${k} → ${result} (expected ${expected})`);
});
