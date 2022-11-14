def to_jaden_case(s):
    import string
    return string.capwords(s, " ")


def to_jaden_case(s):
    words = s.split(" ")
    c =[]
    for w in words:
        c.append(w.capitalize())
    return " ".join(c)
        

def to_jaden_case(s):   
    return " ".join(w.capitalize() for w in s.split(" "))
