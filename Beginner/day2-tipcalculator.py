print("Welcome to the tip calculator!")
totalBill = input("What was the total bill? ")
tipPercent = int(
    input("What percentage tip would you like to give? 10, 12 or 15? "))
splitAmong = int(input("How many people to split the bill? "))

totalBill_Int = float(totalBill[1::])

finalBillPerPerson = (totalBill_Int + (totalBill_Int / 100)
                      * tipPercent)/splitAmong
print(f"Each person should pay: ${round(finalBillPerPerson,2)}")
