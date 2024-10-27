class Family():
    def __init__(self, name, age, relation):
        self.name = name
        self.age  = age
        self.relation = relation
    
    def eating(self):
        print("Lets have lunch together")

daughter = Family("Avira", "13", "daughter")
print(daughter.name)
#init function intialize the variables and is called automatically as soon as the object is created. 
