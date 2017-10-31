# Insight Data Engineering Challenge

# Introduction
As an aspiring data engineer, I am devoloping part of a data pipeline that takes information as data about political donors and from where and when they will make those contributions so we can better assess on what date and in which places is it best to solicit donations. So the program will stream in data and calculate the current median dollar amount of a unique combination of a recipient and the zipcode. Additionally, the program is also meant to compute median data for a unique combination of recipient and date. 

# Prerequisites

In order to evaluate and or work on the challnge, you can download the repository. It is necessary for your computer to be running a Linux or Unix operating system. You schould also have python installed. There are no other dependies needed to complete the challenge. You just need some of the  built-in packages such as math and sys. 


# Detailed explanation of my challenge solution

Using a single read in of the input file, I computed both relevant sets of information. There is one big function that computes both the real-time median data for zipcodes for political donnors and the median data based on date once the streaming has stopped. It may seems counterintuitive to have both actions in a single function, but the date data cannot be computed until the file is done streaming in and, thus, likely after all the median data has been computed.

There are also several helper functions that are called in the bigger function to meet the criterion for the data standards. For example, there are helper functions that test for the validity of both date and zipcode. A data point for zipcode is only considered if it has a valid zipcode and the same goes for a data point for date.

The program starts by reading in a line of the data and then that entry is dissected to provide the relavant information needed for the computations. Then it will compute the median data based on zipcode, in real time. As, the data is streaming in and being computed for median, another data structure within the for loop is accumulating and organizing for another set of computations. 

The zipcode data is written out. Then the program will exit out of the for loop, so that the recipient information and the date can be ordered. Then another for loop is initiated to compute the date data, and finally we come to a final for loop in which the data is written out line by line to a file.

# Tests

There are unittests provided in the `./src` code folder for unittesting the helper functions writtenfor the the script, `finding_political_donors_by_date_and_by_zip.py`.

Additionally, there is a test script in the tests folder that can be run to test data provided by insight. I have provided one other tests that is also in the tests folder and can also be run using the provided `run_tests.sh`. The test that I have a provided tests more rigorously date data 

# Implementation

In order to implement the program, download the repo and run the bash script that sits in the overarching directory of the repo and the program will run, taking an input from the input folder and creating two files in the output folder.

The topmost input folder currently contains an input file that I created from a larger set of data from the FEC. My new file has around a few hundred entries. Finally, the topmost output folder contains the two data files that exist as a result of the processing of the input file. 


