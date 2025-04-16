import Pizzas
class PizzaMenu:

  #SC6 constructor with data structure attribute
  def __init__(self,data):
    self.data = data

  #SC7 creates pizza objects and adds to "data" structure
  def createPizza(self, sym, name, price, inv):
    self.data.append(Pizzas(sym,name,price,inv))

  #SC8
  def getInventoryTVL(self):
    total = 0.0
    for i in self.data:
      total += i.getValue()
    return total

  def __str__(self):
    full = ""
    for i in self.data:
      # SC9
      full += i.printPizzaType + "\n"
    return full
