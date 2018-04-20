start = []
end = []
dur1 = []
names = []
with open('output.txt','w') as file_w:
    with open('input.txt') as file:
        n = int(file.readline())
        for string in range(n):
            s = file.readline()
            if s[len(s)-1:] == '\n':
                s = s[:len(s)-1]
            mas = s.split(' ')
            if mas[0] == 'APPOINT':
                time_start =  int(mas[1])*24*60+int(mas[2].split(':')[0])*60+int(mas[2].split(':')[1])
                time_end = int(mas[1])*24*60+int(mas[2].split(':')[0])*60+int(mas[2].split(':')[1]) + int(mas[3])
                t_name = s[s.rfind(mas[4])+len(mas[4])+1:]

                flag = True
                for i in range(len(start)):
                    if time_start >start[i] and time_start < end[i] or time_end > start[i] and time_end< start[i]:
                        file_w.write('FAIL\n' + t_name +'\n')
                        flag = False
                        break
                if flag == True:
                    start.append(time_start)
                    end.append(time_end)
                    names.append(t_name)
                    dur1.append(int(mas[3]))
                    file_w.write('OK\n')

            if mas[0] == 'PRINT':
                time_start = (int(mas[1])) * 24 * 60
                time_end = (int(mas[1]) + 1) * 24 * 60
                t_name = s[s.rfind(mas[1]) + len(mas[1]) + 1:]
                times_mass= []
                dict_n = {}
                for i in range(len(start)):
                    if names[i].rfind(t_name)!=-1 and time_start < start[i] and time_end > end[i]:

                        times_mass.append(start[i])

                        dict_n.update([(start[i],[end[i],dur1[i],names[i]])])
                times_mass.sort()
                for i in times_mass:
                    m = dict_n[i]
                    hour = str((i % (24 * 60)) // 60)
                    while len(hour)<2:
                        hour = '0'+hour
                    min =  str((i % (24 * 60)) % 60)
                    while len(min)<2:
                        min ='0'+min

                    dur = - i + m[0]
                    nam = m[2]
                    file_w.write(hour+':'+min +' '+str(m[1])+ ' '+ nam+'\n')







