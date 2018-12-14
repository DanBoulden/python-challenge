# Homework 03 part B PyPoll by Dan Boulden (main.py)
# 12/2018

# Create file paths across operating systems
import os
# read CSV module
import csv

# set the path and file for the data
#csvpath = os.path.relpath.join("/Resources", "election_data.csv")

# this woudl use the relative patt... if I coudl get the darn thing to work.
#csvpath = os.path.join(csvpathR, "budget_data.csv")

# my cheat because I could not get the relative path to work (see above)
#csvpath = os.path.join("C:/DAN_BootCamp/Homework_03-Python/03-Python/Homework_03_From_Dan_Boulden/PyPoll/Resources","election_data.csv")

csvpath = os.path.join("Resources", "election_data.csv")
print(csvpath)

# this is so that I can view the data and be sure it is loading.
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    # for row in csvreader:
    #     print(row)


# now we will use the data...
#create varables
Vote_Count = 0
Khan_Count = 0
Khan_Par = 0
Correy_Count = 0
Correy_Par = 0
Li_Count = 0
Li_Par = 0
OTooley_Count = 0
OTooley_Par = 0
Other_Count = 0
Other_Par = 0
# VTotal = 0
# VTotal_new = 0
# VTotal_before = 0
# VTotal_GI1 = 0
# VTotal_GI2 = 0
# VTotal_GI3 = 0
# VTotal_Large = 0
# VTotal_small = 0
# VTotal_GI1s = 0
# VTotal_GI2s = 0
# VTotal_GI3s = 0
# MONYEAR_I = ""
# MONYEAR_D = ""

