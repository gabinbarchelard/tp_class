###Échauffement

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f"Point({self.x}, {self.y})"             #on suit l'écriture attendue, la f-string permet d'avoir une chaîne de caractère modifiée en fonction de self
    
#     def norm(self):                 #norme euclidienne
#         return (self.x ** 2 + self.y ** 2) ** 0.5

 
# try:
#     p = Point(3, 4)
#     assert (p.x, p.y) == (3, 4)
#     assert p.norm() == 5.0
#     assert repr(p) == "Point(3, 4)"
#     q = Point(0, 1)
#     assert (q.x, p.x) == (0, 3)
# except Exception as e:
#     print("OOPS - Something's wrong")
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works !')


# class Bad:

#     def __init__(self) : 
#         self.item = []

#     def __repr__(self):
#         return f"{self.item})"  

#     def add(self, x):
#         self.item.append(x)

# a, b = Bad(), Bad()
# a.add(1)
# print(b.item)


# class Tirelire : 

#     def __init__(self):
#         self.pieces = []

#     def total(self) : 
#         return sum(self.pieces)

#     def deposit(self, value : float) : 
#         if not(value>0) : 
#             return 'Sale rat'
#         self.pieces.append(value)

#     def __len__(self) : 
#             return len(self.pieces)         #erreur ici 

#     def __repr__(self) : 
#             return f"Tirelire({len(self)} coins, total={self.total()})"

    


# pour tester

# try:
#     t = Tirelire()
#     t.deposit(0.5)
#     t.deposit(1)
#     assert len(t) == 2
#     assert t.total() == 1.5
#     assert repr(t) == "Tirelire(2 coins, total=1.5)"
#     other = Tirelire()
#     assert len(other) == 0
#     try:
#         other.deposit(-1)
#     except ValueError:
#         pass
#     else:
#         raise Exception("a negative value should raise ValueError")
# except Exception as e:
#     print("OOPS - Something's wrong")
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works !')


### la classe STUDENT

# from collections import defaultdict

# class Student:
#     def __init__(self, first_name: str, last_name: str):
#         self.nom = last_name
#         self.prenom = first_name
#         self.grades = defaultdict

#     def __repr__(self):
#         return f"{self.prenom} {self.nom}, Grades : {self.grades}"

# pour tester

# try:
#     student = Student("Achille", "Talon")
#     r = repr(student)
#     assert isinstance(r, str), "__repr__ must return a str"
#     assert "Achille" in r and "Talon" in r, f"first and last name should appear in {r!r}"
# except Exception as e:
#     print('OOPS - There is an issue in your code.')
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works !')


### gestion des notes

from collections import defaultdict

class Student:
    def __init__(self, first_name: str, last_name: str):
        self.nom = last_name
        self.prenom = first_name
        self.grades = defaultdict(list)             #le meilleur type pour ranger des notes correspondant à des matières est le dico

    def __repr__(self):
        return f"{self.prenom} {self.nom}, Grades : {dict(self.grades)}"
    
    def add_grade(self, course: str, grade: float): 
        if not (0 <= grade <= 20): 
            raise ValueError("La note doit être comprise entre 0 et 20")
        self.grades[course].append(grade)                  #si course n'existe pas, il le crée dans dico

        
# pour tester

try:
    student = Student("Achille", "Talon")
    student.add_grade("History", 10.)
    student.add_grade("History", 12.)
    try:
        student.add_grade("History", 25.)
    except ValueError:
        pass
    else:
        raise Exception("a grade outside of [0, 20] should raise ValueError")
except Exception as e:
    print('OOPS - There is an issue in your add_grade method.')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')
     
# class Student:
    
#     def __init__(self, first_name, last_name, 
#                  birth_year, birth_month, birth_day):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.birth_date = Date(birth_year, birth_month, birth_day)
        
#     def __repr__(self):
#         return f"{self.first_name} {self.last_name}"
    
#     def age(self) -> TimeDelta:
#         # the difference between 2 Dates is a TimeDelta
#         return Date.today() - self.birth_date
    
#     def repr_age(self) -> str:
#         return timedelta_as_year_month(self.age())