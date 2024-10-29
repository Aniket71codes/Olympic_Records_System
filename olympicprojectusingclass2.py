import os
print("\n\n\t\t\t\t\t<<<<<<<<**********PARIS OLYMPICS 2024************>>>>>>>>\n")
fname1="olympicrecord.txt"
fname2="sportsevent.txt"
fname3="participant details.txt"
fname4="winners.txt"
fname5="table.txt"

class Enter_nations:
    a="BEST OF LUCK!!!>>>"

    def __init__(self,i):
        self.country=i
        

    def entercoun(self):

        while (True):               
            if not os.path.exists(fname1):
                print("\n\n\n!!!!!!!!please first create a file!!!!!!!!!")
                break
            self.display()
            with open(fname1,"r") as fobj1:
                self.country=input("\nEnter name of the Country :")
                if (self.country.isalpha()==False):
                    print("please enter a valid name")
                    continue
                self.country=self.country.upper()
                flag=0
                for i in fobj1:
                    if self.country+"\n"==i:
                        print("\n!!!This name has already been entered. Please enter again!!!")
                        flag=1
                if flag==1:
                    continue
            with open(fname1,"a") as fobj1:
                
                fobj1.write(self.country+"\n")
            self.display()
            ch  =input("To continue press 'y' :")
            if ch!="y":
                break
            

                
    def deletecoun(self):
        p=[]
        with open (fname1,"r") as fobj1:
            s=fobj1.readlines()
                
        self.country=self.country.upper()
        fobj1=open (fname1,"w")
        fobj1.close

        with open (fname1,"a") as fobj1:
            for i in s:
                if i==self.country:
                    continue
                fobj1.write(i)

        self.display()
    def display(self):
            print("\n")
            print("LIST OF NAME OF NATIONS")
            print("\n")
            print("............................................................................................................................................")
            with open(fname1,"r") as fobj1:
                for i in fobj1:
                    if i[0]==None:
                        print("no data")
                        break
                    print("->Country :",i)
            print(".............................................................................................................................................")
        


def enterp(fname4,fname3,fname2,fname1):
    
    
    while(True):
        if not os.path.exists(fname1):
            print("\n\n\n!!!!!!!!please first create a file!!!!!!!!!")
            break
        
        #creating objects for class
        l=[]
        with open (fname1,"r") as fobj1:
            s=fobj1.readlines()
        for i in s:
            i=i[:-1]
            s=Enter_nations(i)
            l.append(s)

        try:
            print("\n\n\n1.Enter Country's Name \n2.Delete countri's Name \n3.View Name Of All countries\n4Congratulate nations.\n5.Return to prvious menu")
            ch=int(input("Enter Your choice:"))
            match ch:
                case 1:
                    Enter_nations(0).entercoun()
                 

                case 2:
                    Enter_nations(0).display()
                    name=input("Enter the name of the country to be deleted :")
                    if (name.isalpha()==False):
                            print("please enter a valid name")
                    name=name+'\n'
                    
                    a=Enter_nations(name)
                    a.deletecoun()
                        
                    
                case 3:
                    Enter_nations(0).display()

                case 4:
                  for i in l:
                      print(Enter_nations.a,i.country)
                case 5:
                    break
                case _:
                    print("\n\n\n!!!Please enter a valid input!!!\n\n\n")
        except ValueError as ve:
            print("Please Enter integer value")
        except AssertionError as ae:
            print("Please enter positive integer value")
        except Exception as e:
            print("An error occurred:", e)
            








class Enter_events:
    

    def addev(self):
        
        while (True):
            Enter_events().displaye()
            with open(fname2,"r") as fobj2:
                
                event=input("\n\n\nEnter name of the event :")
                if (event.isalpha()==False):
                    print("please enter a valid name")
                    continue
                event=event.upper()
                flag=0
                for i in fobj2:
                    if event+"\n"==i:
                        print("\nThis Name has already been entered.please Enter again")
                        flag=1
                if flag==1:
                    continue
            with open(fname2,"a") as fobj2:
                ch  =input("To continue press 'y' :")
                fobj2.write(event+"\n")
                if ch!="y":
                    break
    def removeev(self):
        Enter_events().displaye()
        p=[]
        with open (fname2,"r") as fobj2:
            s=fobj2.readlines()
        name=input("enter the name of the event to be removed")
        if (event.isalpha()==False):
                    print("please enter a valid name")
                    
        name=name.upper()
        fobj2=open (fname2,"w")
        fobj2.close
        name=name+"\n"
        with open (fname2,"a") as fobj2:
            for i in s:
                if i==name:
                    continue
                fobj2.write(i)
        Enter_events().displaye()

    def displaye(self):
        print("\n")
        print("LIST OF NAME OF EVENTS")
        print("\n")
        print("............................................................................................................")

        with open(fname2,"r") as fobj2:
            for i in fobj2:
                    print("->EVENT",i)
        print(".............................................................................................................")
        
