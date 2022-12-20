import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **balls):
    self.contents = []
    keys, amounts = list(balls.keys()), list(balls.values())
    i = 0
    for amount in amounts:
      self.contents+= amount * [keys[i]]
      i += 1
    
  def draw(self, amount):
    if amount > len(self.contents):
      res = self.contents
      self.contents = []
      return res
    else:
      i = 0
      res = []
      while i < amount:
        selection = random.choice(self.contents)
        res.append(selection)
        self.contents.remove(selection)
        i += 1

      return res
      
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for experiment in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    output = hat_copy.draw(num_balls_drawn)
    success = True
    for key in expected_balls:
        if output.count(key) < expected_balls[key]:
          success = False
    if success:
      M += 1
  return M/num_experiments
