class a:
  def __init__(self,name,loc):
    self.name=name
    self.loc=loc
  def printme(self):
    print("name is :",self.name)
  def location(self):
    print("I am from {}.format(self.loc))
    
names=a("joky","DD")
names.printme()
names.location()