def events(fname4,fname3,fname2,fname1):
    while(True):
        if not os.path.exists(fname2):
            print("\n\n\n!!!!!!!!please first create a file!!!!!!!!!")
            break
        print("\n\n\n1.Enter an event \n2.Remove an event \n3.View All sports events \n4.Return to prvious menu")
        try:
            ch=int(input("Enter Your choice:"))
            match ch:
                case 1:
                    Enter_events().addev()
                case 2:
                    Enter_events().removeev()
                case 3:
                   
                    Enter_events().displaye()
                case 4:
                    break
                case _:
                    print("\n\n\n!!!Please enter a valid input!!!\n\n\n")
        except ValueError as ve:
            print("Please Enter integer value")
        except AssertionError as ae:
            print("Please enter positive integer value")
        except Exception as e:
            print("An error occurred:", e)





def table(fname4,fname3,fname2,fname1,fname5):
    while(True):
        if not os.path.exists(fname4):
            print("\n\n\n!!!!!!!!please first create a file!!!!!!!!!")
            break
        else:
            gold=[]
            silver=[]
            bronze=[]
            total=[]
            s=[]
            p=[]
            with open(fname4,"r") as fobj4:
                winner=fobj4.readlines()
            with open(fname3,"r") as fobj3:
                details=fobj3.readlines()
            for i in winner:
                i=i.split(",")
                a=i[3]
                a=a[:-1]
                for j in details:
                    j=j.split(",")
                    if i[1]==j[0]:
                        gold=gold+[j[1]]
                    if i[2]==j[0]:
                        silver=silver+[j[1]]
                    if a==j[0]:
                        bronze=bronze+[j[1]]
            total=gold+silver+bronze
            total=set(total)
            for i in total:
                s=[i,gold.count(i),silver.count(i),bronze.count(i)]
                p.append(s)
            for i in range(0,len(p)):
                for j in range(i+1,len(p)):
                    if (p[i][1]<p[j][1]):
                        temp=p[i]
                        p[i]=p[j]
                        p[j]=temp
                    if (p[i][2]<p[j][2])and(p[i][1]==p[j][1]):
                        temp=p[i]
                        p[i]=p[j]
                        p[j]=temp
                    if (p[i][3]<p[j][3])and(p[i][2]==p[j][2])and(p[i][1]==p[j][1]):
                        temp=p[i]
                        p[i]=p[j]
                        p[j]=temp
            print("\n\n\n\t******************************************THE MEDAL TABLE ************************************************")
            print("\t.................................................................................................................")
            for i in p:
                c=i[0]
                c=c[:-1]
                print("\t\tNATION:",c,"\t\tGOLD:",i[1],"\t\tSILVER:",i[2],"\t\tBRONZE:",i[3])
            print("\t.................................................................................................................")

            fobj5=open (fname5,"w")
            fobj5.close
            with open(fname5,"a")as fobj5:
                for i in p:
                    a=i[0]
                    a=a[:-1]
                    fobj5.write(a+","+str(i[1])+","+str(i[2])+","+str(i[3])+"\n")
        break




