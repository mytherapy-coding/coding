class Table:
    pass

d = Table()
d.set("Slava", 10000)
d.set("Alena", 500000)

s = d.get("Slava")
print(s)


print(d.set("Slava", 20000))


dd ={}
dd["Slava"] = 100000
dd.__setitem__("slava", 10000)