from dataclasses import dataclass


@dataclass
class Taxpayer:
    name: str
    age: int
    tin: int
    sex: str
    salary: int
    spouse:'Taxpayer'=None

print('--------')
t2 = Taxpayer('ALena', 38, 3456789, 'female', 345678)
print(t2)
t1 = Taxpayer('Slava', 44, 567890, 'male', 234567)
t3 = Taxpayer('John', 45, 987667, 'male', 987654, t1)
t1.spouse = t3

print(t1)
print(t3)
print('--------')


taxpayers = [t1, t2, t3]

print(taxpayers)

for t in taxpayers:
    print(t.name)

print([t.name for t in taxpayers])

print({t1, t2, t3})
taxpaid = {t1:500, t2:600, t3:700}
print(taxpaid)

tax_owned_d = {t1.name:t1.salary*0.2-taxpaid[t1], t2.name:t2.salary*0.2-taxpaid[t2], t3.name:t3.salary*0.2}
print(tax_owned_d)

for t in taxpayers:
    print(t.salary*0.2-taxpaid[t])

print([t.salary*0.2-taxpaid[t] for t in taxpayers])

print({t.name:t.salary*0.2-taxpaid[t] for t in taxpayers})

'linked list'