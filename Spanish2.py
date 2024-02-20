import random
import re
#EtoS = {}
f=open("Spanish2.txt", 'r')
CD=[]
ID = []
qa={}
for line in f:
	m=re.search('Chapter',line)
	if (m):
		CD.append(ID)
		ID=[]
		line = f.readline()
	l=line.split(',')
	del l[-1] #delete the last element which is space or new line
	k=l.pop(0)
	qa={}
	qa[k]=l
	ID.append(qa.copy())

CD.append(ID)


#Now CD has complete list. CD[0][0] doesn't hold any value....as chapters start with 1


                      
#1. 1A_(74)          
#2. 1B_(97)          
#3. 2A_(80)          
#4. 2B_(109)          
#5. 3A_()         
#6. 3B_()          
#7. 4A_()          
#8. 4B_()          
#9. 5A_()
#10. 5B_()
#11. 6A_()
#12. 6B_()
#13. 7A_()
#14. 7B_()
#15. 8A_()
#16. 8B_()
#17. 9A_()
#18. 9B_()




#Taking a test from random chapter
#you can randomize this as well
#this is how we get the info

maxq = 10
ch= random.randint(1,len(CD)-1)
questions = random.sample(range(0,len(CD[ch])),maxq)



#this generates a list of random numbers in range...
print("Test is going to be from Chapter: " + str(ch))
print("Test contains " + str(maxq) + " questions." + "\n")
score=0
for q in questions:
	iword = input("\n" + list(CD[ch][q].keys())[0] + ": ")
	tl=list(CD[ch][q].values())[0]
	aaa = ["Incorrect","Wrong","Invalid","Erroneous","Mistaken"]
	aa = random.choice(aaa)
	bbb = ["Correct!","Accurate!","Flawless!","Impressive!","Dazzling!"]
	bb = random.choice(bbb)
	if iword in tl:
		print(bb)
		score = score + 1
		print("Score = " + str(score) + "\n")
	else:
		print(aa + " ---> " + (tl)[0] + "\n")
		
print("Your grand total is: " + str(score))


def percent(score, maxq):
        score = float(score)
        maxq = float(maxq)
        percentage = "{0:.2f}".format((score / maxq * 100))
        return percentage

print("You scored: " + percent(score, maxq) + "%")








