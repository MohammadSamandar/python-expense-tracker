import tkinter as tk
from tkinter import messagebox
from logic import *

def handle_add_expense():

    title = title_entry.get()
    price_str = price_entry.get()
    date = date_entry.get()


    if not title or not price_str or not date:

        messagebox.showerror('Please all fields.')
        return
    
    try:
        price = float(price_str)
    except ValueError:
        messagebox.showerror("The amount must be a number.")


    new_expense = Expense(title, price, date)
    my_tracker.add_expense(new_expense)


    messagebox.showinfo('Success', f'{title} expense was successfully recorded. ')
    title_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

    handle_show_total()


def handle_show_total():
    total_cost  = my_tracker.get_total_expense()
    result_label.config(text=f"Total Expense is : {total_cost}")




my_tracker = ExpenseTracker()

window = tk.Tk()
window.title("Expense Tracker")
window.geometry('1080x500')

main_frame = tk.Frame(window, padx=20, pady=20)
main_frame.pack(side='left', fill='y')

title_label = tk.Label(main_frame, text='Title')
title_label.pack()
title_entry = tk.Entry(main_frame)
title_entry.pack()

price_label = tk.Label(main_frame, text='Expense')
price_label.pack()
price_entry = tk.Entry(main_frame)
price_entry.pack()

date_label = tk.Label(main_frame, text='Date')
date_label.pack()
date_entry = tk.Entry(main_frame)
date_entry.pack()

add_button = tk.Button(main_frame, text='submit', command=handle_add_expense)
add_button.pack()


result_label = tk.Label(window, text='total expense: 0')
result_label.pack()



window.mainloop()