# Homework 03 part A PyBank by Dan Boulden (main.py)
# 12/2018

# Create file paths across operating systems
import os
# read CSV module
import csv

# set the path and file for the data
#csvpath = os.path.relpath.join("/Resources", "budget_data.csv")

# Trying without luck to get the relative path to work... jsut hard coded it on line 20
#csvpathR = os.path.realpath("/Resources")
#csvpathR = os.path.abspath("/Resources")
#csvpathR = os.path.relpath("/Resources")
#csvpathR = os.path.realpath("/Resources")

# this woudl use the relative patt... if I coudl get the darn thing to work.
#csvpath = os.path.join(csvpathR, "budget_data.csv")

# my cheat because I could not get the relative path to work (see above)
#csvpath = os.path.join("C:/DAN_BootCamp/Homework_03-Python/03-Python/Homework_03_From_Dan_Boulden/PyBank/Resources","budget_data.csv")

#csvpath = os.path.join('..', 'Resources', 'accounting.csv')

csvpath = os.path.join("Resources", "budget_data.csv")
print(csvpath)
# this is so that I can view the data and be sure it is loading.
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    #csv_header = next(csvreader)
   # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    # for row in csvreader:
    #     print(row)


# now we will use the data...
#create varables
Month_Row_Count = 0
VTotal = 0
VTotal_new = 0
VTotal_before = 0
VTotal_GI1 = 0
VTotal_GI2 = 0
VTotal_GI3 = 0
VTotal_Large = 0
VTotal_small = 0
VTotal_GI1s = 0
VTotal_GI2s = 0
VTotal_GI3s = 0
MONYEAR_I = ""
MONYEAR_D = ""

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(f"Total Months: " + row_count)


    for row in csvreader:
        if row[1] == "Profit/Losses":
            VTotal_new = 0
        else:
            Month_Row_Count = Month_Row_Count + 1
            VTotal_new = row[1]
            VTotal = VTotal + int(VTotal_new)
            if int(VTotal_new) >= int(VTotal_before) and int(VTotal_new) >= VTotal_Large:
                VTotal_GI1 = int(VTotal_new)
                VTotal_GI2 = VTotal_before
                VTotal_Large = int(VTotal_new)
                MONYEAR_I = row[0]
            else:
                VTotal_before = int(VTotal_new)
       


VTotal_before = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


    for row in csvreader:
        if row[1] == "Profit/Losses":
            VTotal_new = 0
        else:
            VTotal_new = row[1]
            VTotal = VTotal + int(VTotal_new)
            if int(VTotal_new) <= int(VTotal_before) and int(VTotal_new) <= VTotal_small:
                VTotal_GI1s = int(VTotal_new)
                VTotal_GI2s = VTotal_before
                VTotal_small = int(VTotal_new)
                MONYEAR_D = row[0]
            else:
                VTotal_before = int(VTotal_new)            


# final calcuations
VAvg = VTotal / Month_Row_Count
VTotal_GI3 = VTotal_GI1 - VTotal_GI2
VTotal_GI3s = VTotal_GI1s - VTotal_GI2s

#Outputs the total months to screen
print(" ")
print(" ")
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: " + str(Month_Row_Count))
print(f"Total: $" + str(VTotal))
print(f"Average Change: $" + str(VAvg))
print(f"Greatest Increase in Profits: " + str(MONYEAR_I) + " ($" + str(VTotal_GI3) + ")")
# print(f"gi1 " + str(VTotal_GI1) + "       GI2 " + str(VTotal_GI2))
# print(f"VTL " + str(VTotal_Large) + "       VTB " + str(VTotal_before))
print(f"Greatest Decrease in Profits: " + str(MONYEAR_D) + " ($" + str(VTotal_GI3s) + ")")
# print(f"gi1 " + str(VTotal_GI1s) + "       GI2 " + str(VTotal_GI2s))
# print(f"VTL " + str(VTotal_small) + "       VTB " + str(VTotal_before))



# csvpath = os.path.join("C:/DAN_BootCamp/Homework_03-Python/03-Python/Homework_03_From_Dan_Boulden/PyBank/Resources","budget_data.csv")

# folder_name = "C:/DAN_BootCamp/Homework_03-Python/03-Python/Homework_03_From_Dan_Boulden/PyBank"

# Create the path for the filename
data_output = os.path.join("C:/DAN_BootCamp/Homework_03-Python/03-Python/Homework_03_From_Dan_Boulden/PyBank", "data.csv")

print(f"folder path " + data_output)

# Write data to a .csv file

with open(data_output, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

# To save specific data input as a row in the csv

    writer.writerow([" "])
    writer.writerow([" "])    
    writer.writerow(["Financial Analysis"])
    writer.writerow(["--------------------------------"])
    writer.writerow([f"Total Months: " + str(Month_Row_Count)])
    writer.writerow([f"Total: $" + str(VTotal)])
    writer.writerow([f"Average Change: $" + str(VAvg)])
    writer.writerow([f"Greatest Increase in Profits: " + str(MONYEAR_I) + " ($" + str(VTotal_GI3) + ")"])
    writer.writerow([f"Greatest Decrease in Profits: " + str(MONYEAR_D) + " ($" + str(VTotal_GI3s) + ")"])
    # writer.writerow
    # writer.writerow
    # writer.writerow
    # writer.writerow
    # writer.writerow
    # writer.writerow