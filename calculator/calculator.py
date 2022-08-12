# develop by aryan salemabadi
#-------------------------------------------------- liberys
import math
#-------------------------------------------------- first variables
result_list = []
calculate = []
#-------------------------------------------------- main loop
while True:
    #---------------------------------------------------------------- main program
    entery = input("insert your numbers or sin cos tan cot sec csc or power and radical: ").lower()
    if entery == "sin":
        deg = float(input("please insert your number of degree: "))
        rad = math.radians(deg)
        sin = math.sin(rad)
        entery = sin
    elif entery == "cos":
        deg = float(input("please insert your number of degree: "))
        rad = math.radians(deg)
        cos = math.cos(rad)
        entery = cos
    elif entery == "tan":
        deg = float(input("please insert your number of degree: "))
        rad = math.radians(deg)
        tan = math.tan(rad)
        entery = tan
    elif entery == "cot":
        deg = float(input("please insert your number of degree: "))
        rad = math.radians(deg)
        tan = math.tan(rad)
        cot = 1 / tan
        entery = cot
    elif entery == "sec":
        deg = float(input("please insert your number of degree: "))
        rad = math.radians(deg)
        cos = math.cos(rad)
        sec = 1/cos
        entery = sec
    elif entery == "csc":
        deg = float(input("please insert your number of degree: "))
        rad = math.radians(deg)
        sin = math.sin(rad)
        csc = 1/sin
        entery = csc
    elif entery == "power" :
        Basenumber = float(input("please insert Base number :"))
        powernumber = float(input("please insert Powe number: "))
        pown = pow(Basenumber,powernumber)
        entery = pown
    elif entery == "radical":
        number = float(input("please insert your number: "))
        sqrtnumber = math.sqrt(number)
        entery = sqrtnumber
    calculate.append(entery)
    oprator = input(" insert  oprator (+ - / * =)  :  ")
    #---------------------------------------------------------oprators management
    if oprator == "+" or oprator == "-" or oprator == "*" or oprator == "/":
        calculate.append(oprator)
    elif oprator == "=":
        #---------------------------------------------- calculates management
        while True:
            if len(calculate) == 1 :
                result_list = result_list + calculate
            elif calculate[1] == "+":
               x =  float(calculate[0]) + float(calculate[2])
               calculate.insert(0,x)
               for i in range(3,0,-1):
                   calculate.remove(calculate[i])
            elif calculate[1] == "-":
               x =  float(calculate[0]) - float(calculate[2])
               calculate.insert(0,x)
               for i in range(3,0,-1):
                   calculate.remove(calculate[i])
            elif calculate[1] == "*":
               x =  float(calculate[0]) * float(calculate[2])
               calculate.insert(0,x)
               for i in range(3,0,-1):
                   calculate.remove(calculate[i])
            elif calculate[1] == "/":
               x =  float(calculate[0]) / float(calculate[2])
               calculate.insert(0,x)
               for i in range(3,0,-1):
                   calculate.remove(calculate[i])
            else:
                pass
            if len(calculate) == 1 :
                break
            #----------------------------------------- result management
        print(float(calculate[0]))
        result_list = result_list + calculate
        calculate.clear()
        show = input("do you want see the latest calculat? (yes or no) :  ").lower()
        if show == "yes" :
          numbercalculate = int(input("which calculate? : "))
          if numbercalculate <= 0 :
              print("please insert number > 0 thanks")
          else:
            pass
          if len(result_list) < 11:
            if numbercalculate > len(result_list):
                print(" not found number of calcaulate is smallre than your number")
            else:
             print(result_list[numbercalculate - 1])
          elif len(result_list) >= 11 :
             print(result_list[len(result_list) - (10 - numbercalculate)])
          else:
             pass
        else:
            pass        
    else:
        print(" please insert + - * / or = ")
        break