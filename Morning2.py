# set the path
str_path = "C:\\UA\\Files\\Currency\\"

# CSI has USDGBP. The others need inversion.
str_array1 = ['AUDUSD', 'CADUSD', 'CHFUSD', 'CZKUSD', 'USDGBP', 'HUFUSD',  'JPYUSD', 'MXNUSD', 'NZDUSD', 'SEKUSD', 'SGDUSD', 'TRYUSD', 'ZARUSD']
str_array2 = ['QE00000$.csv', 'QE20000$.csv', 'QE}0000$.csv', 'US70000$.csv', 'QF40000$.csv', 'US90000$.csv', 'QE90000$.csv', 'QF50000$.csv', 'QE%0000$.csv', 'QF10000$.csv', 'QE{0000$.csv', 'USD10000$.csv', 'QE_0000$.csv']
str_array3 = ['', '', '', '', '', '', '', '', '', '', '', '', '']


for int_i in range(len(str_array1)):  # for every file

    fin = open(str_path + str_array2[int_i], "r")  # open the file for reading
    strlist_lines = fin.readlines()  # make a string list of the lines
    fin.close()  # close the file

    str_lastline = strlist_lines[-1]  # get the last line from the list of lines
    strlist_lastline = str_lastline.split(',')  # split it
    str_lastclose = strlist_lastline[-1]  # get the last of the splits

    fl_f1 = float(str_lastclose)  # convert it into float
    str_array3[int_i] = fl_f1

    if str_array1[int_i][-3:] == 'USD':  # if it's a "xxxUSD" pair
        fl_f1 = 1 / str_array3[int_i]  # invert it
        fl_f2 = "%.6f" % fl_f1  # show me 6 digits after the point
        #print(str_array1[int_i][-3:] + str_array1[int_i][:3] + '\t' + str(fl_f2))
        print(str(fl_f2))
    else:  # it's a "USDxxx" pair, no inversion needed
        #print(str_array1[int_i] + '\t' + str(str_array3[int_i]))
        print(str(str_array3[int_i]))