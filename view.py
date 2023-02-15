from tkinter import *
from tkinter.ttk import Combobox
import model

#Функция для центрирования trkinter окна
def center(win):
    """
    centers of tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


# Создадим обработчик для кнопки button_start:
def button_start_handler(event):
    amount_chars, amount_words = model.text_counter()   # вызовим функцию расчета ко-ва слов и символов
    entry_chars.delete(0, END)    # зачистим поле с ко-вом символов
    entry_chars.insert(0, amount_chars)    # вставим в поле ко-во символов
    entry_words.delete(0, END)    # зачистим поле с ко-вом слов
    entry_words.insert(0, amount_words)    # вставим в поле ко-во слов
    order_price = float(combo_price.get())    # возбмем цену заказа из соотвествующего окна
    order_cost = order_price * (amount_chars/1000)    # рассчитаем стоимость заказа из вводных данных
    text_counter.delete(1.0, END)    # зачистим текстовое поле
    conclusion = 'Объем всего материала составляет '+str(amount_words)+' слов, или '+str(amount_chars)+' з.б.п. Отсюду получаем стоимость заказа:'+'\n'+'$'+str(order_price)+' * '+str(amount_chars/1000)+' = $'+str(round(order_cost, 2))
    text_counter.insert(1.0, conclusion)    # вставим ответ в текстовое поле со всеми данными


# Создадим функцию для создания главного окна программы
def main_window():
    global entry_chars, entry_words, combo_price, text_counter
    # Создадим главное окно программы
    root = Tk()
    root.geometry('400x340')
    root.title('Text Counter')
    root.config(bg='light blue')
    center(root)
    # Создам виджеты для размещения в окне (подписи, текстовое поле, выпадающие меню и кнопку)
    label_format = Label(root, text='Формат:', font='Calibri 15', background='light blue', width=10)
    label_price = Label(root, text='Цена:', font='Calibri 15', background='light blue', width=10)
    combo_format = Combobox(root)
    combo_price = Combobox(root)
    combo_format_values = ['docx', 'txt']
    combo_price_values = ['3.5', '2.5']
    combo_format['values'] = combo_format_values
    combo_price['values'] = combo_price_values
    combo_format.current(0)
    combo_price.current(0)
    label_amount = Label(root, text='Количество', font='Calibri 17', background='light blue', width=20)
    label_words = Label(root, text='Слова:', font='Calibri 15', background='light blue', width=10)
    label_chars = Label(root, text='Символы:', font='Calibri 15', background='light blue', width=10)
    entry_words = Entry(root, width=10)
    entry_chars = Entry(root, width=10)
    text_counter = Text(root, width=34, height=4)
    button_start = Button(root, text='Поехали', width=30)
    #размещу виджеты в окне
    label_format.grid(row=0, column=0)
    combo_format.grid(row=0, column=1)
    label_price.grid(row=1, column=0)
    combo_price.grid(row=1, column=1)
    label_amount.grid(row=2, columnspan=2)
    label_words.grid(row=3, column=0)
    entry_words.grid(row=3, column=1)
    label_chars.grid(row=4, column=0)
    entry_chars.grid(row=4, column=1)
    text_counter.grid(row=5, columnspan=2)
    button_start.grid(row=6, columnspan=2, pady=10, padx=0)
    # привяжу обработчик к кнопке button_start
    button_start.bind('<Button-1>', button_start_handler)


if __name__ == '__main__':
    main_window()
    mainloop()