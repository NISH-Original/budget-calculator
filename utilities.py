def validateVal(v):
  try:
    x = float(v)
    return x
  except:
    x = validateVal(input(pc.red+"Please enter a valid number: "))
    return x

def validateInt(v):
  try:
    x = int(v)
    if int(v)<=0:
      x=validateInt(input("PLease enter a valid number: "))
    return x
  except:
    x=validateInt(input("Please enter a valid number: "))
    return x

def validateOpt(v):
  try:
    x = int(v)
    if int(v)<=0:
      x=validateOpt(input("PLease enter a valid number: "))
    elif int(v)>5:
      x=validateOpt(input("PLease enter a valid number: "))
    return x
  except:
    x=validateOpt(input("Please enter a valid number: "))
    return x

#validates options, if any. For example, if we have to choose options from 1 to 4, use it like so: utilities.getvalidOpt(1, 4, input("Enter option: "))
def getvalidOpt(mini, maxi, intVal):
        try:
            intVal = int(intVal)
            if intVal is not None and intVal >= mini and intVal <= maxi:
              return intVal
            else:
              intVal = getvalidOpt(mini, maxi, input(pc.bright_red+"Please enter a valid number: "))
              return intVal  
        except ValueError:
            intVal = None
            intVal = getvalidOpt(mini, maxi, input(pc.bright_red+"Please enter a valid number: "))
            return intVal
