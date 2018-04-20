with open('input.txt') as file:
    n = int(file.readline())
    s = file.readline()
    if s[len(s)-1:] == '\n':
        s = s[:len(s)-1]

mas = s.split(' ')


quantity = len(mas[0])
#перебираем со второго слова до последнего

for i in range(len(mas)-1):
    #если слово ни разу не встречалось
    flag = False
    for j in range(i+1):
        if mas[i+1] == mas[j]:
            flag = True
            break
    #то его надо вводить полностью
    if flag == False:
        quantity += len(mas[i+1])
        continue

    #если слово встречалось
    new_mas = []
    new_mas.extend(mas[:i+1])
    for j in range(len(mas[i+1])):
        k1 = 0
        for k in range(len(new_mas)):
            if new_mas[k1][:j+1] != mas[i+1][:j+1]:
                del new_mas[k1]
                k1 -= 1
            k1 += 1
        if len(new_mas) == 1:
            quantity +=  j + 1
            mas[i] =' '
            break
with open('output.txt','w') as file_w:
    file_w.write(str(quantity))





