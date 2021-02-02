import glob

path = 'c:\\Users\\Christos\\Desktop\\MERGE\\2\\'

files = [f for f in glob.glob(path + "**/*.csv", recursive=True)]

for f in files:
    print(f[34:44])

    fin = open(f, "r")
    data2 = fin.read()
    fin.close()

    fout = open("c:\\Users\\Christos\\Desktop\\MERGE\\1\\"+f[34:40]+" 1M.CSV" , "a")
    fout.write(data2)
    fout.close()
    

