
# This function is helpful for the Rectangle.intersects function
def line_segments_intersect(x1, w1, x2, w2):
  return x2 <= x1+w1 and x1 <= x2+w2


class Rectangle:

  def __init__(self,x,y,w,h):
    # This function has been provided for you.
    # The below lines are examples of assert statements. If the "w > 0" is false,
    # Then an AssertionError will be raised.
    assert w > 0, "Width cannot be zero or negative!"
    assert h > 0, "Height cannot be zero or negative!"

    self.x = x
    self.y = y
    self.w = w
    self.h = h

  @classmethod
  def from_points(cls, x1, y1, x2, y2):
    """ Create a Rectangle from two points """

    # TODO: These following two lines are wrong! Make the right sides of the
    # Following two assignments correct for ANY numerical values of x1 and x2
    # Hint: python has built-in functions min and max
    min_x = x1 # Replace this line!
    max_x = x2 # Replace this line!

    # TODO: These following two lines are wrong! Make the right sides of the
    # Following two assignments correct for ANY numerical values of y1 and y2
    # Hint: python has built-in functions min and max
    min_y = y1 # Replace this line!
    max_y = y2 # Replace this line!

    w = max_x - min_x
    h = max_y - min_y

    return cls(min_x, min_y, w, h)

  def area(self):
    """ Calculate and return the area of the rectangle """
    #TODO: Implement this function that finds and returns the area of this rectangle
    # using self.w and self.h

    return 0 # Replace this line!

  def perimeter(self):
    """ Calculate and return the perimeter of the rectangle """
    #TODO: Implement this function that finds and returns the perimeter of this rectangle
    # using self.w and self.h

    return 0 # Replace this line!


  def intersects(self, other):
    """ check if this rectangle intersects the Rectangle other """

    #TODO: Implement this function that checks whether the other Rectangle parameter
    # intersects this Rectangle. 

    # The rectangle intersects if it intersects in both the x and y axes! Use this fact
    # And the line_segments_intersect helper function above to implmement this function

    return False # Replace this line (and add lines above it)


class Square(Rectangle):

  def __init__(self, x, y, w, h):
    # TODO: In this function, write an assert statement that will be true when the width
    # input parameter (w) is not equal to the height input parameter (h).
    # See the assert statements in Rectangle as examples

    assert False # Replace this line!

    # The following line calls Rectangle's init function.
    super().__init__(x,y,w,h)