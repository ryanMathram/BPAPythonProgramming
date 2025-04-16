# 00146353
#SC1 importing the proper python files
import Pizzas
import PizzaMenu
class PizzaOrderController:
    #SC4 first part of exception handling of try
      file = open("PizzasText.txt", 'r')
      sym = ""
      name = ""
      price = 0.0
      inv = 0
      count = 1
      Pizza = []
      #SC3 accessing each line of the file
      for line in file:
         if line != "STOP":
               if count == 1:
                   #SC3 assigning the symbol variable
                  sym = line
               elif count == 2:
                   #SC3 assigning the name variable
                  name = line
               elif count == 3:
                   #SC3 assigning the price variable
                  price = float(line)
               elif count == 4:
                   #SC3 assigning the inventory variable
                  inv = int(line)
               else:
                   #SC2 adding the Pizzas object to the Pizza List
                  Pizza.append(Pizzas(sym,name,price,inv))
                  count = 0
               count += 1
         else:
            break
      Jay = PizzaMenu(Pizza)
      print("Current Active Inventory:\n\n")
      print(Jay)
      print(f"\n Inventory Total Value: $ {Jay.getInventoryTVL()}")
    #SC4 first part of exception handling of try
      '''except:
      print("OS error: [Errno 2] No such file  or directory: 'PizzasTest.txt'")
      #SC5 Printing exit command
      print("use exit() or Ctrl-Z plus Return to exit")
      #SC5 exits
      exit()'''
