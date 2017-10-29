import sys
inFile = sys.argv[1]
outFile1 = sys.argv[2]
#outFile2 = sys.argv[3]
def manipulate_files(inFile):
    """This is the function that will stream in the text files with the political donor information and """
    counter = 0
    with open(inFile) as f:
        for line in f:
            counter = counter + length(line)

    with open(outFile1) as o:
        o.write(counter)
