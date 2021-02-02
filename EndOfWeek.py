import os
from shutil import copyfile

# set the path
str_path = "C:\\UA\\Files\\Currency\\1M\\"
str_path2 = "C:\\UA\\Files\\Currency\\1M BACKUP\\"
str_path3 = "C:\\Users\\Christos\\Dropbox\\1_AUTOMATED TRADING\\8_FOREX\\_TRADES\\W42\\_data\\"
str_path4 = "C:\\UA\\Files\\Currency\\MERGED\\"

strlist_files = os.listdir(str_path)  # list the files



print("# create backup")
for int_i in strlist_files:

    copyfile(str_path+int_i, str_path2+int_i)
    print(str_path+int_i + " backup-ed to: " + str_path2+int_i)

for int_i in strlist_files:

    # read new week data from dropbox/_data folder
    fin = open(str_path3 + int_i[:6].lower() + ".csv", "r")
    data = fin.read()
    fin.close()

    # open original, append data
    fout = open(str_path + int_i, "a")
    #fout.write(data)  # DISABLE PROTECTION
    fout.close()

    print(str_path3 + int_i[:6].lower() + ".csv APPENDED TO: " + str_path + int_i)


for int_i in strlist_files:

    # read new week data from dropbox/_data folder
    fin = open(str_path3 + int_i[:6].lower() + ".csv", "r")
    data = fin.read()
    fin.close()

    # open original, append data
    fout = open(str_path4 + int_i, "a")
    #fout.write(data)  # DISABLE PROTECTION
    fout.close()

    print(str_path3 + int_i[:6].lower() + ".csv APPENDED TO: " + str_path4 + int_i)