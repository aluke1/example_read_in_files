import pandas as pd 

#in this program I demonstrate three different ways to read in multiple files with repeating.
#data is stored convieniently in list or dict

directory = 'file_directory/' #location of all the csv files 

file_name_list = ['file1.csv', 'file2.csv', 'file3.csv',\
                    'file4.csv', 'file5.csv', 'file6.csv',\
                    'file7.csv']

#method 1: read in as dictionary 

data_dict = {} #instantiate an empty dictionary 

for file_name in file_name_list: #iterate through the file names
    full_path = directory + file_name #create full path to file
    data_dict[file_name] = pd.read_csv(full_path)
    print('read in: '+full_path+' using list dictionary storage.') 


#now data is stored in a dictionary, where you can access each dataframe using the name of the file 
#as dictionary key: 

print("data frame corresponding to file1.csv (dict structure): ", data_dict['file1.csv'] )


#we can also store the data in a list.  List vs dictionary depends on your preference and how the 
#data will be accessed (lists are better for iteration, dictionaries are better for sending data via JSON)

data_list = [0]*len(file_name_list) #create a list with 0s the same size as file name list 
                                    # Since we know how many files there are, we dont need to use append. 
                                    #  We can store the data in the list using an index


for idx, file_name in enumerate(file_name_list): #iterate over file names, using enumerate so we can use the idx for storing data
    full_path = directory + file_name #create full path to file
    data_list[idx] = pd.read_csv(full_path) #store data in list 
    print('read in: '+full_path+' using list storage.') 

#now data is stored in a list, where you can access each dataframe using the index of the file_name_list to access 
#the corresponding data in the data list: 

print("data frame corresponding to file1.csv (list structure):", data_list[0] )

#in the third method, we dont use the file name list.  We actually don't need to create a list of file names at all if 
#1) files have a consistent naming convention and 2) we know how many files there are:

directory = 'file_directory/' 
num_files = 7 #number of files to read in 
root_file_name = 'file'
file_extenstion = '.csv'
data_list2 = [0]*num_files


for fnum in range(num_files): #create loop to iterate over file numbers (check range function)
    full_path = directory + root_file_name + str(fnum + 1) + file_extenstion #concatenate full path to file 
    data_list2[fnum] = pd.read_csv(full_path)
    print('read in: '+full_path+' using list storage without file name list.') 

#now data is stored in a list, where you can access each dataframe using the index of the file_name_list to access 
#the corresponding data in the data list: 

print("data frame corresponding to file1.csv (list structure, no file name list):", data_list2[0] )