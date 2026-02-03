def lengthOfLastWord(s: str) -> int:
    trimmed = s.rstrip()
    words = trimmed.split()
    last_word = words[-1]
    return len(last_word)

print(lengthOfLastWord("Hello World"))          # 5
print(lengthOfLastWord("luffy is still joyboy"))# 6
