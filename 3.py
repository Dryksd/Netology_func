import pprint
entered = input("Введите p или s или l или a:     ")

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
      
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }
      
def p (num):
    for i in documents:
        if num == i.get('number'):
            return i.get('name')
        else:
          return 'Нет такого номера документа'
        
        
def l ():
    counter = 0
    while counter >= 0:
        for i in documents:
            print(i.get('type'), repr(i.get('number')), repr(i.get('name')))
            counter += 1
        if counter >= len(documents):
            break
    return 'Выведен список всех документов'
        
    
def s (num):
    for i in directories.items():
        for c in i:
            if num in c:
                return i[0]
            
                
def a (**some_dict):
    vb =[str(len(v)+1)]
    vb2 = [list(((v.get('number'))).split())]
    cvb = dict(zip(vb,vb2))
    directories.update(cvb)

    documents.insert(0, v)
    return directories, pprint.pprint(documents)


if entered == 'p':
  p_input = input("Введите номер документа:     ")
  print(p(p_input))

if entered == 'l':
  print(l())
  
if entered == 's':
  s_input = input("Введите номер документа:     ")
  print(s(s_input))
  
if entered == 'a':
  a_input = list((input("Введите значения для type number name через пробел:     ")).split())
  v = dict(type = a_input[0], number = a_input[1], name = a_input[2])
  
  print(a(**v))
  
input()