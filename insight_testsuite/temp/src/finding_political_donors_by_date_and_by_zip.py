import sys
import math
from datetime import datetime
import operator
import shutil

def manipulate_files(inf, outf1, outf2):
    """Function that streams in the text files 
    and processes them for analysis"""
    zipcode_dict = {}
    date_dict = {}
    date_list_tbw = []
    with open(inf, 'r') as f:
        for line in f:#read in line by line from input
            relevant_list = []
            median_zip_list = []
            linelist = line.split('|') #initialize structures
            if not linelist[15] and (len(linelist[0]) > 0) and (len(linelist[14]) > 0): #make sure OTHER_ID is empty, that there is a recipient id and a money contribution
                relevant_list.extend([linelist[0], linelist[10], linelist[13], linelist[14]])#create data structure to easily access the only relevant data in the input file 
                if is_zip_valid(relevant_list[1]):#make sure the zipcode is valid
                    zipkey = relevant_list[0]+relevant_list[1][0:5]#create unique identifier for relevant data
                    if zipkey in zipcode_dict:
                        zipcode_dict[zipkey].append(float(relevant_list[3]))
                    else:
                        zipcode_dict[zipkey] = [float(relevant_list[3])] #only add information for zipcode keys that already exist in the dictionary, create new entry if it does not exist
                    median_zip = int(round2(find_median(zipcode_dict[zipkey])))#calculate median thus far for unique identifier and zipcode
                    num_zip = len(zipcode_dict[zipkey])#calculate number of data points
                    sum_zip = int(round2(sum(zipcode_dict[zipkey])))#calculate total sum of data points
                    median_zip_list.extend([relevant_list[0], relevant_list[1][0:5]])
                    median_zip_list.extend([str(median_zip), str(num_zip), str(sum_zip)])#create list for median zipcode data
                    zip_entry = '|'.join(median_zip_list)
                    zip_entry = zip_entry + '\n'
                    with open("results.txt", 'a') as zip_output:
                        zip_output.write(zip_entry)
                if is_date_valid(relevant_list[2]):#validate the date in the input file line
                    datekey = '|'.join([relevant_list[0], relevant_list[2]])#create unique identifier for relevant date data
                    if datekey in date_dict:
                        date_dict[datekey].append(float(relevant_list[3]))
                    else:
                        date_dict[datekey] = [float(relevant_list[3])]#create dictionary for relevant date data, add to existing key library only if it already doesn't exist
        id_date = date_dict.keys()
        id_date_data = list(date_dict.values())#change from dictionary structure back to list structure for easier manipulation
        for idx, val in enumerate(id_date): #for loop to calculate median by date after receiving all the information from the input
            id_date_split = val.split('|')
            id_date_split[1] = datetime.strptime(id_date_split[1], '%m%d%Y')
            median_date = int(round2(find_median(id_date_data[idx])))#compute the median value for the unique recipient and date   
            num_date = len(id_date_data[idx])#calculate the number of data points for the unique recipient and date
            sum_date = int(round2(sum(id_date_data[idx])))
            id_date_split.extend([str(median_date), str(num_date), str(sum_date)])
            date_list_tbw.append(id_date_split)#append information to list structure to be written later
        date_list_tbw = sorted(date_list_tbw, key=operator.itemgetter(0, 1))
        for idx, val in enumerate(date_list_tbw):#created another for loop because the date data needed to be sorted first and then written out to list by looping over its entries
            date_list_tbw[idx][1] = datetime.strftime(date_list_tbw[idx][1], '%m%d%Y')
            date_entry = '|'.join(date_list_tbw[idx])
            date_entry = date_entry + '\n'
            with open("results2.txt", 'a') as date_output:
                date_output.write(date_entry)#write date data to file output
    shutil.move("results.txt", outf1)#Initially, created temporary files then write to actual file
    shutil.move("results2.txt", outf2)

def find_median(lst):
    """This function finds the median of a list of numbers"""
    lst.sort()
    length = len(lst)
    if length % 2 == 0:
        num = int(length/2)
        median = (lst[num-1]+lst[num])/2
    else:
        median = lst[(int(math.ceil(length/2)))-1]
    return median

def round2(num):
    """Rounds a number such that a number at 0.5 or up 
    rounds up and all other numbers round down."""
    if (num % 1) >= 0.5:
        rounded = math.ceil(num)
    else:
        rounded = math.floor(num)
    return rounded

def is_date_valid(string):
    """This function determines if a date is valid."""
    if len(string) == 8:
        if (1 <= int(string[0:2]) <= 12) and (1975 <= int(string[4:8]) <= 2017):
            if (string[0:2] in ['01', '03', '05', '07', '08', '10', '12']) and (1 <= int(string[2:4]) <= 31):
                return datetime.strptime((string), '%m%d%Y') < datetime.today()
            else:
                return False
            if (string[0:2] in ['02']) and (1 <= int(string[2:4]) <= 29):
                return datetime.strptime((string), '%m%d%Y') < datetime.today()
            else:
                return False
            if (string[0:2] in ['04', '06', '09', '11']) and (1 <= int(string[2:4]) <= 31):
                return datetime.strptime((string), '%m%d%Y') < datetime.today()
            else:
                return False
        else:
            return False
    else:
        return False

def is_zip_valid(string):
    """This function determines if a zipcode is valid."""
    return len(string) >= 5

if __name__ == '__main__':
    inFile = sys.argv[1]
    outFile1 = sys.argv[2]
    outFile2 = sys.argv[3]
    manipulate_files(inFile, outFile1, outFile2)

