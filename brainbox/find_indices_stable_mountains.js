function findStableMountains(height, threshold) {
  const result = [];
  for (let i = 1; i < height.length; i++) {
    if (height[i - 1] > threshold) {
      result.push(i);
    }
  }
  return result;
}

function test_findStableMountains() {
  console.log(findStableMountains([1,2,3,4,5], 2), "== [3, 4]");
  console.log(findStableMountains([10,1,10,1,10], 3), "== [1, 3]");
  console.log(findStableMountains([10,1,10,1,10], 10), "== []");
  console.log(findStableMountains([5,5,5,5], 4), "== [1, 2, 3]");
  console.log(findStableMountains([5,5,5,5], 5), "== []");
  console.log(findStableMountains([2,100], 50), "== [1]");
  console.log(findStableMountains([1,50,1,50,1], 10), "== [1, 3]");
}

test_findStableMountains();
