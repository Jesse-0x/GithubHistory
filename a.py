import os
import random

sentence = "echo $(date) > a.txt && git add . && git commit -a -m 'commit some file'"

#MMDDhhmmyyyy.ss
MM = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
        "11", "12"]
dd = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
        "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
        "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
        "31"]

hh = ["14", "17"]

yyyy = ["2022", "2023"]

dates = []
for l in yyyy:
    for i in MM:
        for j in dd:
            for k in hh:
                for m in range(random.randint(0, 8)):
                    dates.append(f"{i}{j}{k}{random.randint(10, 59)}{l}.0{m}")

a = dates
a = sorted(a)

for i in a:
    os.system('date ' + i)
    os.system(sentence)
    
