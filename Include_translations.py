import re
   
def word_def(): #вводим слово и значеине в словарь
    d = {}
    file = open('Toli_res.txt', 'r', encoding='utf-8')
    text = file.read().split('\n')
    for line in text:
        lin = line.split(':')
        for word in range(0, len(lin) - 1):
            d[lin[word]] = lin[word + 1]
    file.close()
    return d


def trans_ru(text): #вставляем строку для перевода в файл с лексемами
    r = re.sub('\n-lexeme\n', '\n trans_ru:\n-lexeme\n', text)
    f_out = open('LEXEME-all.txt', 'w', encoding='utf-8')
    f_out.write(r)
    f_out.close()

      
#f = open('lexemes-all.txt', 'r', encoding='utf-8')
#text = f.read()
#trans_ru(text)
f_2 = open('Parts_of_speech.txt', 'r', encoding='utf-8')
text = f_2.read().split('\n')
lines = [] #создаём массив с строчками из бурятского словаря
for i in text:
    lines.append(i.split(':')) #заполняем этот массив

f_3 = open('LEXEME-all.txt', 'r', encoding='utf-8')
f_out = open('File_with_trans.txt', 'w', encoding='utf-8') #выходной файл с переводами
text_3 = f_3.read()
cells = text_3.split('\n-')
lexemes = []
for i in range(len(lines) - 1): #в массиве со строками словаря
    for u in cells: #ячейка файла с лексемами
        if ('lex: ' + lines[i][0] + '\n') in u: #проверяем, есть ли первое слово строки массива lines в ячейке с лексемами
            lexemes.append(u.replace('trans_ru:', 'trans_ru: ' + lines[i][1] + '\n'))
"""
arr = []
without_trans = set()
for i in range(len(lines) - 1):
    arr.append(lines[i][0])
for word in arr:
    if ' ' + word + '\n' not in str(lexemes) and ' ' + word + '\n' in text_3:
        for i in cells:
            if ' ' + word + '\n' in i:
                without_trans.add(i + '\n-')
lex = lexemes|without_trans

for i in lex:
    f_out.write(i)

for i in range(len(lines) - 1): #в массиве со строками словаря
    for u in cells: #ячейка файла с лексемами
        if (u + ' ' + lines[i][1] + '\n') in lexemes:
            break
        else:
            print(u)
"""


for i in lexemes: #записываем в файл
    f_out.write(i)


#f.close()
f_2.close()
f_3.close()
f_out.close()
