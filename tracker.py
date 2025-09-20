#----------Personal Expense Tracker----------
import csv 
class expenseTracker():
        def __init__(self):
            self.expenses = []
            try:
                with open('expenses.csv', newline='') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        self.expenses.append(row)  # Save to list
            except FileNotFoundError:
               print("Something went wrong!") 

        def view_expenses(self):
            print("\nAll Expenses:")
            if not self.expenses:
                print("No expenses recorded yet.")
            print(f"Sr. Amount Category")
            for i, (amount, category) in enumerate(self.expenses, start=1):
                print(f"{i}. {amount} in {category}")

        def save_expenses(self):
            with open("expenses.csv", "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerows(self.expenses)
            print("Expenses saved successfully!")

        def add_expense(self, amount, category):
            self.expenses.append([amount, category])
            print(f"Added expense: {amount} in {category}")

        def exp(self):
            while True:
                print("\n----Personal Expense Tracker----")
                print("1. Add an expense")
                print("2. View an expense")
                try:
                    choice = int(input("Choose option: "))
                    print(choice)
                except ValueError:
                    print("Only option number. Ex:- 2")
                    continue

                if choice == 1:
                    print("\n----Select Category----")
                    print("1. Food")
                    print("2. Transport") 
                    print("3. Entertainment") 
                    try:
                        category = int(input("Choose category: "))
                        print(category)
                    except ValueError:
                        print("Only category number. Ex:- 2")
                        continue 
                    

                    if category == 1:
                        category = "Food"
                    elif category == 2:
                        category = "Transport"
                    elif category == 3:    
                        category = "Entertainment"
                    else:
                        print("Successfully chosen!")
                        continue 


                    try:
                        amount = int(input("Enter amount: "))
                    except ValueError:
                        print("Amount must be a number")
                        continue
    
                    self.add_expense(amount, category)
                    self.save_expenses()

                elif choice == 2:
                    self.view_expenses()
obj = expenseTracker()
obj.exp()   # just call it, no print
     
