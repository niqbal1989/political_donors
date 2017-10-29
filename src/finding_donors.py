import sys
import math
inFile = sys.argv[1]
outFile1 = sys.argv[2]
#outFile2 = sys.argv[3]
def manipulate_files(inf, outf1):
    #relevant_list=[]
    """This is the function that will stream in the text files with the political donor information """
    zipcode_dict = {}
    date_dict = {}
    with open(inf,'r') as f:
        for line in f:
            relevant_list=[]
            median_zip_list=[]
            linelist=line.split('|')
            if not linelist[15]:
                relevant_list.extend([linelist[0],linelist[10],linelist[13],linelist[14]])
                zipkey = relevant_list[0]+relevant_list[1][0:5]
                if zipkey in zipcode_dict:
                    zipcode_dict[zipkey].append(float(relevant_list[3]))
                else:
                    zipcode_dict[zipkey] = [float(relevant_list[3])]
                median_zip = round2(find_median(zipcode_dict[zipkey]))
                sum_zip = round2(sum(zipcode_dict[zipkey]))
                num_zip = len(zipcode_dict[zipkey])
                median_zip_list.extend([relevant_list[0],relevant_list[1],str(median_zip),str(num_zip),str(sum_zip)])
                datekey = relevant_list[0]+relevant_list[2]
                median_entry = '|'.join(median_zip_list)
                median_entry = median_entry + '\n'
                print(median_entry)
                with open(outf1,'a') as o:
                    o.write(median_entry)

def find_median(lst):
    lst.sort()
    length = len(lst)
    if length % 2 == 0:
        num = length/2
        median = (lst[num-1]+lst[num])/2
    else:
        median=lst[int(math.ceil(length/2))]
    return median

def round2(num):
    if (num % 1) >= 0.5:
        rounded = math.ceil(num)
    else:
        rounded = math.floor(num)
    return(rounded)
manipulate_files(inFile, outFile1)

