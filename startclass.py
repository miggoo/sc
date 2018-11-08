import os
import subprocess
import path
#My course folder is on my desktop so I've set that as the base filename
coursefileslocation = "C:\\Users\\micha\\Desktop\\"
#kept the 2 variables separate in case 1 of them changes in future
jupyterbase = "C:\\Users\\micha\\Desktop\\UCBMaster\\"
### subprocess.Popen('explorer "C:\\Users\\micha\\Desktop\\UCBMaster\\DATAGL\\UCBWorking\\UCBSAN201807DATA3\\course-content"')
# 


def startFolder(desktop, topic, session, *jyn):
    jyn = str(
        input("Should I Launch Jupyter Notebook for you? (y/n): ")).lower().strip()
    foldername = coursefileslocation + \
        "UCBMaster\\DATAGL\\UCBWorking\\UCBSAN201807DATA3\\course-content\\" + \
        topic+"\\activities\\"+session
    
    subprocess.call(f"explorer {foldername}", shell=True)
    #will launch jupyter at the coursefileslocation location for easier transfer between 
    # reply = str(input('Launch Jupyter Notebook? Enter (y/n): ')).lower().strip()
    print("Opening " + foldername)
    #Ask user input on whether or not to launch Jupyter Notebook
    jyn = str(input("Should I Launch Jupyter Notebook for you? (y/n): ")).lower().strip()

    if jyn == "y":
            subprocess.call(f"jupyter notebook {jupyterbase}", shell=True)
    if jyn == "n":
            print("Jupyter Not Launched")
    # subprocess.call(f"jupyter notebook {jupyterbase}", shell=True)

           
startFolder(coursefileslocation, "08-SQL", "01",'y')

# # def yes_or_no(question):
# #     while "the answer is invalid":
# #         reply = str(input(question+' (y/n): ')).lower().strip()
# #         if reply[0] == 'y':
# #             return True
# #         if reply[0] == 'n':
# #             return False

# subprocess.call(f"jupyter notebook {desktop}", shell=True)

# Panopto videos linked to topics not days (maybe even activities)
# Sumcheck?
# Parsing students so that students with more DA/DS/DV intensive questions to the right tutor \
# 

# filename =
# print(filename.name)
# # prints "raw_data.txt"

# print(filename.suffix)
# # prints "txt"

# print(filename.stem)
# # prints "raw_data"

# if not filename.exists():
#     print("Oops, file doesn't exist!")
# else:
#     print("Yay, the file exists!")
# #!/usr/bin/python
