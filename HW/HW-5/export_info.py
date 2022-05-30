def export_info():
    with open('tablet.csv', 'r') as file:
        info = []
        t = []
        for line in file:
            if ',' in line:
                temp = line.strip().split(',')
                info.append(temp)
            elif ';' in line:
                temp = line.strip().split(';')
                info.append(temp)
            elif ':' in line:
                temp = line.strip().split(':')
                info.append(temp)        
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    info.append(t)
                    t= []
    return info