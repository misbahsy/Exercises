# Code your solution here
data =[]
vowel = ['A', 'E', 'I', 'O', 'U']
string = 'BYTE ACADEMY'

for char in string:
    if char not in vowel:
        data.append(char)

print(data)



