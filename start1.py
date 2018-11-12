import os
import subprocess
import path
import fnmatch
#My course folder is on my desktop so I've set that as the base filename
coursefileslocation = "C:\\Users\\micha\\Desktop\\"
jupyterbase = "C:\\Users\\micha\\Desktop\\UCBMaster\\"
### subprocess.Popen('explorer "C:\\Users\\micha\\Desktop\\UCBMaster\\DATAGL\\UCBWorking\\UCBSAN201807DATA3\\course-content"')
# 

topic = str(input(f'What topic number? (Enter 2 digits)'))
sess = str(input(f'What Session? (Enter 2 digits)'))


# def startFolder(desktop, topic, session, *jyn):
f1 = f"{coursefileslocation}UCBMaster\\DATAGL\\UCBWorking\\UCBSAN201807DATA3\\course-content\\"
foldername = f'"{f1}{topic}"'
for folder in os.listdir(f'{f1}'):
    if folder.startswith(f'{topic}'):
        subprocess.call(f"explorer {f1}{folder}\\activities\\{sess}\\", shell=True)
    #will launch jupyter at the coursefileslocation location for easier transfer between 
reply = str(input('Launch Jupyter Notebook? Enter (y/n): ')).lower().strip()
if reply[0] == 'y':
            subprocess.call(f"jupyter notebook {jupyterbase}", shell=True)
if reply[0] == 'n':
            print("No Jupyter Notebook Launched")
#             return False
    # subprocess.call(f"jupyter notebook {jupyterbase}", shell=True)
print(f"{f1}{folder}")
    
# startFolder(coursefileslocation, "08-SQL", "01")

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
