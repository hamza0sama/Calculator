import math
class Calculator:
    def __init__(self):
        self.result=0
    #******************************************************
    def Add(self,*nums):
        try:
            self.result=0
            for num in nums:
                self.result +=num
            return self.result
        except Exception:
            print("Invalid input: please enter numeric values only.")
    #******************************************************
    def Multip(self,*nums):
        try:
            self.result=1
            for num in nums:
                self.result *=num
            return self.result
        except Exception:
            print("Invalid input: please enter numeric values only.")
    #******************************************************
    def Subtract(self,*nums):
        try:
            self.result = nums[0]
            for num in nums[1:]:
                self.result -= num
            return self.result
        except Exception:
            print("Invalid input: please enter numeric values only.")
    #******************************************************
    def Division(self,*nums):
        try:
            self.result = nums[0]
            for num in nums[1:]:
                if num ==0:
                    print("can't divide by zero!")
                    return None
                self.result /= num
            return self.result
        except Exception:
            print("Invalid input: please enter numeric values only.")
    #******************************************************
    def Power (self,numer,power):
        try:
            return numer ** power
        except Exception:
            print("Invalid input: please enter numeric values only.")
    #******************************************************
    def Sin(self, angle):
        try:
            return math.sin(math.radians(angle))
        except Exception:
            print("Invalid input: please enter numeric values only.")
    #******************************************************
    def Sin_invers(self, num):
        try:
            return math.degrees(math.asin(num))
        except Exception:
            print("Invalid input: please enter numeric values only.")
    #******************************************************
    def Cos(self, angle):
        try:
            return math.cos(math.radians(angle))
        except Exception:
            print("Invalid input: please enter numeric values only.")
    #******************************************************
    def Cos_invers(self, num):
        try:
            return math.degrees(math.acos(num))
        except Exception:
            print("Invalid input: please enter numeric values only.")
    #******************************************************
    def Tan(self, angle):
        try:
            return math.tan(math.radians(angle))
        except Exception:
            print("Invalid input: please enter numeric values only.")
    #******************************************************
    def Tan_invers(self, num):
        try:
            return math.degrees(math.atan(num))
        except Exception:
            print("Invalid input: please enter numeric values only.")
    #******************************************************
    def factorial(self, num):
        try:
            if not isinstance(num, int) or num < 0:
                print("Invalid input: please enter non-negative integer.")
                return None
            if num == 0:
                return 1
            return num * self.factorial(num - 1)
        except Exception:
            print("Invalid input: please enter numeric values only.")
    #******************************************************
    def Log(self, num, base=10):
        try:
            if num <=0 or base <=0 or base==1:
                print("Invalid log arguments: num >0, base >0 and !=1")
                return None
            return math.log(num, base)
        except Exception:
            print("please enter positive number and valid base")
    #******************************************************
    def Pow_exponent_base(self, exponent, base):
        try:
            return self.Power(base, exponent)
        except Exception:
            print("Invalid input: please enter numeric values only.")
#***************************************************************************************************************************************
calc=Calculator()
while True: 
    try:
            opration=int(input("hello please choose the number of opration\nAdd => 1\nSubtract => 2\nMultip => 3\nDivision => 4\nPower => 5\nLog => 6\nPow_exponent_base => 7\nfactorial => 8\nSin => 9\nCos => 10\nTan => 11\nSin_invers => 12\nCos_invers => 13\nTan_invers => 14\nfor exit => 15\n").strip())
    except Exception:
        print("Invalid input: please enter positive and numeric values only.")
#******************************************************
    if opration ==1:
        num=[]
        ask=1
        while ask==1:
           try:

            num.append( float(input("enter numbers you want to Add\n")))
            ask=int(input("did you finish?\nif you finished choose 0 and 1 if not\n").strip())
            
           except ValueError:
               print("Invalid input: please enter numeric values only.\n")


        print(f"the result of add opration is : {calc.Add(*num)}.\n")    


#******************************************************
    elif opration ==2:
        num=[]
        ask=1
        while ask==1:
           try:
                
                num.append( float(input("enter numbers you want to Subtract\n")))
                ask=int(input("did you finish?\nif you finished choose 0 and 1 if not\n").strip())

           except ValueError:
                print("Invalid input: please enter numeric values only.\n") 

        print(f"the result of Subtract obration is : {calc.Subtract(*num)}.\n")

#******************************************************

    elif opration ==3:
        num=[]
        ask=1
        while ask==1:
           try:

            num.append( float(input("enter numbers you want to Multip\n")))
            ask=int(input("did you finish?\nif you finished choose 0 and 1 if not\n").strip())

           except ValueError:
               print("Invalid input: please enter numeric values only.\n")
        
        print(f"the result of Multip opration is : {calc.Multip(*num)}.\n")

#******************************************************

    elif opration ==4:
        num=[]
        ask=1
        while ask==1:
           try:

            num.append( float(input("enter numbers you want to Division\n")))
            ask=int(input("did you finish?\nif you finished choose 0 and 1 if not\n").strip())

           except ValueError:
               print("Invalid input: please enter numeric values only.\n")

        print(f"the rseult of Division opration is : {calc.Division(*num)}.\n")

#******************************************************

    elif opration ==5:
        number=float(input("enter the number2\n"))
        power=float(input("enter the power\n"))
        print(f"the result of power opration is: {calc.Power(number,power) }.\n") 
#******************************************************
    elif opration ==6:
        number=float(input("enter the number\n"))
        bais=float(input("enter the bais\n"))
        print(f"the result of log opration is : {calc.Log(number,bais)}.\n")
#******************************************************
    elif opration ==7:
        number=float(input("enter the number\n"))
        bais=float(input("enter the bais\n"))
        print(f"the result of power exponent base is : {calc.Pow_exponent_base(exponent=number, base=bais)}.\n")
#******************************************************
    elif opration ==8:
        num=int(input("enter the number\n"))
        print(f"the result of factorial is : {calc.factorial(num)}.\n")
#******************************************************
    elif opration ==9:
        angle=float(input("please enter the angle\n"))
        print(f"the result of sin is : {calc.Sin(angle)}.\n")
#******************************************************
    elif opration ==10:
        angle=float(input("please enter the angle\n"))
        print(f"the result of Cos is : {calc.Cos(angle)}.\n")
#******************************************************
    elif opration ==11:
        angle=float(input("please enter the angle\n"))
        print(f"the result of Tan is : {calc.Tan(angle)}.\n")
#******************************************************
    elif opration ==12:
        number=float(input("please enter the number\n"))
        print(f"the result of Sin_invers is : {calc.Sin_invers(number)}.\n")
#******************************************************
    elif opration ==13:
        number=float(input("please enter the number\n"))
        print(f"the result of Cos_invers is : {calc.Cos_invers(number)}.\n")
#******************************************************
    elif opration ==14:
        number=float(input("please enter the number\n"))
        print(f"the result of Tan_invers is : {calc.Tan_invers(number)}.\n")
#******************************************************
    elif opration ==15:
        print("thank you!")
        break
#******************************************************
    else :
        print("Wrong choose please choose correctly !\n")
        continue
#******************************************************