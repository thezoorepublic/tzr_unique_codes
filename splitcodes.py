# This program is used to split codes into separate promotions
#just to get the lazywrite function
from generate import lazy_write
i=1
#Codes 1,2 and 3 refer to separate promotions - define how many codes are required for each promotion
#TODO: automate this for multiple promotions and don't manually code it
codes1=250000
codes2=3200000
codes3=0
codes4=0
#these are the lists for each promotion
codes1list=list()
codes2list=list()
codes3list=list()
codes4list=list()


#This is a logic check, it simply counts how many codes were in the list
numberofcodes=0
codeFile = open('codes/codes-all.csv','rU+')
#Split adds blank rows - the next section removes them
rows = codeFile.read().split('\n')
for row in rows:
	#confirm it's not a blank row
	if len(row)>1:
		numberofcodes=numberofcodes+1
		if i<=codes1:
			codes1list.append(row)
			i=i+1
			continue
		if i<=codes2+codes1 and i > codes1:
			codes2list.append(row)
			i=i+1
			continue
		if i<=codes3+codes2+codes1 and i > codes2+codes1:
			codes3list.append(row)
			i=i+1
			continue
		if i<=codes4+codes3+codes2+codes1 and i > codes3+codes2+codes1:
			codes4list.append(row)
			i=i+1
			continue

if numberofcodes > codes1+codes2+codes3+codes4:
	print("You have "+str(numberofcodes)+" in your list however you have only split out "+str(codes1+codes2+codes3+codes4)+" into separate groups - this is a mistake")
if numberofcodes < codes1+codes2+codes3+codes4:
	print("You have "+str(numberofcodes)+" in your list however you have tried to split out "+str(codes1+codes2+codes3+codes4)+" into separate groups - this is a mistake")
lazy_write("575g20190829.csv",codes1list)
lazy_write("1120g20190829.csv",codes2list)
lazy_write("800gSpare.csv",codes3list)
lazy_write("575gSpare.csv",codes4list)