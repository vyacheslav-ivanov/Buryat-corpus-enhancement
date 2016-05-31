import re
file = open('БРС_О-Я.txt', 'r', encoding='utf-8')
text = file.read()
text = re.sub('\(.+?\n?\)', '', text)
#регулярное выражение для извлечения лексем из первого тома словаря:
#word_translation = re.findall('\n([а-яүөh]+(?: атр\.)?(?: [1-9]\.|I{,3})?(?: [1-9]\.)?(?: [1-9]\))? .+(?:;|\.))', text)

#регулярное выражение извлечения лексем из второго тома словаря:
word_translation = re.findall('\n([а-яүөhё]+ .+?;)', text)

#регулярное выражение, извлекающее все слова на нужную букву из первого тома словаря
#trans_select = re.findall('\nа.* ?', '\n'.join(word_translation))

file_out = open('Letter_o-ya.txt', 'w', encoding='utf-8')
file_out.write('\n'.join(word_translation))
file_out.close()
file.close()

