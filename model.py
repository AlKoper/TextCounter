from pathlib import Path
from docx import Document

# создам функцию, которая открывает FileLinks.txt и берет адрес, где будут хранится исходные файлы
def open_filelinks():
    with open('FileLinks.txt', 'r') as file:
        address = file.readlines()
    return address[1]


# создам функию, которая будет открывать файлы из папки Input files и считать количесвто символов
def text_counter():
    counter_chars = 0    # счетчик для символов всех исходных файлов
    counter_words = 0    # счетчик для слов всех исходных файлов
    for text_file in (Path(open_filelinks()).glob('*.txt')):
        file = open(text_file, 'r', encoding="utf-8")
        counter_text_chars = 0    # счетчик для символов каждого нового текста
        counter_text_words = 0    # счетчик для слов каждого нового текста
        for line in file:
            if line.count(' ') != 0:
                amount_words = line.count(' ') + 1
                counter_text_words = counter_text_words + amount_words
            clear_line = line.translate({ord(i): None for i in "\n,' ',"})    # чистим каждую линию от символов (' ', '\n'), используем метод .translate
            counter_text_chars = counter_text_chars + len(clear_line)    # прибавляем количесвто сиволов каждой строки к счетчику
        counter_words = counter_words + counter_text_words
        counter_chars = counter_chars + counter_text_chars    # прибавлеем количесвто символов в файле к общему счетчику
    # print(f'Общее количество символов нескольких файлов составляет: {counter_chars}, слов: {counter_words}')
    return counter_chars, counter_words


# Создам функцию, которая будет открывать .docx файлы и сохранять их тексты в формате .txt для дальнейшей обработки
def docx_to_txt():
    for text_file in (Path(open_filelinks()).glob('*.docx')):
        doc = Document(text_file)
        text = []
        filename = open_filelinks() + text_file.name[0:-5:1] + '.txt'
        for paragraph in doc.paragraphs:
            text.append(paragraph.text)
        file = '\n'.join(text)
        save_file = open(filename, 'w')
        save_file.write(file)
        save_file.close()



