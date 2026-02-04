function countSymmetricIntegers(low, high) {
    let count = 0;

    for (let num = low; num <= high; num++) {
        const s = String(num);
        const length = s.length;

        // Skip odd-length numbers
        if (length % 2 !== 0) continue;

        const mid = length / 2;
        const left = s.slice(0, mid);
        const right = s.slice(mid);

        const leftSum = [...left].reduce((a, c) => a + Number(c), 0);
        const rightSum = [...right].reduce((a, c) => a + Number(c), 0);

        if (leftSum === rightSum) {
            count++;
        }
    }

    return count;
}

console.log(countSymmetricIntegers(1, 100)); // 9
