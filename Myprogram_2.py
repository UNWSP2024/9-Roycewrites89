#Royce Daniel, 3/27/2026, "Random number generator"
import random
rando=open("randomnumbers.txt","w")
count=int(input("How many numbers do you want? 1000 Maximum"))

for i in range(count):
            num=random.randint(1,500)
            rando.write(str(num)+"\n")
if count>1000:
        count=1000
        print("1000 is the limit. your number will be set to 1000")
rando.close()
print("numbers generated to randomnumbers.txt")
