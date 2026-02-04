function lengthOfLastWord(s) {
    const trimmed = s.trim();
    const words = trimmed.split(/\s+/);
    const lastWord = words[words.length - 1];
    return lastWord.length;
}

console.log(lengthOfLastWord("Hello World"));            // 5
console.log(lengthOfLastWord("luffy is still joyboy"));  // 6
