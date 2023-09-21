def decodeString(s: str) -> str:
    st = []
    for ch in s:
        if ch != ']':
            st.append(ch)
        else:
            data = []
            while st[-1] != '[':
                data.append(st.pop())
            # st[-1] == '['
            st.pop()
            number = []
            while st and st[-1].isdigit():
                number.append(st.pop())
            num = int(''.join(reversed(number)))
            d = ''.join(reversed(data))
            st.append(num*d)
    return ''.join(st)


s = '10[10[10[10[10[10[a]]]]]]'
# print(decodeString(s))
print(len((decodeString(s))))
s = '12[abc]'
print(decodeString(s))
s = "3[a]2[bc]"
print(decodeString(s))