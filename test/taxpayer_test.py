from dataclasses import dataclass


@dataclass
class Subject:
    title:str
    number:str
    students: list['Student']=None


@dataclass(frozen=True)
class Student:
    name:str
    age:int
    subjects:list[Subject]

sub1 = Subject('Math', '456789')
sub2 = Subject('CS','45678')

st1 = Student('Slava', 44, [sub1, sub2])
st2 = Student('Alena', 38, [sub2])
st3 = Student('John', 45, [sub2])

sub1.students = [st1]
sub2.students = [st1, st2, st3]

students = [st1, st2, st3]
subjects =[sub1, sub2]
print(students)
print(subjects)

'''

'''