name = 'Artem'
last_name = "Svarych"

# doc string
def some_func():
    ...:'''texttexttext
    jhjdsb
    dnvjkxdhvjkxdvbjxhvbjhxvbkjdv
    vjbfhvbkdd
    fdvgnbjfjvndf,'''
    pass
string = 'Some text'
string + string
print(string)
string * 5
len(string)
# str - змінна рядка (рядок)
string[2:5] # 2,3,4 - символи будуть обрані
string = 'some words'
string.upper() # всі літери великі
string2.lower() # всі літери малі
string.capitalize() # перша літера велика
len(string.split(''))
string.replace('O', str(0)) #заміна символів з одного на інший


text = "Тут якийсь чудовий текст" # Заміна літери об'єднання та змінити літеру
txt1 = text.split('')
txt1

for word in txt1:
    ...:    if word in txt1:
        word = word.capitalize()
words_for_format = 'First Name: {}, '

'{}{}{}'.format('1', '2', '3')
'{one}{two}{three}'.format(three = '3!',one = '1!')
f' {one}{two}{three}
