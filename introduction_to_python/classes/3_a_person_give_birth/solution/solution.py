class Person:
    def __init__(self, name, age, spouse = None, children=[]):
        self.name = name
        self.age = age
        self.spouse = spouse
        self.children = children

    def give_birth(self, child_name):
        baby = Child(child_name, 0, None, [], [self])
        self.children.append(baby)
        if self.spouse:
            self.spouse.children.append(baby)
            baby.parents.append(self.spouse)

class Child(Person):
    def __init__(self, name, age, spouse=None, children=[], parents=[]):
        super().__init__(name, age, spouse, children)
        self.parents = parents