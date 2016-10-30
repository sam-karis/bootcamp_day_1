def data_type(value):
  if type(value) == str:
    return len(value)
  elif value == None:
    return "no value"
  elif type(value) == bool:
    return value
  elif type(value) == int:
    if value < 100:
      return "less than 100"
    elif value > 100:
      return "more than 100"
    elif value == 100:
      return "equal to 100"
  elif type(value) == list:
    if len(value) >= 3:
      return value[2]
    else:
      return None