from dice import *
name = input("Enter your character's name here: ")
filename = name+"sFamilyTree.txt"

f = open(filename,mode='w+')
d6 = Die(6)
d20 = Die(20)
alive = 0
age = 16+d6.roll()
f.writelines(name.title() + ' - ' + str(age) +'\n')
f.write('-----\n-----\n')
f.write('YOUR PARENTS\n')
fathersName = input("Enter your father's name here: ")
dads_age = 35+d20.roll()
f.write(fathersName.title() + " - " + str(dads_age) + "\n")
mothersName = input("Enter your mother's name here: ")
moms_age=35+d20.roll()
f.write(mothersName.title() + " - " + str(moms_age) + ' \n')
siblings = d6.roll()
dads_sibs = d6.roll()
moms_sibs = d6.roll()
dads_bros = 0
moms_bros = 0
dads_sis = 0
moms_sis = 0
gdads_sibs = d6.roll()
gdads_bros = 0
gdads_sis = 0
gmoms_sibs = d6.roll()
gmoms_bros = 0
gmoms_sis = 0
f.write('-----\n-----\n')
f.write('YOUR SIBLINGS\n')
#print("You have " + str(siblings) + " siblings.")
f.write(str(siblings) + " siblings\n")
brothers = 0
sisters = 0

kids = 0
sons = 0
daughters = 0
for i in range (siblings):
    r = d6.roll()
    if (int(r % 2 == 0)):
        brothers += 1
    else:
        sisters += 1


#print("You have " + str(brothers) + " brothers and " + str(sisters) + " sisters.")
f.write (str(brothers) + " brothers\n")
f.write(str(sisters) + " sisters\n")
f.write('-----\n-----\n')
f.write('YOUR SIBLINGS-IN-LAW\n')
i = 0

