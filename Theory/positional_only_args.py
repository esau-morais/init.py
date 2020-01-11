def simple_math(a, b, c, /, any_print='Simple Math'):
  """ Simple Math
    Everytinhg behing '/', can't be called by your parameter name; 
    Only thing that need to do is change the values;
    Everything in front can be called by your parameter name (in your def position).
  """
  print(any_print)
  return a * b + c


print(simple_math(10, 10, 10, any_print='Math Account'))