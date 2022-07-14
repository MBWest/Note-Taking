#READING AND WRITING FILES------------------------------------------------------------

#READING A FILE
months = open('file.txt', "r")
print(months)
print(months.mode)
print(months.readable()) #Prints one line at a time
months.seek(0) #Goes back to first line in file
for month in months: #Print each line out
    print(month.strip()) #Strip the spaces out
print(months.readlines()) #Prints into an array


#WRITING TO A FILE
days = open('days.txt', "w") #Open a new file that hasnt been created in write mode
print(days.mode) #Print the mode out
days.write("Monday") #Write to the days file, this will overwrite anything in the file
days = open('days.txt', "a") #Open a new file that hasnt been created in append mode
days.close() #Close the file

# ---------- File Manipulation ----------
with open(file, "r") as f:  # Opens a file in read mode as variable f
      x = readlines()  # Reads each line and stores it into variable x

with open(file, "a") as f:  # Opens a file in append mode as variable f
      x = writelines("New lines of text")  # Reads each line and stores it into variable x