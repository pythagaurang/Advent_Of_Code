import os
import subprocess

i=input("Enter q number: ")

os.mkdir('./'+str(i))
os.chdir('./'+str(i))
file = open("input1.txt", "w") 
file.close()
subprocess.run(["vim","input1.txt"])
file = open("input2.txt", "w") 
file.close()
subprocess.run(["vim","input2.txt"])
with open(f"{i}_1.py","w") as file:
    file.write("file = open('input1.txt')\n")
    file.write("input_list = []\n")
    file.write("for line in file:\n")
    file.write("    print(line)\n")
    file.write("    input_list.append(line.strip())\n")
    file.write("print()\n")
subprocess.run(["vim",f"{i}_1.py"])
with  open(f"{i}_1.py","r") as file1:
    file = open(f"{i}_2.py","w")
    for line in file1:
        file.write(line)
    file.close()
subprocess.run(["vim",f"{i}_2.py"])
