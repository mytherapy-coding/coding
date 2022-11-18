def reverse_words1(text):
    words = text.split(" ")
    res = []
    for w in words:
        res.append(w[::-1])
    return " ".join(res)
    
def reverse_words2(text):
    return " ".join(w[::-1] for w in text.split(" "))
    
def text_reverse_words():
    tab: tuple[tuple[str, str], ...] = (
        ('hi', 'ih'),
        ('hello', 'olleh'),
        ('Hello world', 'olleH dlrow'),
    )
    for f in reverse_words1, reverse_words2:     
        for text, expected in tab:
            result = f(text)
            assert result == expected, f'test failed on {f.__name__}({text}), {expected=}, {result=}'
        
    print('end of tests')   
    
text_reverse_words()  