with open(csvpath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')

#     #print(f"Total Months: " + row_count)

# Voter ID,County,Candidate


     for row in csvreader:
         if row[1] == "County":
             VTotal_new = 0
         else:
             Vote_Count = Vote_Count + 1
             if row[2] == "Khan":
                 Khan_Count = Khan_Count + 1
             else:
                 Khan_Count = Khan_Count
             if row[2] == "Correy":
                 Correy_Count = Correy_Count + 1
             else:
                 Correy_Count = Correy_Count
             if row[2] == "Li":
                 Li_Count = Li_Count + 1
             else:
                 Li_Count = Li_Count
             if row[2] == "O'Tooley":
                 OTooley_Count = OTooley_Count + 1
             else:
                 OTooley_Count = OTooley_Count
             if row[2] != "O'Tooley" and row[2] != "Li" and row[2] != "Correy" and row[2] != "Khan":
                 Other_Count = Other_Count + 1
             else:
                 Other_Count = Other_Count



#             VTotal_new = row[1]
#             VTotal = VTotal + int(VTotal_new)
#             if int(VTotal_new) >= int(VTotal_before) and int(VTotal_new) >= VTotal_Large:
#                 VTotal_GI1 = int(VTotal_new)
#                 VTotal_GI2 = VTotal_before
#                 VTotal_Large = int(VTotal_new)
#                 MONYEAR_I = row[0]
#             else:
#                 VTotal_before = int(VTotal_new)

Khan_Par = Khan_Count / Vote_Count
Correy_Par = Correy_Count / Vote_Count
Li_Par = Li_Count / Vote_Count
OTooley_Par = OTooley_Count / Vote_Count
Other_Par = Other_Count / Vote_Count       

print (f"Khan: " + "{:.3%}".format(Khan_Par) + " (" + str(Khan_Count) + ")")
print (f"Correy_Count " + str(Correy_Count))
print (f"Li_Count " + str(Li_Count))
print (f"O'Tooley_Count " + str(OTooley_Count))
print (f"Other_Count " + str(Other_Count))



print(f"Khan Percentage Test :" + "{:.3%}".format(Khan_Par) + "%")
print(f"Correy Percentage Test :" + "{:.3%}".format(Correy_Par) + "%")
print(f"Li Percentage Test :" + "{:.3%}".format(Li_Par) + "%")
print(f"O'Tooley Percentage Test :" + "{:.3%}".format(OTooley_Par) + "%")
print(f"Other Percentage Test :" + "{:.3%}".format(Other_Par) + "%")



#list1, list2 = ["Khan", "Corry", "Li", "O'Tooley", "Other"], [Khan_Count, Correy_Count, Li_Count, OTooley_Count, Other_Count]
#print "Max value element : ", max(list1)
#print ("Max value element : " + max(str(list2)))
#print("avg: " + str(average([Khan_Count, Correy_Count, Li_Count])))

Winner = max(Khan_Count, Correy_Count, Li_Count, OTooley_Count, Other_Count)
print("The Winner is: " + str(Winner))

#winner_var = 0

#myList = ["Khan", Khan_Count, "Corry", Correy_Count, "Li", Li_Count, "O'Tooley", OTooley_Count, "Other", Other_Count]
#index()

#print(myList)

myList2 = {"Khan": Khan_Count, "Corry": Correy_Count, "Li": Li_Count, "O'Tooley": OTooley_Count, "Other": Other_Count}

#print(myList2)

#myList2[max(myList2, key=myList2.get)]

#Working max
max_key = max(myList2, key=lambda k: myList2[k])
#print(max_key + " is the winner with " + str(Winner) + " votes.")


#winner_var = max(myList)
#print(winner_var)



# #Outputs the total months to screen
print(" ")
print(" ")
print("Election Results")
print(" -------------------------")
print(f"Total Votes: " + str(Vote_Count))
print(" -------------------------")
print (f"Khan: " + "{:.3%}".format(Khan_Par) + " (" + str(Khan_Count) + ")")
print (f"Correy: " + "{:.3%}".format(Correy_Par) + " (" + str(Correy_Count) + ")")
print (f"Li: " + "{:.3%}".format(Li_Par) + " (" + str(Li_Count) + ")")
print (f"O'Tooley: " + "{:.3%}".format(OTooley_Par) + " (" + str(OTooley_Count) + ")")
print (f"Other: " + "{:.3%}".format(Other_Par) + " (" + str(Other_Count) + ")")
print(" -------------------------")
print(max_key + " is the winner with " + str(Winner) + " votes.")
print(" -------------------------")




# # Create the path for the filename
data_output = os.path.join("C:/DAN_BootCamp/Homework_03-Python/03-Python/Homework_03_From_Dan_Boulden/PyPoll", "data.csv")

# print(f"folder path " + data_output)

# # Write data to a .csv file

with open(data_output, "w", newline="") as csvfile:
     writer = csv.writer(csvfile)

# # To save specific data input as a row in the csv

     writer.writerow([" "])
     writer.writerow([" "])    
     writer.writerow(["Election Results"])
     writer.writerow(["--------------------------------"])
     writer.writerow([f"Total Votes: " + str(Vote_Count)])
     writer.writerow(["--------------------------------"])
     writer.writerow([f"Khan: " + "{:.3%}".format(Khan_Par) + " (" + str(Khan_Count) + ")"])
     writer.writerow([f"Correy: " + "{:.3%}".format(Correy_Par) + " (" + str(Correy_Count) + ")"])
     writer.writerow([f"Li: " + "{:.3%}".format(Li_Par) + " (" + str(Li_Count) + ")"])
     writer.writerow([f"O'Tooley: " + "{:.3%}".format(OTooley_Par) + " (" + str(OTooley_Count) + ")"])
     writer.writerow([f"Other: " + "{:.3%}".format(Other_Par) + " (" + str(Other_Count) + ")"])
     writer.writerow(["--------------------------------"])
     writer.writerow([max_key + " is the winner with " + str(Winner) + " votes."])
     writer.writerow(["--------------------------------"])
    #  writer.writerow([max_key + " is the winner with " + str(Winner) + " votes."])
    #  writer.writerow([f"Greatest Increase in Profits: " + str(MONYEAR_I) + " ($" + str(VTotal_GI3) + ")"])
    #  writer.writerow([f"Greatest Decrease in Profits: " + str(MONYEAR_D) + " ($" + str(VTotal_GI3s) + ")"])
