def recurs(mas1, mas2, sum,f1, f2):
    global N
    if len(mas1) == 1:
        global znach
        if f2<N:
            znach = max(znach, sum + mas2[0])
        else:
            znach = max(znach, sum + mas1[0])
        return
    for i in range(len(mas1)):
        if f1 < N:
            recurs(mas1[:i]+mas1[i+1:],mas2[:i]+mas2[i+1:],sum+mas1[i],f1+1,f2)
        elif f2 < N:
            recurs(mas1[:i]+mas1[i+1:],mas2[:i]+mas2[i+1:],sum+mas2[i], f1, f2 + 1)

sum = 0
mass = []
N=0
mas9 = []
with open('input.txt') as file:
    s = int(file.readline())
    N = s/2
    mass.append(file.readline().split())
    mass.append(file.readline().split())
    for i in range(s):
        mass[0][i] = int(mass[0][i])
        mass[1][i] = int(mass[1][i])
    s = int(file.readline())
    for i in range(s):
        num, type, d = file.readline().split()
        mass[int(type)-1][int(num)-1] += int(d)
        mas9.append([mass[0][:],mass[1][:]])

s = ""
for a in mas9:
    znach = 0
    recurs(a[0],a[1],0,0,0)
    s+=str(znach)+'\n'
with open('output.txt', 'w') as file_w:
    file_w.write(s)
