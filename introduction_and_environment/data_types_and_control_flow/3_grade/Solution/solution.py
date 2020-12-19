# Code your solution here
mark = int(input())
#error of marks vs mark
if mark > 90:
    grade = 'A+'
elif mark >70 and mark < 90:
    grade = 'B'
elif mark >50 and mark < 70:
    grade = 'C'
elif mark >35 and mark < 50:
    grade = 'D'
else:
    grade = 'Fail'

print(grade)