class Name:
    
    def addna(self):
        
        while (True):


            print("\n")
            print("LIST OF DETAILS OF ALL ATHLETE")
            print("\n")
            print("............................................................................................................")
            with open (fname3,"r") as fobj3:
                s=fobj3.readlines()
            

            for i in s:
            
                i=i.split(",")
                print("->Name:",i[0],"\t\tCountry:",i[1])
            print("............................................................................................................")


                
            with open(fname3,"r") as fobj3:
                s=fobj3.readlines()
                name=input("\nEnter name of the Athlete :")
                if (name.isalpha()==False):
                    print("please enter a valid name")
                    continue
                name=name.upper()
                flag=0
                for i in s:
                    i=i.split(",")
                    if name==i[0]:
                        print("\nThis Name has already been entered.please Enter again")
                        flag=1
                if flag==1:
                    continue
            
            while (True):

                with open(fname3,"a") as fobj3:

                    with open(fname1,"r") as fobj1:
                        a=fobj1.readlines()
                        country=input("Enter Nation of the Athlete :")
                        if (country.isalpha()==False):
                            print("please enter a valid name")
                            continue
                        country=country.upper()
                        country=country+"\n"
                
                    if country not in a:
                        print("\n!!!!!!!!!!<<Invalid country name. Please enter again.>>!!!!!!!!!!")
                        print("\n")
                        print("LIST OF NATIONS")
                        print("\n")
                        print("............................................................................................................")
                        with open(fname1,"r") as fobj1:
                            for i in fobj1:
                                if i[0]==None:
                                    print("no data")
                                    break
                                print("->Country :",i)
                        print(".............................................................................................................")
                        print("\n\nEnter the data again")
                        continue
                    else :
                        break
                    

                    
                        
            with open(fname3,"a") as fobj3:       
            
                fobj3.write(name+","+country)
            ch  =input("\nTo enter details of more participants press'y'")
            if ch!="y":
                break
        
        
    def removena(self):
        print("\n")
        print("LIST OF DETAILS OF ALL ATHLETE")
        print("\n")
        print("............................................................................................................")
        with open (fname3,"r") as fobj3:
            s=fobj3.readlines()
        

        for i in s:
        
            i=i.split(",")
            print("->Name:",i[0],"\t\tCountry:",i[1])
        print("............................................................................................................")
        
        p=[]
        with open (fname3,"r") as fobj3:
            s=fobj3.readlines()
        name=input("\nEnter the name of the Athlete to be removed :")
        if (name.isalpha()==False):
            print("please enter a valid name")
            
        name=name.upper()
        fobj3=open (fname3,"w")
        fobj3.close
        with open (fname3,"a") as fobj3:
            for i in s:
                j=i
                i=i.split(",")
                if i[0]==name:
                    continue
                fobj3.write(j)


        print("\n")
        print("LIST OF DETAILS OF ALL ATHLETE")
        print("\n")
        print("............................................................................................................")
        with open (fname3,"r") as fobj3:
            s=fobj3.readlines()
        

        for i in s:
        
            i=i.split(",")
            print("->Name:",i[0],"\t\tCountry:",i[1])
        print("............................................................................................................")

    def view(self):
        try:
            ch=int(input("\n1.View deatails of all Athletes\n2.view details of an athlete"))
            match ch:
                case 1:
                    print("\n")
                    print("LIST OF DETAILS OF ALL ATHLETE")
                    print("\n")
                    print("............................................................................................................")
                    with open (fname3,"r") as fobj3:
                        s=fobj3.readlines()
                    

                    for i in s:
                    
                        i=i.split(",")
                        print("->Name:",i[0],"\t\tCountry:",i[1])
                    print("............................................................................................................")
                case 2:
                    with open (fname3,"r") as fobj3:
                        name=input("enter the name of participant to be displayed")
                        for i in fobj3:
                            l=i.split(",")
                            if l[0]==name:
                                print("->Name: ",l[0],"\t\tCountry: ",l[1])
        except ValueError as ve:
            print("Please Enter integer value")
        except AssertionError as ae:
            print("Please enter positive integer value")
        except Exception as e:
            print("An error occurred:", e)





def parti(fname4,fname3,fname2,fname1):
    while(True):
        if not os.path.exists(fname3):
            print("\n\n\n!!!!!!!!please first create a file!!!!!!!!!")
            break
        print("\n\n\n1.ENTER details of an Athlete\n2.Remove details of an Athlete \n3.View details of an Athlete\
\n4.Return to prvious menu")
        try:
            ch=int(input("Enter Your choice :"))
            match ch:
                case 1:
                    Name().addna()
                case 2:
                    Name().removena()
                case 3:
                    Name().view()
                case 4:
                    break
                case _:
                    print("\n\n\n!!!Please enter a valid input!!!\n\n\n")
        except ValueError as ve:
            print("Please Enter integer value")
        except AssertionError as ae:
            print("Please enter positive integer value")
        except Exception as e:
            print("An error occurred:", e)






