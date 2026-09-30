from Brute import *
import json

Data = []
for rollnumber in range(225000, 250000): #Range of roll numbers
    try:
        number, name, father_name = Program(rollnumber)
        Data.append(["Roll Number",rollnumber ,number, name, father_name])
        with open("MassResult2.json", "w", encoding="utf-8") as f:
         json.dump(Data, f, indent=4)
         print("roll no: ", rollnumber, "\n" ,"Number: ", number, "\n", name, "\n", father_name)
    except  Exception:
       continue
input("Your program has finished, write anything to end it \n")
driverexitter()





