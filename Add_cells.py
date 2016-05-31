f = open('File_with_trans.txt', 'r', encoding='utf-8')
f_2 = open('New_lexemes.txt', 'r', encoding='utf-8')
f_out = open('Added_lex.txt', 'w', encoding='utf-8')
text = f.read()
text_2 = f_2.read()
cells_2 = text_2.split('\n-')

f_3 = open('Parts_of_speech.txt', 'r', encoding='utf-8')
txt = f_3.read().split('\n')
lines = [] #создаём массив с строчками из бурятского словаря
for i in txt:
    lines.append(i.split(':'))
arr_lex = []
for i in range(len(lines) - 1):
    arr_lex.append(lines[i][0])

for word in arr_lex:
    if ' ' + word + '\n' not in text and ' ' + word + '\n' in text_2:
        for i in cells_2:
            if ' ' + word + '\n' in i:
                f_out.write(i + '\n-')
            
f.close()
f_2.close()
f_3.close()
f_out.close()
