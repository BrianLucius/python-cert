from datetime import datetime

programs = []
# episodes = []

with open("scraped.txt") as input_data:
    for line in input_data:
        if ("file:" in line) or ("title:" in line):
            # f=open("cleaned.txt", "a")
            # f.write(str(line.strip())+"\n")
            # f.close()
            # # print(line.strip())
            programs.append(str(line.strip())+"\n")
# print(episodes)
            
for i in range(0, len(programs), 2):
    # print(programs[i+1][8:programs[i+1].find(";")])
    date = datetime.strptime(programs[i+1][8:programs[i+1].find(";")], '%A, %b %d, %Y').strftime("%m/%d/%Y")
    touchdate = datetime.strptime(programs[i+1][8:programs[i+1].find(";")], '%A, %b %d, %Y').strftime("%Y%m%d")
    filename = datetime.strptime(programs[i+1][8:programs[i+1].find(";")], '%A, %b %d, %Y').strftime("%m%d%y")
    title = programs[i+1][programs[i+1].find("Echoes"):-3]
    url = programs[i][programs[i].find("https"):-2]
    url = url[:8] + 'brianlucius:KGBMjS36c@' + url[8:]
    # episodes.append(date)
    # episodes.append(title)
    # episodes.append(url)
    # print("Title:", programs[i+1], "URL:", programs[i])
    print('./recover_echoes.sh "', date, '" "',title, '" "', url, '" "20:00:00" "01:58:30"', sep="", end="\n")
    print('touch -t ',touchdate, '2000 ./media/', filename, '_200000.mp3',sep="", end="\n")

# print(episodes)