spouseGender = 0
for i in range (brothers):
    a = i + 1
    alive = d20.roll()
    married = d20.roll()
    broAge = 16+d6.roll()
    kids = 0
    sons = 0
    daughters = 0
    if (alive <=10):
        f.write("Brother #" + str(a) + " has passed away. He was " + str(broAge) + "\n")
        if(married > 10):
            spouseGender = d20.roll()
            if(spouseGender <=10):
                spouseAge = 14+d6.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(gnd % 2 == 0):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Brother was married to a good wife, a lass of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
            else:
                spouseAge = 16+d6.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(int(gnd % 2 == 0)):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Brother was married to a good husband, a lad of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
                
        if(married <=10):
            f.write('Brother was never married\n')
    else:
        f.write('Brother #' + str(a) + " is still alive, he is currently "+ str(broAge) +"\n")
        if (married > 10):
            kids = d6.roll()
            spouseGender = d20.roll()
            if(spouseGender <=10):
                spouseAge = 14+d6.roll()
                
                for num in range(kids):
                    gnd = d6.roll()
                    if(int(gnd % 2 == 0)):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Brother is married to a good wife, a lass of ' + str(spouseAge) + ' years\n')
                f.write('They have ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')

            else:
                spouseAge = 16+d6.roll()
                kids = d6.roll()
                sons = 0
                daughters = 0
                for num in range(kids):
                    gnd = d6.roll()
                    if(gnd % 2 == 0):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Brother is married to a good husband, a lad of ' + str(spouseAge) + ' years\n')
                f.write('They have ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
        if(married <=10):
                f.write('Brother has not married yet\n')
   
    f.write('\n')

#f.write('-----\n')

for i in range (sisters):
    a = i + 1
    alive = d20.roll()
    married = d20.roll()
    age = 14+d6.roll()
    kids = 0
    sons = 0
    daughters = 0
    if (alive <=10):
        f.write("Sister #" + str(a) + " has passed away. She was " + str(age) + "\n")
        if(married > 10):
            spouseGender = d20.roll()
            if(spouseGender <=10):
                spouseAge = 14+d6.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(gnd % 2 == 0):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Sister was married to a good wife, a lass of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
            else:
                spouseAge = 16+d6.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(int(gnd % 2 == 0)):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Sister was married to a good husband, a lad of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
                
        if(married <=10):
            f.write('Sister was never married\n')
    else:
        f.write('Sister #' + str(a) + " is still alive, she is currently "+ str(age) +"\n")
        if (married > 10):
            kids = d6.roll()
            spouseGender = d20.roll()
            if(spouseGender <=10):
                spouseAge = 14+d6.roll()
                
                for num in range(kids):
                    gnd = d6.roll()
                    if(int(gnd % 2 == 0)):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Sister is married to a good wife, a lass of ' + str(spouseAge) + ' years\n')
                f.write('They have ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')

            else:
                spouseAge = 16+d6.roll()
                kids = d6.roll()
                sons = 0
                daughters = 0
                for num in range(kids):
                    gnd = d6.roll()
                    if(gnd % 2 == 0):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Sister is married to a good husband, a lad of ' + str(spouseAge) + ' years\n')
                f.write('They have ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
        if(married <=10):
                f.write('Sister has not married yet\n')
   
    f.write('\n')

f.write('-----\n-----\n')
f.write('YOUR PATERNAL FAMILY\n')
i = 0
for i in range (dads_sibs):
    r = d6.roll()
    if (int(r % 2 == 0)):
        dads_bros += 1
    else:
        dads_sis += 1
spouseGender = 0
for i in range (dads_bros):
    a = i + 1
    alive = d20.roll()
    married = d20.roll()
    age = 35+d20.roll()
    kids = 0
    sons = 0
    daughters = 0
    if (alive <=10):
        f.write("Uncle #" + str(a) + " has passed away. He was " + str(age) + "\n")
        if(married > 10):
            spouseGender = d20.roll()
            if(spouseGender <=10):
                spouseAge = 35+d20.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(gnd % 2 == 0):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Uncle was married to a good wife, a lady of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
            else:
                spouseAge = 35+d20.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(int(gnd % 2 == 0)):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Uncle was married to a good husband, a man of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
                
        if(married <=10):
            f.write('Uncle was never married\n')
    else:
        f.write('Uncle #' + str(a) + " is still alive, he is currently "+ str(age) +"\n")
        if (married > 10):
            kids = d6.roll()
            spouseGender = d20.roll()
            if(spouseGender <=10):
                spouseAge = 35+d20.roll()
                
                for num in range(kids):
                    gnd = d6.roll()
                    if(int(gnd % 2 == 0)):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Uncle is married to a good wife, a lady of ' + str(spouseAge) + ' years\n')
                f.write('They have ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')

            else:
                spouseAge = 35+d20.roll()
                kids = d6.roll()
                sons = 0
                daughters = 0
                for num in range(kids):
                    gnd = d6.roll()
                    if(gnd % 2 == 0):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Uncle is married to a good husband, a man of ' + str(spouseAge) + ' years\n')
                f.write('They have ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
        if(married <=10):
                f.write('Uncle has not married yet\n')
   
    f.write('\n')

f.write('-----\n')

for i in range (dads_sis):
    a = i + 1
    alive = d20.roll()
    married = d20.roll()
    age = 35+d20.roll()
    kids = 0
    sons = 0
    daughters = 0
    if (alive <=10):
        f.write("Aunt #" + str(a) + " has passed away. She was " + str(age) + "\n")
        if(married > 10):
            spouseGender = d20.roll()
            if(spouseGender <=10):
                spouseAge = 35+d20.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(gnd % 2 == 0):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Aunt was married to a good wife, a lady of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
            else:
                spouseAge = 35+d20.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(int(gnd % 2 == 0)):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Aunt was married to a good husband, a man of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
                
        if(married <=10):
            f.write('Aunt was never married\n')
    else:
        f.write('Aunt #' + str(a) + " is still alive, she is currently "+ str(age) +"\n")
        if (married > 10):
            kids = d6.roll()
            spouseGender = d20.roll()
            if(spouseGender <=10):
                spouseAge = 35+d20.roll()
                
                for num in range(kids):
                    gnd = d6.roll()
                    if(int(gnd % 2 == 0)):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Aunt is married to a good wife, a lady of ' + str(spouseAge) + ' years\n')
                f.write('They have ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')

            else:
                spouseAge = 35+d20.roll()
                kids = d6.roll()
                sons = 0
                daughters = 0
                for num in range(kids):
                    gnd = d6.roll()
                    if(gnd % 2 == 0):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Aunt is married to a good husband, a man of ' + str(spouseAge) + ' years\n')
                f.write('They have ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
        if(married <=10):
                f.write('Aunt has not married yet\n')
   
    f.write('\n')
f.write('-----\n-----\n')
f.write('YOUR MATERNAL FAMILY\n')
i = 0
for i in range (moms_sibs):
    r = d6.roll()
    if (int(r % 2 == 0)):
        moms_bros += 1
    else:
        moms_sis += 1
spouseGender = 0
for i in range (moms_bros):
    a = i + 1
    alive = d20.roll()
    married = d20.roll()
    age = 35+d20.roll()
    kids = 0
    sons = 0
    daughters = 0
    if (alive <=10):
        f.write("Uncle #" + str(a) + " has passed away. He was " + str(age) + "\n")
        if(married > 10):
            spouseGender = d20.roll()
            if(spouseGender <=10):
                spouseAge = 35+d20.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(gnd % 2 == 0):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Uncle was married to a good wife, a lady of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
            else:
                spouseAge = 35+d20.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(int(gnd % 2 == 0)):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Uncle was married to a good husband, a man of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
                
        if(married <=10):
            f.write('Uncle was never married\n')
    else:
        f.write('Uncle #' + str(a) + " is still alive, he is currently "+ str(age) +"\n")
        if (married > 10):
            kids = d6.roll()
            spouseGender = d20.roll()
            if(spouseGender <=10):
                spouseAge = 35+d20.roll()
                
                for num in range(kids):
                    gnd = d6.roll()
                    if(int(gnd % 2 == 0)):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Uncle is married to a good wife, a lady of ' + str(spouseAge) + ' years\n')
                f.write('They have ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')

            else:
                spouseAge = 35+d20.roll()
                kids = d6.roll()
                sons = 0
                daughters = 0
                for num in range(kids):
                    gnd = d6.roll()
                    if(gnd % 2 == 0):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Uncle is married to a good husband, a man of ' + str(spouseAge) + ' years\n')
                f.write('They have ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
        if(married <=10):
                f.write('Uncle has not married yet\n')
   
    f.write('\n')

for i in range (moms_sis):
    a = i + 1
    alive = d20.roll()
    married = d20.roll()
    age = 35+d20.roll()
    kids = 0
    sons = 0
    daughters = 0
    if (alive <=10):
        f.write("Aunt #" + str(a) + " has passed away. She was " + str(age) + "\n")
        if(married > 10):
            spouseGender = d20.roll()
            if(spouseGender <=10):
                spouseAge = 35+d20.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(gnd % 2 == 0):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Aunt was married to a good wife, a lady of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
            else:
                spouseAge = 35+d20.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(int(gnd % 2 == 0)):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Aunt was married to a good husband, a man of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
                
        if(married <=10):
            f.write('Aunt was never married\n')
    else:
        f.write('Aunt #' + str(a) + " is still alive, she is currently "+ str(age) +"\n")
        if (married > 10):
            kids = d6.roll()
            spouseGender = d20.roll()
            if(spouseGender <=10):
                spouseAge = 35+d20.roll()
                
                for num in range(kids):
                    gnd = d6.roll()
                    if(int(gnd % 2 == 0)):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Aunt is married to a good wife, a lady of ' + str(spouseAge) + ' years\n')
                f.write('They have ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')

            else:
                spouseAge = 35+d20.roll()
                kids = d6.roll()
                sons = 0
                daughters = 0
                for num in range(kids):
                    gnd = d6.roll()
                    if(gnd % 2 == 0):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Aunt is married to a good husband, a man of ' + str(spouseAge) + ' years\n')
                f.write('They have ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
        if(married <=10):
                f.write('Aunt has not married yet\n')
   
    f.write('\n')
f.write('-----\n-----\n')
f.write('YOUR PATERNAL EXTENDED FAMILY\n')
i = 0
for i in range (gdads_sibs):
    r = d6.roll()
    if (int(r % 2 == 0)):
        gdads_bros += 1
    else:
        gdads_sis += 1
spouseGender = 0
for i in range (gdads_bros):
    a = i + 1
    married = d20.roll()
    age = 45+d20.roll()
    kids = 0
    sons = 0
    daughters = 0
    f.write("Great-Uncle #" + str(a) + " has passed away. He was " + str(age) + "\n")
    if(married > 10):
            spouseGender = d20.roll()
            if(spouseGender <=10):
                spouseAge = 45+d20.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(gnd % 2 == 0):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Great-Uncle was married to a good wife, a lady of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
            else:
                spouseAge = 45+d20.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(int(gnd % 2 == 0)):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Great-Uncle was married to a good husband, a man of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
                
    if(married <=10):
            f.write('Great-Uncle was never married\n')
    f.write('\n')
for i in range (gmoms_sis):
    a = i + 1
    married = d20.roll()
    age = 45+d20.roll()
    kids = 0
    sons = 0
    daughters = 0
    f.write("Great-Aunt #" + str(a) + " has passed away. She was " + str(age) + "\n")
    if(married > 10):
            spouseGender = d20.roll()
            if(spouseGender <=10):
                spouseAge = 45+d20.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(gnd % 2 == 0):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Great-Aunt was married to a good wife, a lady of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
            else:
                spouseAge = 45+d20.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(int(gnd % 2 == 0)):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Great-Aunt was married to a good husband, a man of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
                
    if(married <=10):
            f.write('Great-Aunt was never married\n')
    f.write('\n')
f.write('-----\n-----\n')
f.write('YOUR MATERNAL EXTENDED FAMILY\n')
i = 0
for i in range (gmoms_sibs):
    r = d6.roll()
    if (int(r % 2 == 0)):
        gmoms_bros += 1
    else:
        gmoms_sis += 1
spouseGender = 0

for i in range (gmoms_bros):
    a = i + 1
    married = d20.roll()
    age = 45+d20.roll()
    kids = 0
    sons = 0
    daughters = 0
    f.write("Great-Uncle #" + str(a) + " has passed away. He was " + str(age) + "\n")
    if(married > 10):
            spouseGender = d20.roll()
            if(spouseGender <=10):
                spouseAge = 45+d20.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(gnd % 2 == 0):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Great-Uncle was married to a good wife, a lady of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
            else:
                spouseAge = 45+d20.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(int(gnd % 2 == 0)):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Great-Uncle was married to a good husband, a man of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
                
    if(married <=10):
            f.write('Great-Uncle was never married\n')
    f.write('\n')
f.write('-----\n')
for i in range (gmoms_sis):
    a = i + 1
    married = d20.roll()
    age = 45+d20.roll()
    kids = 0
    sons = 0
    daughters = 0
    f.write("Great-Aunt #" + str(a) + " has passed away. She was " + str(age) + "\n")
    if(married > 10):
            spouseGender = d20.roll()
            if(spouseGender <=10):
                spouseAge = 45+d20.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(gnd % 2 == 0):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Great-Aunt was married to a good wife, a lady of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
            else:
                spouseAge = 45+d20.roll()
                kids = d6.roll()
                for num in range(kids):
                    gnd = d6.roll()
                    if(int(gnd % 2 == 0)):
                        sons +=1
                    else:
                        daughters += 1
                f.write('Great-Aunt was married to a good husband, a man of ' + str(spouseAge) + ' years\n')
                f.write('They had ' + str(kids) + ' kids: ' + str(sons) + ' sons and ' + str(daughters) + ' daughters\n')
                
    if(married <=10):
            f.write('Great-Aunt was never married\n')
    f.write('\n')
f.close()
