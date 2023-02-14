from pathlib import Path
import

# создам функцию, которая открывает FileLinks.txt и берет адрес, где будут хранится исходные файлы
def open_filelinks():
    with open('FileLinks.txt', 'r') as file:
        address = file.readlines()
    return address[1]


# создам функию, которая будет открывать файлы из папки Input files и считать количесвто символов
def text_counter():
    counter_files = 0    # счетчик для символов всех исходных файлов
    for text_file in (Path(open_filelinks()).glob('*.txt')):
        file = open(text_file, 'r', encoding="utf-8")
        counter_text = 0    # счетчик для символов каждого нового текста
        for line in file:
            clear_line = line.translate({ord(i): None for i in "\n,' ',"})    # чистим каждую линию от символов (' ', '\n'), используем метод .translate
            counter_text = counter_text + len(clear_line)    # прибавляем количесвто сиволов каждой строки к счетчику
        counter_files = counter_files + counter_text    # прибавлеем количесвто символов в файле к общему счетчику
    print(f'Общее количесвто символов нескольких файлов составляет: {counter_files}')


if __name__ == '__main__':
    text_counter()


