f_2 = open('Parts_of_speech.txt', 'r', encoding='utf-8')
file = open('New_lexemes.txt', 'w', encoding='utf-8')
text = f_2.read().split('\n')
cons = 'рнгдблмс'
front = 'үөэ'
back = 'ыаоу'
lines = [] #создаём массив с строчками из бурятского словаря
for i in text:
    lines.append(i) #заполняем этот массив
arr_lex = []

for line in lines:
    if 'N' in line:
        a = line.split(':')
        if a[0][-1:] == 'а':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0] + '.' + '|' \
                  + a[0][:-1] + '.' + '\n' + ' paradigm: ' + \
                  'N-back-case' + '\n' + ' trans_ru: ' + a[1] + '\n')
            
        elif a[0][-1:] == 'э':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0] + '.' + '|' \
                  + a[0][:-1] + '.' + '\n' + ' paradigm: ' + \
                  'N-front-case' + '\n' + ' trans_ru: ' + a[1] + '\n')
   
        elif (a[0][-1:] in cons):
            if a[0][1:2] in back or a[0][:1] in back:
               arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n'  + ' stem: ' + a[0] + '.'\
                      + '\n' + ' paradigm: ' + \
                      'N-back-velar-cons-case' + '\n' + ' trans_ru: ' + a[1] + '\n')
                
            else:
                arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0] + '.'\
                      + '\n' + ' paradigm: ' + \
                      'N-front-velar-cons-case' + '\n' + ' trans_ru: ' + a[1] + '\n')
                
        elif a[0][-1:] == 'о':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0] + '.' + '|' \
                  + a[0][:-1] + '.' + '\n' + ' paradigm: ' + \
                  'N-back-lab-case' + '\n' + ' trans_ru: ' + a[1] + '\n')
        
        elif a[0][-1:] == 'ё':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0] + '.' + '|' \
                  + a[0][:-1] + '.' + '\n' + ' paradigm: ' + \
                  'N-back-lab-case' + '\n' + ' trans_ru: ' + a[1] + '\n')
            
        elif a[0][-1:] == 'и':
            if a[0][1:2] in back or a[0][:1] in back:
                arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0] + '.'\
                      + '\n' + ' paradigm: ' + \
                      'N-back-i-short-case' + '\n' + ' trans_ru: ' + a[1] + '\n')
            else:
                arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0] + '.'\
                      + '\n' + ' paradigm: ' + \
                      'N-front-i-short-case' + '\n' + ' trans_ru: ' + a[1] + '\n')
                
        elif a[0][-2:] == 'ии':
            if a[0][1:2] in front or a[0][:1] in front:
                arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0] + '.'\
                  + '\n' + ' paradigm: ' + \
                  'N-front-i-long-case' + '\n' + ' trans_ru: ' + a[1] + '\n')
            else:
                arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0] + '.'\
                  + '\n' + ' paradigm: ' + \
                  'N-back-i-long-case' + '\n' + ' trans_ru: ' + a[1] + '\n')
                
        elif a[0][-2:] == 'эй' or a[0][-2:] == 'үй' or a[0][-2:] == 'ей':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0] + '.'\
                  + '\n' + ' paradigm: ' + \
                  'N-front-y-case' + '\n' + ' trans_ru: ' + a[1] + '\n')
            
        elif a[0][-2:] == 'ай' or a[0][-2:] == 'ы':
            if a[0][1:2] in front or a[0][:1] in back:
                arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0] + '.'\
                  + '\n' + ' paradigm: ' + \
                  'N-back-y-case' + '\n' + ' trans_ru: ' + a[1] + '\n')
                
        elif a[0][-2:] == 'ой':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0] + '.'\
                  + '\n' + ' paradigm: ' + \
                  'N-back-oj-case' + '\n' + ' trans_ru: ' + a[1] + '\n')
            
        elif a[0][-2:] == 'үү' or a[0][-2:] == 'өө' or a[0][-2:] == 'ээ' or a[0][-2:] == 'еэ':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0] + '.'\
                  + '\n' + ' paradigm: ' + \
                  'N-front-long-case' + '\n' + ' trans_ru: ' + a[1] + '\n')
            
        elif a[0][-2:] == 'юу' or a[0][-2:] == 'яа' or a[0][-2:] == 'ёо' or a[0][-2:] == 'оо' or a[0][-2:] == 'аа':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0] + '.'\
                  + '\n' + ' paradigm: ' + \
                  'N-back-long-case' + '\n' + ' trans_ru: ' + a[1] + '\n')
            
        elif a[0][-2:] == 'уу':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0] + '.'\
                  + '\n' + ' paradigm: ' + \
                  'N-back-long-lab-case' + '\n' + ' trans_ru: ' + a[1] + '\n')
            
        elif a[0][-1:] in cons:
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0] + '.'\
                  + '\n' + ' paradigm: ' + \
                  'N-back-velar-cons-case' + '\n' + ' trans_ru: ' + a[1] + '\n')
            
        elif a[0][-1:] == 'ь':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0] + '.'\
                  + '\n' + ' paradigm: ' + \
                  'N-back-palat-cons-case' + '\n' + ' trans_ru: ' + a[1] + '\n')
            
        elif a[0][-1:] == 'ь' and 'о' in a[0][1:2]:
             arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0] + '.'\
                  + '\n' + ' paradigm: ' + \
                  'N-back-lab-palat-cons-case' + '\n' + ' trans_ru: ' + a[1] + '\n')
        else:
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0] + '.'\
                  + '\n' + ' paradigm: ' + \
                  'N-unstable_n-all-case' + '\n' + ' trans_ru: ' + a[1] + '\n')



    elif ':V' in line:
        a = line.split(':')
        if a[0][-3:] == 'лха' or a[0][-3:] == 'рха':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' + '//' +\
                  a[0][:-2] + 'a.' + '|' + a[0][:-2] + '.' + '\n' + \
                  ' paradigm: ' + 'short-back' + '\n' + ' trans_ru: ' + a[1] + '\n')
            
        elif a[0][-4:] == 'ииха' or a[0][-4:] == 'ааха' or a[0][-4:] == 'айха':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' +\
                  '\n' + \
                  ' paradigm: ' + 'long-back' + '\n' + ' trans_ru: ' + a[1] + '\n')
            
        elif a[0][-4:] == 'ойхо' or a[0][-4:] == 'оохо' or a[0][-3:] == 'ыхо' or a[0][-4:] == 'иихо':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' +\
                  '\n' + \
                  ' paradigm: ' + 'long-back-lab' + '\n' + ' trans_ru: ' + a[1] + '\n')
            
        elif a[0][-4:] == 'иихэ' or a[0][-4:] == 'ээхэ' or a[0][-4:] == 'еэхэ':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' +\
                  '\n' + \
                  ' paradigm: ' + 'long-front' + '\n' + ' trans_ru: ' + a[1] + '\n')
        elif a[0][-3:] == 'аха':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' +\
                  '|' + a[0][:-3] + '.' + '\n' + \
                  ' paradigm: ' + 'short-back' + '\n' + ' trans_ru: ' + a[1] + '\n')
            
        elif a[0][-3:] == 'лхо' or a[0][-3:] == 'рхо':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' + '//' +\
                  a[0][:-2] + 'о.' + '|' + a[0][:-2] + '.' + '\n' + \
                  ' paradigm: ' + 'short-back-lab' + '\n' + ' trans_ru: ' + a[1] + '\n')
            
        elif a[0][-3:] == 'охо':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' +\
                  '|' + a[0][:-3] + '.' + '\n' + \
                  ' paradigm: ' + 'short-back-lab' + '\n' + ' trans_ru: ' + a[1] + '\n')
            
        elif a[0][-3:] == 'лхэ' or a[0][-3:] == 'рхэ':
            if 'э' in a[0][1:2] or a[0][:1] == 'э':
                arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' + '//' +\
                  a[0][:-2] + 'э.' + '|' + a[0][:-2] + '.' + '\n' + \
                  ' paradigm: ' + 'short-front' + '\n' + ' trans_ru: ' + a[1] + '\n')
            else:
                arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' + '//' +\
                  a[0][:-2] + 'э.' + '|' + a[0][:-2] + '.' + '\n' + \
                  ' paradigm: ' + 'short-front-lab' + '\n' + ' trans_ru: ' + a[1] + '\n')
            
        elif a[0][-3:] == 'эхэ':
            if 'э' in a[0][1:2] or a[0][:1] == 'э':
                arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' +\
                  '|' + a[0][:-3] + '.' + '\n' + \
                  ' paradigm: ' + 'short-front' + '\n' + ' trans_ru: ' + a[1] + '\n')
            else:
                arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' +\
                  '|' + a[0][:-3] + '.' + '\n' + \
                  ' paradigm: ' + 'short-front-lab' + '\n' + ' trans_ru: ' + a[1] + '\n')
        elif a[0][-3:] == 'иха':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' +\
                  '|' + a[0][:-3] + '.' + '\n' + \
                  ' paradigm: ' + 'i-palat-back' + '\n' + ' trans_ru: ' + a[1] + '\n')
        elif a[0][-3:] == 'ихо':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' +\
                  '|' + a[0][:-3] + '.' + '\n' + \
                  ' paradigm: ' + 'i-palat-back-lab' + '\n' + ' trans_ru: ' + a[1] + '\n')
            
        elif a[0][-3:] == 'ихэ':
            if 'ө' in a[0][1:2] or a[0][:1] == 'ү':
                arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' +\
                  '|' + a[0][:-3] + '.' + '\n' + \
                  ' paradigm: ' + 'i-palat-front-lab' + '\n' + ' trans_ru: ' + a[1] + '\n')
            else:
                arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' +\
                  '|' + a[0][:-3] + '.' + '\n' + \
                  ' paradigm: ' + 'i-palat-front' + '\n' + ' trans_ru: ' + a[1] + '\n')
                
        elif a[0][-3:] == 'яха':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' +\
                  '|' + a[0][:-3] + '.' + '\n' + \
                  ' paradigm: ' + 'j-back' + '\n' + ' trans_ru: ' + a[1] + '\n')
        
        elif a[0][-3:] == 'ёхо':
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' +\
                  '|' + a[0][:-3] + '.' + '\n' + \
                  ' paradigm: ' + 'j-back-lab' + '\n' + ' trans_ru: ' + a[1] + '\n')
        elif a[0][-3:] == 'ехэ':
            if 'ю' in a[0][1:2] or a[0][:1] == 'ү':
                arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' +\
                  '|' + a[0][:-3] + '.' + '\n' + \
                  ' paradigm: ' + 'j-front-lab' + '\n' + ' trans_ru: ' + a[1] + '\n')
            else:
                arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' +\
                  '|' + a[0][:-3] + '.' + '\n' + \
                  ' paradigm: ' + 'j-front' + '\n' + ' trans_ru: ' + a[1] + '\n')
        
        else:
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0]+ '\n' + ' gramm: ' + a[2] + '\n' + ' stem: ' + a[0][:-2] + '.' +\
                  '\n' + \
                  ' paradigm: ' + 'long-front-lab' + '\n' + ' trans_ru: ' + a[1] + '\n')
            

    else:
        a = line.split(':')
        if len(a) == 3:
            arr_lex.append('-lexeme\n' + ' lex: ' + a[0] + '\n' + ' stem: ' + a[0] + \
              '\n' + ' gramm: ' + a[2] + '\n' + ' paradigm: ' + 'unchangeable' + '\n' + ' trans_ru: ' + a[1] + '\n')
        else:
            break

for i in arr_lex:
    file.write(i)
    
f_2.close()
file.close()
