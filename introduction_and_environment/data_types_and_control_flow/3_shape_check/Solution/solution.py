# Code your solution here
figure = str(input())
shapes = { '3':'Triangle' , '4':'Quadrilateral' , '5':'Pentagon' , "6":'Hexagon',
                 "7":'Heptagon', "8":'Octagon', '9':'Nonagon'}
if figure in shapes.keys():
    data = shapes[figure]
print(data)