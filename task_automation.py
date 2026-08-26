import os

print("===== Task Automation - File Creator =====")

filename = input("Enter file name: ")
content = input("Enter content: ")

with open(filename, "w") as file:
    file.write(content)

print("\nFile created successfully!")
print("File name:", filename)

# Check whether the file exists
if os.path.exists(filename):
    print("Automation completed successfully.")
else:
    print("File creation failed.")
    //output
    ===== Task Automation - File Creator =====
Enter file name: Enter content: 
File created successfully!
File name: task3.txt
Automation completed successfully.
