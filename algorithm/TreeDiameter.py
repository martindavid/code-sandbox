def process(tree):
  max_child_height=0
  secmax_child_height=0
  max_child_diameter=0
  for child in tree:
    child_height,child_diameter=process(child)
    if child_height>max_child_height:
      secmax_child_height=max_child_height
      max_child_height=child_height
    elif child_height>secmax_child_height:
      secmax_child_height=child_height
    if child_diameter>max_child_diameter:
      max_child_diameter=child_diameter
  height=max_child_height+1
  if len(tree)>1:
    diameter=max(max_child_diameter,max_child_height+secmax_child_height)
  else:
    diameter=max_child_diameter
  return height,diameter

def diameter(tree):
  height,diameter=process(tree)
  return diameter
