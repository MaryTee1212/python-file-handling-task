#File Creation:
#Create a Python script (file_handling_assignment.py) that does the following:
#Creates a new text file named "my_file.txt" in write mode ('w').
#Write at least three lines of text to the file, including a mix of strings and numbers.


#File Reading and Display:
#Enhance your script to read the contents of "my_file.txt" and display them on the console.


#File Appending:
#Modify the script to open "my_file.txt" in append mode ('a').
#Append three additional lines of text to the existing content.


#Error Handling:
#Implement error handling using try, except, and finally blocks to manage potential 
#file-related exceptions (e.g., FileNotFoundError, PermissionError).

#SOLUTION
#Creates a new text file named "my_file.txt" in write mode ('w').
file = open("my_file.txt", "w")

#Write at least three lines of text to the file, including a mix of strings and numbers.
file.write("My name is Omofoye Mary\n")
file.write("second line\n")
file.write("This is a file\n")

file.close()

#File Reading and Display:
#Enhance your script to read the contents of "my_file.txt" 
file_object = open("my_file.txt", "r")
file_contents = file_object.read()
#file_object.close()
#display them on the console.
print(file_contents)

#File Appending:
#Modify the script to open "my_file.txt" in append mode ('a').
#Append three additional lines of text to the existing content.

file_object = open("my_file.txt", "a")
file.write("My Daughter\n")
file.write("She's two years old\n")
file.write("She's intelligent\n")

#Error Handling:
#Implement error handling using try, except, and finally blocks to manage potential 
#file-related exceptions (e.g., FileNotFoundError, PermissionError)
#Using the above  as instance

try:
    file = open("my_file.txt", "w")
    file.write("My name is Omofoye Mary\n")
    file.write("second line\n")
    file.write("This is a file\n")
 
except IOError as e:
        print("Error writing to file:", e)
except Exception as e:
        print("An unexpected error occurred:", e)
finally:
        print("Write operation completed.")

try:
        file_object = open("my_file.txt", "r")
            
except FileNotFoundError:
        print("File not found:", "my_file.txt")
except PermissionError:
        print("Permission denied to open the file:", "my_file.txt")
except Exception as e:
        print("An unexpected error occurred:", e)
finally:
        print("Read operation completed.")

try:
        file_object = open("my_file.txt", "a")
        file.write("My Daughter\n")
        file.write("She's two years old\n")
        file.write("She's intelligent\n")
           
        print("Content appended to", "my_file.txt")
except IOError as e:
        print("Error appending to file:", e)
except Exception as e:
        print("An unexpected error occurred:", e)
finally:
        print("Append operation completed.")


