import os, subprocess, path, fnmatch, http.server

#My course folder is on my desktop so I've set that as the base filename
coursefileslocation = "C:\\Users\\micha\\Desktop\\"
jupyterbase = "C:\\Users\\micha\\Desktop\\UCBMaster\\"
### subprocess.Popen('explorer "C:\\Users\\micha\\Desktop\\UCBMaster\\DATAGL\\UCBWorking\\UCBSAN201807DATA3\\course-content"')
# 

topic = str(input(f'What topic number? (Enter 2 digits)'))
sess = str(input(f'What Session? (Enter 2 digits)'))
ex = str(input(f'What Exercise Number? (Enter 2 digits)'))
# a = "'alias git-bash=' / git-bash.exe & > / dev/null 2 & >1"

# def startFolder(desktop, topic, session, *jyn):
f1 = f"{coursefileslocation}UCBMaster\\DATAGL\\UCBWorking\\UCBSAN201807DATA3\\course-content\\"
foldername = f'"{f1}{topic}"'
for folder in os.listdir(f'{f1}'):
    if folder.startswith(f'{topic}'):
        for folders in os.listdir(f"{f1}{folder}\\activities\\{sess}\\"):
            if folders.startswith(f'{ex}'):
                subprocess.call(f"explorer {f1}{folder}\\activities\\{sess}\\{folders}", shell=True)
                subprocess.call(f"notepad {f1}{folder}\\activities\\{sess}\\{folders}\\README.md", shell=True)


    #will launch jupyter at the coursefileslocation location for easier transfer between 
reply = str(input('Want to launch a server? Enter j for jupyter, m for mongodb, p for Python http.server): ')).lower().strip()
if reply[0] == 'j':
        #     subprocess.call("git-bash", shell=True)
        subprocess.call(f"jupyter notebook {coursefileslocation}", shell=True)
        print(f"Jupyter Notebook launched at {coursefileslocation}")
if reply[0] == 'm':
        subprocess.call(f"mongod", shell=True)
        print(f"MondoDB launched {coursefileslocation}")       
if reply[0] == 'n':
        print(f"Session Folder opened for {f1}{sess}")
        exit()
             
#   end
# return False
    # subprocess.call(f"jupyter notebook {jupyterbase}", shell=True)
# print(f"{f1}{folder}")
    
# startFolder(coursefileslocation, "08-SQL", "01")


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
