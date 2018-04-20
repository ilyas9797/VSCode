sum = 0
mass = []
with open('input.txt') as file:
    s = int(file.readline())
    while s>0:
        a, b = file.readline().split(' ')
        a, b = int(a), int(b)
        sum += a*b
        mass.append(a*b)
        s -= 1
with open('output.txt','w') as file_w:
    for i in mass:
        f = i/sum
        file_w.write(str(f)+'\n')
