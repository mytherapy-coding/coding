function truncateSentence(s: string, k: number): string {
    return s.split(" ").slice(0, k).join(" ");
}

function test_truncateSentence() {
  console.log(truncateSentence("Hello world", 1), "== Hello");
  console.log(truncateSentence("Hello world", 2), "== Hello world");
  console.log(truncateSentence("What is your name", 3), "== What is your");
  console.log(truncateSentence("This is a test sentence", 4), "== This is a test");
  console.log(truncateSentence("Single", 1), "== Single");
}

test_truncateSentence();

