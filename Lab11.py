
# #1
# def read_file(file_path):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()[1:]
#         return [line.strip().split(',') for line in lines]

# cs_majors = read_file('cs.txt')
# math_majors = read_file('math.txt')

# cs_set = set(tuple(student) for student in cs_majors)
# math_set = set(tuple(student) for student in math_majors)

# # Question 1
# print("1. The data files cs.txt and math.txt contain the names of the computer science majors and math majors.")
# print()

# #a
# double_majors = cs_set & math_set
# if double_majors:
#     print("1a. All of the Math-CS Double Majors:")
#     print(double_majors)
#     print()

# #b
# math_or_cs = cs_set | math_set
# if math_or_cs:
#     print("1b. All of the People Majoring in Math or CS:")
#     print(math_or_cs)
#     print()

# #c
# strict_cs = cs_set - math_set
# if strict_cs:
#     print("1c. All of the People Who Are Strictly CS Majors:")
#     print(strict_cs)
#     print()
# print("------------------------------------------------------------")
# print()
# # Question 2
# print("2. The file studentYear.txt has the same students (+a few extra) ranked according to their class year.")
# print()

# student_years = read_file('studentYear.txt')
# student_year_set = set(tuple(student) for student in student_years)

# # 2a
# sophomore_cs = set()
# for student in student_year_set:
#     if student[0] == '2' and tuple(student[1:]) in cs_set:
#         sophomore_cs.add(student)
# if sophomore_cs:
#     print("2a. All Sophomore Level CS Majors:")
#     print(sophomore_cs)
#     print()

# # 2b
# freshmen_not_math_cs = set()
# for student in student_year_set:
#     if student[0] == '1' and tuple(student[1:]) not in (cs_set | math_set):
#         freshmen_not_math_cs.add(student)
# if freshmen_not_math_cs:
#     print("2b. All Freshmen Who Are Not Majoring in Math or CS:")
#     print(freshmen_not_math_cs)
#     print()

# # 2c
# senior_math_cs = set()
# for student in student_year_set:
#     if student[0] == '4' and tuple(student[1:]) in (cs_set | math_set):
#         senior_math_cs.add(student)
# if senior_math_cs:
#     print("2c. All Senior Math and CS Majors:")
#     print(senior_math_cs)
#     print()







#1
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]
        return [line.strip().split(',') for line in lines]

cs_majors = read_file('cs.txt')
math_majors = read_file('math.txt')

cs_set = set(tuple(student) for student in cs_majors)
math_set = set(tuple(student) for student in math_majors)

# Question 1
print("1. The data files cs.txt and math.txt contain the names of the computer science majors and math majors.")
print()

#a
double_majors = cs_set & math_set
if double_majors:
    print("1a. All of the Math-CS Double Majors:")
    for student in double_majors:
        print(f"{student[0]} {student[1]}")
    print()

#b
math_or_cs = cs_set | math_set
if math_or_cs:
    print("1b. All of the People Majoring in Math or CS:")
    for student in math_or_cs:
        print(f"{student[0]} {student[1]}")
    print()

#c
strict_cs = cs_set - math_set
if strict_cs:
    print("1c. All of the People Who Are Strictly CS Majors:")
    for student in strict_cs:
        print(f"{student[0]} {student[1]}")
    print()
print("------------------------------------------------------------")
print()
# Question 2
print("2. The file studentYear.txt has the same students (+a few extra) ranked according to their class year.")
print()

student_years = read_file('studentYear.txt')
student_year_set = set(tuple(student) for student in student_years)

# 2a
sophomore_cs = set()
for student in student_year_set:
    if student[0] == '2' and tuple(student[1:]) in cs_set:
        sophomore_cs.add(student)
if sophomore_cs:
    print("2a. All Sophomore Level CS Majors:")
    for student in sophomore_cs:
        print(f"{student[1]} {student[2]}")
    print()

# 2b
freshmen_not_math_cs = set()
for student in student_year_set:
    if student[0] == '1' and tuple(student[1:]) not in (cs_set | math_set):
        freshmen_not_math_cs.add(student)
if freshmen_not_math_cs:
    print("2b. All Freshmen Who Are Not Majoring in Math or CS:")
    for student in freshmen_not_math_cs:
        print(f"{student[1]} {student[2]}")
    print()

# 2c
senior_math_cs = set()
for student in student_year_set:
    if student[0] == '4' and tuple(student[1:]) in (cs_set | math_set):
        senior_math_cs.add(student)
if senior_math_cs:
    print("2c. All Senior Math and CS Majors:")
    for student in senior_math_cs:
        print(f"{student[1]} {student[2]}")
    print()