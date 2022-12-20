import math

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

  def set_width(self, new_width):
    self.width = new_width

  def set_height(self, new_height):
    self.height = new_height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2*self.width + 2*self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    picture = ''
    if (self.height > 50 or self.width > 50):
      return 'Too big for picture.'
    else:
      for i in range(self.height):
        for j in range(self.width):
          picture += '*'
        picture += '\n'
      return picture

  def get_amount_inside(self, shape):
    return math.floor(self.get_area()/shape.get_area())

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)

  def __str__(self):
    return f'Square(side={self.width})'

  def set_side(self, new_side):
    super().set_width(new_side)
    super().set_height(new_side)

  def set_width(self, new_width):
    self.width = new_width
    self.height = new_width

  def set_height(self, new_height):
    self.width = new_height
    self.height = new_height
  