class Winners:
    

    def winna(self):
        
        with open(fname2,"r") as fobj2:
            a=fobj2.readlines()
        with open(fname3,"r") as fobj3:
            c=fobj3.readlines()
        d=[]
        for i in c:
            i=i.split(",")
            d=d+[i[0]]
            
        while(True):
            while(True):

                with open(fname4,"r") as fobj4:
                    
                    print("\n")
                    print("LIST OF NAME OF ALL EVENTS IN OLYMPICS :")
                    print("\n")
                    print("............................................................................................................")

                    with open(fname2,"r") as fobj2:
                        for i in fobj2:
                                print("->EVENT",i)
                    print(".............................................................................................................")


                    print("\n\nLIST OF ENTERED EVENTS :")
                    print("...........................................................................................................")
                    with open (fname4,"r") as fobj4:
                        for i in fobj4:
                            l=i.split(",")
                            print("->Event:",l[0])
                    print("...........................................................................................................")

                    name=input("\n\n\nEnter name of the event :")
                    if (name.isalpha()==False):
                        print("please enter a valid name")
                        continue
                    name=name.upper()
                    flag=0
                with open(fname4,"r") as fobj4:
                    for i in fobj4:
                        i=i.split(",")
                        if name==i[0]:
                            print("\nThis Event has already been entered.please Enter again")
                            flag=1
                    if flag==1:
                        continue
                
                if (name+"\n") not in a:
                    print("\n\n!!!!!!!!please enter the correct Event!!!!!!!!")
                    continue
                else:
                    break
            while(True):
                
                print("\n")
                print("LIST OF DETAILS OF ALL ATHLETE")
                print("\n")
                print("............................................................................................................")
                with open (fname3,"r") as fobj3:
                    s=fobj3.readlines()
                

                for i in s:
                
                    i=i.split(",")
                    print("->Name:",i[0],"\t\tCountry:",i[1])
                print("............................................................................................................")
                
                gold=input("Enter the winner of gold meadal :")
                if (gold.isalpha()==False):
                        print("please enter a valid name")
                        continue
                gold=gold.upper()
                if gold not in d:
                    print("\n\n!!!!!!!!please CHOOSE from the list participating athlete!!!!!!!!")
                    print("\n")
                    continue
                else:
                    break
            
            while(True):
                
                print("\n")
                print("LIST OF DETAILS OF ALL ATHLETE")
                print("\n")
                print("............................................................................................................")
                with open (fname3,"r") as fobj3:
                    s=fobj3.readlines()

                for i in s:
                
                    i=i.split(",")
                    print("->Name:",i[0],"\t\tCountry:",i[1])
                print("............................................................................................................")
                silver=input("Enter the winner of silver meadal :")
                if (silver.isalpha()==False):
                        print("please enter a valid name")
                        continue
                silver=silver.upper()
                if silver not in d:
                    print("\n\n!!!!!!!!please CHOOSE from the list participating athlete!!!!!!!!")
                    print("\n")
                    continue
                else:
                    break
            while(True):
                
                print("\n")
                print("LIST OF DETAILS OF ALL ATHLETE")
                print("\n")
                print("............................................................................................................")
                with open (fname3,"r") as fobj3:
                    s=fobj3.readlines()

                for i in s:
                
                    i=i.split(",")
                    print("->Name:",i[0],"\t\tCountry:",i[1])
                print("............................................................................................................")
                bronze=input("Enter the winner of bronze meadal :")
                if (bronze.isalpha()==False):
                        print("please enter a valid name")
                        continue
                bronze=bronze.upper()
                if bronze not in d:
                    print("\n\n!!!!!!!!please CHOOSE from the list participating athlete!!!!!!!!")
                    print("\n")
                    continue
                else:
                    break
            with open(fname4,"a") as fobj4:
                fobj4.write(name+","+gold+","+silver+","+bronze+"\n")
            ch  =input("\nTo continue enter 'y'")
            if ch!="y":
                    print("\n\n*******************************OUTCOMES OF ALL EVENTS***********************************")
                    print("...........................................................................................................")
                    with open (fname4,"r") as fobj4:
                        for i in fobj4:
                            l=i.split(",")
                            print("->Event:",l[0],"\tGold:",l[1],"\tsilver:",l[2],"\tbronze:",l[3])
                    print("...........................................................................................................")
                    break
    def removwin(self):
        print("\n\n*******************************OUTCOMES OF ALL EVENTS***********************************")
        print("...........................................................................................................")
        with open (fname4,"r") as fobj4:
            for i in fobj4:
                l=i.split(",")
                print("->Event:",l[0],"\tGold:",l[1],"\tsilver:",l[2],"\tbronze:",l[3])
        print("...........................................................................................................")

        
        p=[]
        with open (fname4,"r") as fobj4:
            s=fobj4.readlines()
        name=input("enter the event to be removed")
        if (name.isalpha()==False):
                print("please enter a valid name")
                
        name=name.upper()
        fobj4=open (fname4,"w")
        fobj4.close
        with open (fname4,"a") as fobj4:
            for i in s:
                j=i
                i=i.split(",")
                if i[0]==name:
                    continue
                fobj4.write(j)


                
        print("\n\n*******************************OUTCOMES OF ALL EVENTS***********************************")
        print("...........................................................................................................")
        with open (fname4,"r") as fobj4:
            for i in fobj4:
                l=i.split(",")
                print("->Event:",l[0],"\tGold:",l[1],"\tsilver:",l[2],"\tbronze:",l[3])
        print("...........................................................................................................")


        
        
    def viewin(self):
        try:
            ch=int(input("1.View winners of every event\n2.View number of medals won by a sinle athlete\
        \n3.no. of medals won by each athlete"))
            match ch:
                case 1:
                    print("\n\n*******************************OUTCOMES OF ALL EVENTS***********************************")
                    print("...........................................................................................................")
                    with open (fname4,"r") as fobj4:
                        for i in fobj4:
                            l=i.split(",")
                            print("->Event:",l[0],"\tGold:",l[1],"\tsilver:",l[2],"\tbronze:",l[3])
                    print("...........................................................................................................")
                case 2:
                    gold=0
                    silver=0
                    bronze=0
                    with open(fname4,"r")as fobj4:
                        s=fobj4.readlines()
                    name=input("Enter the athlete's name :")
                    for i in s:
                        i=i.split(",")
                        if name==i[1]:
                            gold=gold+1
                        if name==i[2]:
                            silver=silver+1
                        if (name+"\n"==i[3]):
                            bronze=bronze+1
                        total =gold+silver+bronze
                    print("\n\n\n->Name:",name,"\tGold:",gold,"\tSilver:",silver,"\tBronze:",bronze,"\tTotal",total)
                case 3:
                    print("\n\n*******************************MEDAL WON BY EACH ATHLETE***********************************")
                    print("...........................................................................................................")
                    d=[]
                    with open(fname3,"r") as fobj3:
                        a=fobj3.readlines()
                    for j in a:
                        j=j.split(",")
                        
                        gold=0
                        silver=0
                        bronze=0
                        with open(fname4,"r")as fobj4:
                            s=fobj4.readlines()
                        for i in s:
                            i=i.split(",")
                            if j[0]==i[1]:
                                gold=gold+1
                            if j[0]==i[2]:
                                silver=silver+1
                            if (j[0]+"\n"==i[3]):
                                bronze=bronze+1
                            total =gold+silver+bronze
                        print("\n->Name:",j[0],"\tGold:",gold,"\tSilver:",silver,"\tBronze:",bronze,"\tTotal",total)
                    print("...........................................................................................................")
        except ValueError as ve:
            print("Please Enter integer value")
        except AssertionError as ae:
            print("Please enter positive integer value")
        except Exception as e:
            print("An error occurred:", e)
                    
                
                
