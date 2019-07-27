import os
from tkinter import *
from tkinter.ttk import *

path = os.path.dirname(__file__) + '/'


def rounding(n, digit=0):
    """Return the rounding of n"""
    if n < 0:
        number = int(n * 10 ** digit - 0.5) / 10 ** digit
    else:
        number = int(n * 10 ** digit + 0.5) / 10 ** digit

    if number % 1 == 0:
        return int(number)
    return number


def format_currency(n):
    return re.sub(r'\B(?=(\d{3})+(?!\d))', ',', str(n))


def integer_number(raw):
    temp = re.sub(r'[^\d]+', '', raw)
    return re.sub(r'^0+(?!$)', '', temp)


def string_to_int(raw):
    temp = re.sub(r'[^\d]+', '', raw)
    return int(temp)


def on_change(entry):
    temp = integer_number(entry.get())
    if temp:
        value = format_currency(temp)
    else:
        value = ''

    entry.delete(0, END)
    entry.insert(0, value)


# noinspection PyUnusedLocal
def calculate(*args):
    capital_val = string_to_int(capital.get())
    percent_val = percent.get()
    period_val = string_to_int(period.get())

    try:
        capital_val = int(capital_val)
        percent_val = float(percent_val)
        period_val = int(period_val)
        if period_val < 0 or percent_val < 0:
            profit.set('Input error!')
            return

        percent_val /= 100
        profit_val = 0
        income_val = capital_val
        for i in range(period_val):
            profit_val += income_val * percent_val
            income_val += (income_val * percent_val)

        invest.set(f'Capital: {format_currency(rounding(capital_val, 2))}')
        profit.set(f'Profit: {format_currency(rounding(profit_val, 2))}')
        income.set(f'Income: {format_currency(rounding(income_val, 2))}')

    except Exception:
        invest.set('')
        income.set('')
        profit.set('Input error!')


if __name__ == '__main__':
    root = Tk()
    root.title("An's revenue calculator v1.0")
    img = PhotoImage(file=path + 'icon.png')
    root.iconphoto(False, img)
    root.minsize(150, 150)
    root.resizable(False, False)

    style = Style()
    themes = style.theme_names()
    if 'clam' in themes:
        style.theme_use('clam')
    elif 'aqua' in themes:
        style.theme_use('aqua')
    else:
        style.theme_use('default')

    main_frame = Frame(root, padding=10)
    main_frame.grid(column=0, row=10, sticky='wnes')

    capital_label = Label(main_frame, text='Capital')
    capital_label.grid(row=0, column=0)

    capital = StringVar()
    capital_entry = Entry(main_frame, textvariable=capital)
    capital_entry.grid(row=0, column=1, padx=5, pady=5)
    capital.trace('w', lambda name, index, mode, entry=capital_entry: on_change(entry))

    invest = StringVar()
    invest_label = Label(main_frame, textvariable=invest)
    invest_label.grid(row=0, column=2)

    percentLbl = Label(main_frame, text='Percent')
    percentLbl.grid(row=1, column=0)

    percent = StringVar()
    percent_entry = Entry(main_frame, textvariable=percent)
    percent_entry.grid(row=1, column=1, padx=5, pady=5)
    percent.trace('w', lambda name, index, mode, entry=percent_entry: on_change(entry))

    profit = StringVar()
    profit_label = Label(main_frame, textvariable=profit)
    profit_label.grid(row=1, column=2)

    period_label = Label(main_frame, text='Period number')
    period_label.grid(row=3, column=0)

    period = StringVar()
    period_entry = Entry(main_frame, textvariable=period)
    period_entry.grid(row=3, column=1, padx=5, pady=5)
    period.trace('w', lambda name, index, mode, entry=period_entry: on_change(entry))

    income = StringVar()
    income_label = Label(main_frame, textvariable=income)
    income_label.grid(row=3, column=2)

    calculate_button = Button(main_frame, text='Calculate', command=calculate)
    calculate_button.grid(row=4, column=1, pady=5)

    capital_entry.focus()
    root.bind('<Return>', calculate)
    root.mainloop()
