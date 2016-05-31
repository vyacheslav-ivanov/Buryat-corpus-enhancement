import re

def colon(file):
    f = open(file, 'r', encoding='utf-8')
    text = f.read()
    r = re.sub('\n([а-яөүһ]+) ', '\n\\1:', text) #разделили друг от друга слово и значение, чтобы потом можно было их отделить сплитом друг от друга
    f_out = open('Toli_res.txt', 'a', encoding='utf-8')
    f_out.write(r)
    f_out.close()
    f.close()

    
def word_def(file): #вводим слово и значение в словарь
    d = {}
    f = open(file, 'r', encoding='utf-8')
    text = f.read().split('\n')
    for line in text:
        lin = line.split(':')
        for word in range(0, len(lin) - 1):
        
            d[lin[word]] = lin[word + 1]
    f.close()
    return d

colon('Letter_o-ya.txt')
f = open('Toli_res.txt', 'r', encoding='utf-8')
text = f.read()

bur_words = re.findall('\n([а-яүөһ]+:)', text)
diction = word_def('Toli_res.txt') #запускаем функцию, которая выдает словарь

#создаем массивы, в которые складываем слова, для которых определены части речи
verbs = re.findall('[а-яүөһ]+(?:ха|хэ|хо):', str(bur_words)) 
nouns = re.findall('[а-яүөһ]+(?:л?г(?:а|э|о)|уур|лт(?:а|э|о)|ш(?:а|э|о)н?|с(?:а|э|о)|х(?:а|э|о)й|һ(?:а|э|о)н|х?(?:а|э|о)л|б(?:а|э|о)ри|д(?:а|э|о)л|хин|с(?:а|э|о)н|(?:аа|ээ|оо|өө|уу)н|ж(?:а|э|о)н|г(?:а|э|о)н|яал|ьел):', str(bur_words))
adverbs = re.findall('[а-яүөһ]+(?:(?:аа|оо|ээ)р):', str(bur_words))

#ищем слова словаря в массивах, содержащих части речи, если находится, то припимываем перевод и часть речи
f_out = open('Parts_of_speech.txt', 'w', encoding='utf-8')
for word in diction:
    if word + ':' in verbs:
        f_out.write(word + ':' + diction[word] + ':V\n')
    elif word + ':' in nouns:
        f_out.write(word + ':' + diction[word] + ':N\n')
    elif word + ':' in adverbs:
        f_out.write(word + ':' + diction[word] + ':ADV\n')
    else:
        f_out.write(word + ':' + diction[word] + ':A\n')


f.close()
f_out.close()
