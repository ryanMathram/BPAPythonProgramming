class Pizzas:
  def __init__(self,symbol,name,pri,invent):
    self.symbol = symbol
    self.name = name
    self.pri = pri
    self.invent = invent

  def getValue(self):
    return self.pri * self.invent

  def __str__(self):
    return f"Pizza Type Symbol:{self.symbol}\n\tPizza Name: {self.name}\n\tUnit Price: {self.pri}\n\tActive Inventory: {self.invent}\n\t Estimated Inventory ($): {self.getValue()}"

  def printPizzaType(self):
    return self



  
