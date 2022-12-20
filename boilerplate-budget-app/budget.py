import math

class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.balance = 0

  def __str__(self):
    stars1 = "*"*(15 - math.floor((len(self.name))/2))
    stars2 = "*"*(15 - math.ceil((len(self.name))/2))
    ledger_str = stars1 + self.name + stars2
    for element in self.ledger:
      newline="\n" + '{:<23}{:>7}'.format(element["description"][0:23], str(element["amount"]))
      ledger_str += newline
    ledger_str += "\nTotal: " + str(self.balance)
    return ledger_str

  def deposit(self, amount, description=""):
    self.balance += amount
    self.ledger.append({"amount": amount, "description": description})
  

  def withdraw(self, amount, description=""):
    if(self.check_funds(amount)):
      self.balance -= amount
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False
  
  def get_balance(self):
    return self.balance

  def transfer(self, amount, dest_category):
    if(self.check_funds(amount)):
      self.withdraw(amount, f"Transfer to {dest_category.name}")
      dest_category.deposit(amount, f"Transfer from {self.name}")
      return True
    else:
      return False
    

  def check_funds(self, amount):
    if amount > self.balance:
      return False
    else:
      return True

def create_spend_chart(categories):
  names = [category.name for category in categories]
  balances = [category.balance for category in categories]
  percentages = [100*balance/sum(balances) for balance in balances]
  graph_str = "Percentage spent by category"
  # STEP 1 - Generate graph
  y_axis = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
  for y_value in y_axis:
    newline = "{:>4}".format(str(y_value) + "|")
    for percentage in percentages: #loop over category percentages
      if (percentage > y_value):
        newline += " o "
    graph_str += "\n" + newline
  # STEP 2 - Generate subtitles
  graph_str += "\n    " + "---"*len(categories) + "-"
  for i in range(len(max(names, key=len))): #return length of biggest string in list
    newline = "     "
    for name in names:
      try:
        newline += " " + name[i] + " "
      except: #if out of range --> just print spaces
        newline += "   "
    graph_str += "\n" + newline
  return graph_str