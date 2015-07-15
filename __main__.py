import os
path = os.path.dirname(__file__) + '/'

from tkinter import *
from tkinter.ttk import *

def calculate():
	cap = capital.get()
	pct = percent.get()
	per = period.get()

	try:
		cap = float(cap)
		pct = float(pct)
		per = int(per)

		if per < 0 or pct < 0:
			profit.set('Input error!')
			return

		pro = 0
		inc = cap
		pct /= 100

		for i in range(per):
			pro += inc * pct
			inc += (inc * pct)

		invest.set('Capital: {}'.format(cap))
		profit.set('Profit: {}'.format(pro))
		income.set('Income: {}'.format(inc))
		
	except:
		invest.set('')
		income.set('')
		profit.set('Input error!')

if __name__ == '__main__':
	root = Tk()
	root.title("An's revenue calculator v1.0")
	img = PhotoImage(file = path + 'icon.gif')
	root.tk.call('wm', 'iconphoto', root._w, img)
	root.minsize(150, 150)
	root.resizable(False, False)

	style = Style()
	themes = style.theme_names()

	if 'xpnative' in themes:
		style.theme_use('xpnative')
	elif 'aqua' in themes:
		style.theme_use('aqua')
	elif 'alt' in themes:
		style.theme_use('alt')
	else:
		style.theme_use('default')

	mf = Frame(root, padding = 10)
	mf.grid(column = 0, row = 10, sticky = 'wnes')

	capitalLbl = Label(mf, text = 'Capital')
	capitalLbl.grid(row = 0, column = 0)

	capital = StringVar()
	capEn = Entry(mf, textvariable = capital)
	capEn.grid(row = 0, column = 1, padx = 5, pady = 5)

	invest = StringVar()
	investLbl = Label(mf, textvariable = invest)
	investLbl.grid(row = 0, column = 2)

	percentLbl = Label(mf, text = 'Percent')
	percentLbl.grid(row = 1, column = 0)

	percent = StringVar()
	perEn = Entry(mf, textvariable = percent)
	perEn.grid(row = 1, column = 1, padx = 5, pady = 5)

	profit = StringVar()
	proLbl = Label(mf, textvariable = profit)
	proLbl.grid(row = 1, column = 2)

	periodLbl = Label(mf, text = 'Period number')
	periodLbl.grid(row = 3, column = 0)

	period = StringVar()
	periodEn = Entry(mf, textvariable = period)
	periodEn.grid(row = 3, column = 1, padx = 5, pady = 5)

	income = StringVar()
	incomeLbl = Label(mf, textvariable = income)
	incomeLbl.grid(row = 3, column = 2)

	calBtn = Button(mf, text = 'Calculate', command = calculate)
	calBtn.grid(row = 4, column = 1, pady = 5)

	capEn.focus()
	root.bind('<Return>', calculate)
	root.mainloop()
