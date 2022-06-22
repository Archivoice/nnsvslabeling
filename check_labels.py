import glob
import os
phones = ['br', 'a', 'ia', 'ua', 'A', 'iA', 'uA', 'ng', 'N', 'e', 'ie', 'E', 'yu', 'i', 'I', 'ih', 'ii', 'U', 'uo', 'er', 'u', 'V', 'yE', 'uE', 'O', 'iO', 'yI', 'iU', 'b', 'c', 'ch', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 'rr', 's', 'sh', 't', 'w', 'x', 'y', 'z', 'zh', 'cl', 'uu', 'vf', 'exh', 'sil', 'pau']

density = {}

for i in phones:
    density[i] = 0

for file in glob.glob('*.lab'):
    with open(file) as f:
        i = f.readline()
        line_count = 1
        while i:
            p = i.strip().split()
            i = f.readline()
            if p[-1] not in phones:
                print(f'In {file}: {p[-1]} is not in the list. At line {line_count}')
            else:
                density[p[-1]] += 1

            if int(p[0]) == int(p[1]):
                print(f'In {file}: {p[-1]} has the same start and end. At line {line_count}')
            line_count += 1

for k, v in density.items():
    if v == 0:
        print(f'No data for {k}')

os.system('pause')
