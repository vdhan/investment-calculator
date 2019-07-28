import os
from tkinter import *
from tkinter.ttk import *

path = os.path.dirname(__file__) + '/'


def rounding(n, digit=0):
    """Return the rounding of n"""
    if n < 0:
        num = int(n * 10 ** digit - 0.5) / 10 ** digit
    else:
        num = int(n * 10 ** digit + 0.5) / 10 ** digit

    if num % 1 == 0:
        return int(num)
    return num


def format_currency(n):
    parts = str(n).split('.', 1)
    parts[0] = re.sub(r'\B(?=(\d{3})+(?!\d))', ',', parts[0])
    return '.'.join(parts)


def integer_number(raw):
    regexes = (r'[^\d]+', r'^0+(?!$)')
    for regex in regexes:
        raw = re.sub(regex, '', raw)

    return raw


def float_number(raw):
    regexes = (r'[^\d]+', r'^0+(?!$)')
    parts = raw.split('.', 1)
    for regex in regexes:
        parts[0] = re.sub(regex, '', parts[0])

    if len(parts) > 1:
        parts[1] = re.sub(r'[^\d]+', '', parts[1])
    return '.'.join(parts)


def currency_to_num(raw):
    parts = raw.split('.', 1)
    for idx, val in enumerate(parts):
        parts[idx] = re.sub(r'[^\d]+', '', val)

    if not parts[0]:
        parts[0] = '0'

    num = float('.'.join(parts))
    if num % 1 == 0:
        return int(num)
    return num


def on_change(entry, kind='int'):
    if kind == 'int':
        value = integer_number(entry.get())
    else:
        value = float_number(entry.get())

    entry.delete(0, END)
    entry.insert(0, format_currency(value))


# noinspection PyUnusedLocal
def calculate(*args):
    try:
        capital_val = currency_to_num(capital.get())
        percent_val = currency_to_num(percent.get())
        period_val = currency_to_num(period.get())

        percent_val /= 100
        amount = capital_val * (1 + percent_val) ** period_val
        profit_val = amount - capital_val

        invest.set(f'Invest: {format_currency(rounding(capital_val, 2))}')
        profit.set(f'Profit: {format_currency(rounding(profit_val, 2))}')
        income.set(f'Amount: {format_currency(rounding(amount, 2))}')

    except OverflowError:
        invest.set('')
        income.set('')
        profit.set('Buffer Overflow Error!')


def select_all(e):
    # entry select all
    e.widget.select_range(0, END)


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

    percentLbl = Label(main_frame, text='Interest')
    percentLbl.grid(row=1, column=0)

    percent = StringVar()
    percent_entry = Entry(main_frame, textvariable=percent)
    percent_entry.grid(row=1, column=1, padx=5, pady=5)
    percent.trace('w', lambda name, index, mode, entry=percent_entry, kind='float': on_change(entry, kind))

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
    root.bind('<Control-a>', select_all)  # entry select all
    root.mainloop()
