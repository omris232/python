while (True):
     c=int(input("please choose 1-4 option: \nMENU: \n1. insert num and ** by 3 \n2. insert 4 ip and add to list and print it \n3. insert 4 enteris dns to dic \n4. check if string i polindrom \nyour choise: "))
     if c==1:
         x=int(input("enter a num:"))
         print(x**3)
         mylist=[]
     elif c==2:
         for i in range(4):
             l=(input("enter a ip"))
             mylist.append(l)
         print(mylist)
     elif c==3:
         mydic={}
         for i in range(4):
             k=input("enter a key")
             v=input("enter a value")
             mydic.update({k:v})
         print(mydic)
     elif c==4:
         s = (input("enter a string:"))
         #list=s.split()

         s1=(s[::-1])
         if s==s1:
             print("is a polindrom")
         else:
             print("it's no polindrom")
     else:
         print("enter 1-4 only..")
         exit=(input("if you want to exit type yes or no"))
         if exit=="yes":
             break
         else:
             continue

print ("bye bye...")

