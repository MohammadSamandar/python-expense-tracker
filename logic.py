


class Expense():

    def __init__(self, title, price, date):

        self.title = title
        self.price = price
        self.date = date
        


class ExpenseTracker():

    def __init__(self):
        self.expenses_list = []


    def add_expense(self, expense):
        self.expenses_list.append(expense)



    def get_total_expense(self):

        total = 0

        for item in self.expenses_list:
            
            total += item.price
            
        return total





def add_expense_by_user(tracker):

    title = input('Add title of your expense: ')

    try:
        price = float(input('Add price of your expense: '))
    except ValueError:
        print('Please enter the amount in numbers.')
        
    date = input('Add date of your expense (15-07-2025): ')



    expense = Expense(title, price, date)
    tracker.add_expense(expense)
    print(f'expense: {title} added.')


def display_all_expenses(tracker):

    total = tracker.get_total_expense()
    print(f'\n>> total cost: {total}')


my_main_tracker = ExpenseTracker()







if __name__ == '__main__':



    while True:

  
        print('\n --- Expense tracker menu ---')
        print('1. Add expense')
        print('2. Show all expenses')
        print('3. Exit')


        choice = input('choose an option please (1-3): ')


        if choice == '1':

            add_expense_by_user(my_main_tracker)
        

        if choice == '2':

            display_all_expenses(my_main_tracker)

        
        elif choice == '3':

            print('Good Bye')
            break

        else:
            print('Invalid input. Please try again.')

