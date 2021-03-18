# This program is used to split codes into separate promotions
#just to get the lazywrite function
from generate import lazy_write
from csv import writer


#This is a logic check, it simply counts how many codes were in the list
numberofcodes=0

original_filename="541FridgePack19.11.20/541fridgecodes-spare.txt"
new_filename='541FridgePack19.11.20/541fridgecodes-spare-columns.txt'
fullcodelist=[]
codeFile = open(original_filename,'rU+')
rows = codeFile.read().split('\n')
print len(rows)
i=0
for row in rows:
    if i==0:
        fullcodelist.append(row)
    elif i>=2:
        fullcodelist.append(" ")
        fullcodelist.append(row)
        fullcodelist.append("\n")

        i=0
        continue
    else:
        fullcodelist.append(" ")
        fullcodelist.append(row)
    i+=1

codeFile.close()
outputFile=open (new_filename, 'w')
for x in fullcodelist:
    outputFile.write (x)


#Split adds blank rows - the next section removes them
#
# for row in rows:
# 	#confirm it's not a blank row
# 	if len(row)>1:
# 		numberofcodes=numberofcodes+1
# 		if i<=codes1:
# 			codes1list.append(row)
# 			i=i+1
# 			continue
# 		if i<=codes2+codes1 and i > codes1:
# 			codes2list.append(row)
# 			i=i+1
# 			continue
# 		if i<=codes3+codes2+codes1 and i > codes2+codes1:
# 			codes3list.append(row)
# 			i=i+1
# 			continue
# 		if i<=codes4+codes3+codes2+codes1 and i > codes3+codes2+codes1:
# 			codes4list.append(row)
# 			i=i+1
# 			continue
#
# if numberofcodes > codes1+codes2+codes3+codes4:
# 	print("You have "+str(numberofcodes)+" in your list however you have only split out "+str(codes1+codes2+codes3+codes4)+" into separate groups - this is a mistake")
# if numberofcodes < codes1+codes2+codes3+codes4:
# 	print("You have "+str(numberofcodes)+" in your list however you have tried to split out "+str(codes1+codes2+codes3+codes4)+" into separate groups - this is a mistake")
# lazy_write("575g20190829.csv",codes1list)
# lazy_write("1120g20190829.csv",codes2list)
# lazy_write("800gSpare.csv",codes3list)
# lazy_write("575gSpare.csv",codes4list)