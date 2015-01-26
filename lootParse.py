
csv = open('loot.csv', 'r')

line = csv.readline()

print line


while (len(line)>0):
    if (line.find('(') != -1): # This line contains data
        array = line.split(',')
        # Zeroth is empty
        # First is the name
        name = array[1]
        if (name.find('-') != -1):
            break
        # Second is in the format "JOB (iLevel)"
        temp = array[2].split(' ')
        job = temp[0]
        ilevel = temp[1][1:len(temp[1])-1]

        # 3, 4, 5 are job, job, empty
        # 6 and beyond are drops
        i = 6
        drops = 0
        bis = 0
        sand = 0
        oil = 0
        uat = 0
        while (len(array[i]) > 0):
            # If this item matches the player's job or it is a special drop, count it
            if (array[i].find(job) != -1 or array[i].find("Sand")!= -1 or array[i].find("Oil")!= -1 or array[i].find("UAT")!= -1):
                drops = drops + 1
                if (len(array) > i + 1):
                    if (array[i + 1].find("x") != -1):
                        bis = bis + 1
                if (array[i].find("Sand") != -1):
                    sand = sand + 1
                if (array[i].find("Oil") != -1):
                    oil = oil + 1
                if (array[i].find("UAT") != -1):
                    uat = uat + 1
            i = i + 2
            if (i > len(array) - 1):
                break
            
        print "/l6 ", name," (", job, ilevel,") ---", drops," drops (",bis,"bis,",uat,"UAT,",oil,"Oil,",sand,"Sand)"

    # Read the next player
    line = csv.readline()        

