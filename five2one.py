import pandas
import os

def function1(str_path1, s1):
    
    # read csv file
    csv_data = pandas.read_csv(str_path1+s1, dtype=str)
    
    print("point1")
    
    #READ COLUMNS as series
    c0 = csv_data['DATE']
    c1 = csv_data['TIME']
    c2 = csv_data['OPEN']
    c3 = csv_data['HIGH']
    c4 = csv_data['LOW']
    c5 = csv_data['CLOSE']
    
    print("point2")
    
    for index, val in enumerate(c0):
        if ((len(c1[index]) == 4 and (c1[index][3] == '4' or c1[index][3] == '9'))
        or (len(c1[index]) == 3 and (c1[index][2] == '4' or c1[index][2] == '9'))
        or (len(c1[index]) == 2 and (c1[index][1] == '4' or c1[index][1] == '9'))
        or (len(c1[index]) == 1 and (c1[index][0] == '4' or c1[index][0] == '9'))):
            
            hh = -9999
            ll = +9999
            
            for index2 in range(index-4, index+1, 1):
               
                #do stuff here
                if index2 == index-4:
                    date = c0[index2]
                    time = c1[index2]
                    o = float(c2[index2])
    
    
                if float(c3[index2]) > hh:
                    hh = float(c3[index2])
                
                if float(c4[index2]) < ll:
                    ll = float(c4[index2])
    
                if index2 == index:
                    c = float(c5[index2])
            
            line = date + "," + time + "," + str(o) + "," + str(hh) + "," + str(ll) + "," + str(c)
            print (line, file = f)
            
            
# set the paths for input and output files
str_path1 = "_input/"
str_path2 = "_output/"

# list the input files
strlist_inputfiles = os.listdir(str_path1)        

for s1 in strlist_inputfiles: 
    
    print("-------------------")
    print("OPENING FILE: " + str_path1 + s1)
    
    f = open(str_path2+s1[:6]+' 5M.csv', "w")
    print("DATE,TIME,OPEN,HIGH,LOW,CLOSE", file = f)
    function1(str_path1, s1)
    f.close()
    
    print("CREATED FILE: " + str_path2+s1[:6]+' 5M.csv')
    print("-------------------") 
                          
     
          
    
    
    
    
                                            
    
    