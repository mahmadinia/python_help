fw = open('textfile.txt' ,'r')
for line in fw :
    if '*** trace' not in line:
        txt=line.split('XAx')
        print(txt)
        print (txt[0])
        print (txt[1])

        #if len(txt)>1:
        if 'XAx' in line:

            print  (1)

fw.close()