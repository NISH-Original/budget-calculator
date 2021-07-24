import utilities as ut
import pythonColours as pc

#All global variables
opt = 0
expense = []
optRep = 0
expelt = []

#All functions Below:

#homeScr is a function to show the homescreen.
def homeScr():
    global opt
    opt = ut.getvalidOpt(1, 4, input(pc.yellow+'What do you want to do?\nEnter Expenditure [Press 1]\nView Analysis [Press 2]\nExpenditure List Options [Press 3]\nClose program [Press 4]\nType in an option: '))

#This is the function which appends expenses to the list.
def insExp():
    global expense
    exp = ut.validateVal(input(pc.white+"Enter amount: "))
    reason = str(input("Enter expense type (Eg. Food, Electricity bills, etc.): "))
    ut.line()
    expelt = [exp, reason]
    expense.append(expelt)
    if str.lower(input("Want to continue?(y): ")) == "y":
        ut.line()
        insExp()    
    else:
        ut.line()
        print(pc.cyan+"Your expenses are:")
        for i in range(len(expense)):
           print(pc.cyan+"{}) $ {} | {}" . format(i+1, expense[i][0], expense[i][1])) 
        ut.line()
        homeScr()
        ut.line()    

#This function shows the report.
def viewReport():
    optRep = ut.getvalidOpt(1, 3, input(pc.yellow+'What do you want to see?\nView top expenses [Press 1]\nView percentage of budget spent [Press 2]\nGo back home [Press 3]\nType in an option: '))
    ut.line()

    if optRep == 1:
        top = ut.getvalidOpt(1, len(expense), input(pc.yellow+"How many top expenses do you want to view? "))
        expense.sort(reverse = True)
        for i in range(top):
            print(pc.cyan+"{}) $ {} | {}" . format(i+1, expense[i][0], expense[i][1]))   
    
    if optRep == 2:
        exp = []
        for i in range(len(expense)):
            exp.append(expense[i][0])
        total = sum(exp)
        print(pc.cyan+"You total expense is $",total)
        percent = 100*(total/budget)
        print("You have spent {}%" . format(percent),"of your budget")
        
        if percent >= 100:
            print(pc.red+"Oops, You've gone over budget.")
        if 0 < percent < 100:
            print(pc.green+"Good! You'r totally in budget.")
        if percent == 0:
            print(pc.white+"You haven't spent even a dollar! If you haven't filled up your expense list, please do so.")
        ut.line()
    if optRep == 3:
        homeScr()  

#This functions deletes elements in the expense list.
def delElem():
    delete = ut.getvalidOpt(1, len(expense), input(pc.yellow+"Please add the serial number of the expense you want to delete: "))
    expense.pop(delete-1)
    ut.line()
    if str.lower(input("Want to continue?(y): ")) == "y":
        delElem()
        ut.line()
    else:
        ut.line()
        print(pc.cyan+"Your expenses are:")
        for i in range(len(expense)):
           print(pc.cyan+"{}) $ {} | {}" . format(i+1, expense[i][0], expense[i][1])) 
          

#This is the function to edit the function of the list.
def expOpt():
    expEdit = ut.getvalidOpt(1, 3, input(pc.yellow+"What do you want to do?\nDelete items in list [Press 1]\nEmpty the whole list [Press 2]\nGo back home [Press 3]\nType in an option:  "))

    if expense == []:
        print(pc.red+"Oops! Your expense list is empty, please fill it up first.")
        ut.line()
        homeScr()
    if expEdit == 1:
        delElem()
        ut.line()
        homeScr()
        ut.line()
    if expEdit == 2:
        expense.clear()
        print(pc.white+"Done!")
        ut.line()
        homeScr()

print(pc.white+"Hello! This code will help you in calculating your monthly budget.")
ut.line()

budget = ut.validateVal(input(pc.yellow+"First, to start your money-saving journey, enter your budget for the month: "))

ut.line()
homeScr()
ut.line()

#main body.
while True:    
    if opt == 1:
        while True:
            insExp()                    
            break
   
    if opt == 2:
        ut.line()
        viewReport()

    if opt == 3:
        expOpt()
    
    if opt == 4:
        print(pc.bright_cyan+"Good Bye!")
        break
