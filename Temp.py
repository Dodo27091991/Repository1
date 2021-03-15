from datetime import *
class Parking :
    
    node =""
    v_type=""
    v_num=0
    v_e_day=0
    v_e_month=0
    v_e_year=0
    timeHint=0
    timeMint=0

    def vEntry(self):

        print (" Two whealer : A")
        print ("         Bus : B")
        print ("         Car : C")
        print ("       Truck : D")

        v_type=input("Enter type of Vehical :")
        self.v_type=v_type
        v_num = int(input("Enter Vehical number :"))
        self.v_num=v_num
        now=datetime.now()
        v_e_day=int(now.strftime("%d"))
        self.v_e_day=v_e_day
        v_e_month=int(now.strftime("%m"))
        self.v_e_month=v_e_month
        v_e_year=int(now.strftime("%y"))
        self.v_e_year=v_e_year
        htime=now.strftime("%H")
        timeHint=int(htime)
        self.timeHint=timeHint
        mtime=now.strftime("%M")
        timeMint=int(mtime)
        self.timeMint=timeMint
        timeMint=int(mtime)
        print("*******************************")
        print("* Vehical number :",v_num,"      *")
        print("* Entry time :",now.strftime("%H:%M"),"         *")
        print("* Thank you for Parking       *")
        print("*******************************")

    def createBill(self):
        vemp=self
        now=datetime.now()
        v_e_day=int(now.strftime("%d"))
        v_e_month=int(now.strftime("%m"))
        v_e_year=int(now.strftime("%y"))
        htime=now.strftime("%H")
        timeHint=int(htime)
        mtime=now.strftime("%M")
        timeMint=int(mtime)
        v_year=v_e_year-vemp.v_e_year
        v_month=v_e_month-vemp.v_e_month
        v_day=v_e_day-vemp.v_e_day
        hour=timeHint-vemp.timeHint
        minutes=timeMint-vemp.timeMint

        min_year=v_year*365*24
        min_month=v_month*30*24
        min_day=v_day*24
        min_hour=hour

        if (min_year==0):
            min_year=1
        if (min_month==0):
            min_month=1
        if (min_day==0):
            min_day=1
        if (min_hour==0):
            min_hour=1
        p_time=min_year*min_month*min_day*min_hour

        print("************************ Bill ************************")
        print("* Vehical number : ",vemp.v_num,"                            *")                      
        print("* Checked in at  : ",vemp.timeHint,":",vemp.timeMint,"  ",vemp.v_e_day,"/",vemp.v_e_month,"/",vemp.v_e_year,"            *")
        print("* Checked out at :", now.strftime("%H:%M  %d/%m/%y"),"                  *")
        print("* Time in hours  :",p_time,"                                *")
        print("* Charges Applied: Rs 20/Hour","                       *")
        print("* Payable Amount :",p_time*20,"                               *")
        print("*                                                    *")
        print("* We thank you for your Visit here                   *")
        print("*******************************************************")    

    def checkout(self):
        vemp=self   
        temp2=self 
        
        num=int(input("Enter Vehical number :"))
        if (num==vemp.v_num):
            if (num==0):
                print("You've not parked here")
            else :
                vemp.createBill()
                temp=vemp.node
                vemp.node=""
                return temp
        else:
            vemp=vemp.node
            while(vemp!=""):
                if(num==vemp.v_num):
                    print("Date found")
                    break
                else:
                    self=vemp
                    vemp=vemp.node
                    print("Ittreation")

            if (num==0):
                print("You've not parked here")
            else :
                vemp.createBill()
                self.node=vemp.node
            return temp2

            '''if(vemp.node==""):
                self.node=""
            else :
                self.node=vemp.node'''
            
    
    def summery(self):
        vemp=self
        while(vemp!=""):
            print("*******************************")
            print("* Vehical number :",vemp.v_num,"      *")
            print("* Entry time :",vemp.timeHint,":",vemp.timeMint,"        *")
            print("*******************************")
            vemp=vemp.node
        
vemp=""
temp=""
while(1):
    print(" A for Parking")
    print(" B for checkout")
    print(" E for Exit system")
    print(" C For All vehical parked")
    option=input("Enter your option :")
    if(option=='A' or option =='a'):
        if(temp==""):
            n1=Parking()
            n1.vEntry()
            temp=n1
            print("____________________________________________________________")
        else:
            n2=Parking()
            n2.node=temp
            n2.vEntry()
            temp=n2
            print("____________________________________________________________*") 
    elif (option=='B' or option=='b'):
        vemp=temp
        temp=vemp.checkout()
    elif (option=='E' or option=='e'):
        break
    elif (option=="C" or option=='c'):
        vemp=temp
        vemp.summery()
    
    else:
        print("Invalid option entered. Try again")

              

