function totalPenalty(daysLate: number[]): number {
    let total = 0;

    for (const d of daysLate) {
        if (d === 1) {
            total += 1;
        } else if (d >= 2 && d <= 5) {
            total += 2 * d;
        } else if (d > 5) {
            total += 3 * d;
        }
    }

    return total;
}

console.log(totalPenalty([5, 1, 7]));   // 32
console.log(totalPenalty([1, 1]));      // 2

// extra tests
console.log(totalPenalty([2, 3, 4, 5])); // 28
console.log(totalPenalty([6, 10]));     // 48
console.log(totalPenalty([]));          // 0
