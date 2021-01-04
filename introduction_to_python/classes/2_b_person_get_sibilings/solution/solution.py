from operator import attrgetter
class Person:
    def __init__(self, name, age, spouse = None, children=[]):
        self.name = name
        self.age = age
        self.spouse = spouse
        self.children = children

class Child(Person):
    def __init__(self, name, age, spouse=None, children=[], parents=[]):
        super().__init__(name, age, spouse, children)
        self.parents = parents
    
    def get_siblings(self):
        siblings = []
        for parent in self.parents:
            siblings = list(set(siblings) | set(parent.children))
        siblings.remove(self)
        siblings = sorted(siblings, key=attrgetter('age'))
        siblings_names = [sib.name for sib in siblings]
        return siblings_names
