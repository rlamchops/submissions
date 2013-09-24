class Baby:
    def __init__(self,name="Z",happiness=10,hunger=0):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
    def hungerStatus(self):
        if(self.hunger > 10):
            print self.name + " is hungry."
        else:
            print self.name + " is not hungry."
    def happyStatus(self):
        if(self.happiness == 0):
            print self.name + " is very sad."
        elif (self.happiness == 10):
            print self.name + " is very happy."
        else:
            print self.name + " is just fine."

bob = Baby("Bob",0,3)
bob.hungerStatus()
bob.happyStatus()