def win(fname4,fname3,fname2,fname1):
    while(True):
        if not os.path.exists(fname4):
            print("\n\n\n!!!!!!!!please first create a file!!!!!!!!!")
            break
        print("\n\n\n1.Enter medal winner of events \n2. Delete medal winner of events \n3.View details of medal winners\
\n4.Return to prvious menu")
        try:
            ch=int(input("Enter Your choice:"))
            match ch:
                case 1:
                    Winners().winna()
                case 2:
                    Winners().removwin()
                case 3:
                    Winners().viewin()
                case 4:
                    break
                case _:
                    print("\n\n\n!!!Please enter a valid input!!!\n\n\n")
        except ValueError as ve:
            print("Please Enter integer value")
        except AssertionError as ae:
            print("Please enter positive integer value")
        except Exception as e:
            print("An error occurred:", e)













    
while(True):
    print("\n\n\n1.Enter nations.\n2.Enter sport's events.\n3.Enter participant details.\n\
4.Enter medal winner of each event.\n5.View medal table.\n6.Create a new file.\n7.Exit.")
    try:
        ch=int(input("\n\nEnter your choice :"))
        match ch:
            case 1:
                enterp(fname4,fname3,fname2,fname1)


                
            case 2:
                events(fname4,fname3,fname2,fname1)

                
            case 3:
                parti(fname4,fname3,fname2,fname1)

                
            case 4:
                win(fname4,fname3,fname2,fname1)

                
            case 5:
                table(fname4,fname3,fname2,fname1,fname5)

                
            case 6:
                c=input("do your really want to create a new file by deleting previous data y/n:")
                if c=='y':
                    with open(fname1,"w") as fobj1:
                        print("\n\n\n***************Country file created***************")
                    with open(fname2,"w") as fobj2:
                        print("***************Event file created*****************")
                    with open(fname3,"w") as fobj3:
                        print("********Participants details file created*********")
                    with open(fname4,"w") as fobj4:
                        print("*************Event winner file created************")
                        
            
            case 7:
                exit()
                
            case _:
                print("\n\n\n!!!Please enter a valid input!!!\n\n\n")
            
    except ValueError as ve:
        print("Please Enter integer value")
    except AssertionError as ae:
        print("Please enter positive integer value")
    except Exception as e:
        print("An error occurred:", e)




