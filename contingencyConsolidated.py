from acc_convert import AccConv

def RangeGen(Pre_M_E,Post_M_E,Pre_M_C):
    print("\n")
    for i in range (0,75):
        if i % 5 == 0:
            print("Contingency Differential: ",i,"%", sep='')
            Claim_Val = ((Pre_M_E - Pre_M_E*(Pre_M_C/100))-(Post_M_E - Post_M_E*(Pre_M_C/100+i/100)))
            print("Loss of Income: ",AccConv(Claim_Val))
            print("\n")
        else:
            pass

def DiffSpread(Pre_M_E,Post_M_E,Pre_M_C,Claim_Val):
    Post_M_C = 1 - ((Pre_M_E*(1-(Pre_M_C/100)) - Claim_Val)/Post_M_E)
    print("\n")
    print("The Contingency Differential is: ", (AccConv(Post_M_C*100 - (Pre_M_C))), "%", sep = "")
    print("\n")
    print("The Post-Morbid Contingency is: ",AccConv(Post_M_C*100), "%", sep = "")
    print("\n")
    return

def CalcClaim(Pre_M_E,Post_M_E,Pre_M_C, Post_M_C):
    Pre_M_C = Pre_M_C/100
    Post_M_C = Post_M_C/100
    Claim_V = (Pre_M_E - Pre_M_E*Pre_M_C)-(Post_M_E - Post_M_E*Post_M_C)
    Diff = Post_M_C*100 - Pre_M_C*100
    print("\n")
    print("Claim Value = ",AccConv(Claim_V))
    print("Contingency Differential = ", AccConv(Diff), "%", sep = '')
    print(AccConv(Pre_M_C*100),"% contingency deduction on pre-morbid earnings = ", AccConv(Pre_M_E*Pre_M_C), sep="")
    print(AccConv(Post_M_C*100),"% contingency deduction on post-morbid earnings = ", AccConv(Post_M_E*Post_M_C), sep = "")
    print("Contingency Adjusted Pre-Morbid Earnings = ", AccConv(Pre_M_E - Pre_M_E*Pre_M_C))
    print("Contingency Adjusted Post-Morbid Earnings = ", AccConv(Post_M_E - Post_M_E*Post_M_C))

Selection = int

while Selection not in range(1,4):
    try:
        Selection = int(input("For Claim Calculation Select: 1 \nFor Generation of a Schedule Select: 2 \nFor Calculation of a Differential Spread Select: 3 \n\nSelection: "))
        if Selection not in range(1,4):
            print("\nInvalid Selction. Please select from options 1 to ", max(range(1,4)),". \n", sep='')
        else:
            continue
    except:
        print("\nInvalid Selection.\n")
print("\n")

while True:
    try:
        Pre_M_E = float(input("enter the pre-morbid earnings:  "))
    except ValueError:
        print("float values only")
        continue
    else:
        break
while True:
    try:
        Post_M_E = float(input("enter the post-morbid earnings:  "))
    except ValueError:
        print("float values only")
        continue
    else:
        break
while True:
    try:
        Pre_M_C = float(input("enter the pre-morbid contingency as a %:  "))
    except ValueError:
        print("float values only")
        continue
    else:
        break

if Selection == 1:

    while True:
        try:
            Post_M_C = float(input("enter the post-morbid contingency as a %:  "))
        except ValueError:
            print("float values only")
            continue
        else:
            break

    CalcClaim(Pre_M_E,Post_M_E,Pre_M_C,Post_M_C)

elif Selection == 2:

    RangeGen(Pre_M_E,Post_M_E,Pre_M_C)

else:

    while True:
        try:
            Claim_Val = float(input("enter the Offer/Claim Value:  "))
        except ValueError:
            print("float values only")
            continue
        else:
            break

    DiffSpread(Pre_M_E,Post_M_E,Pre_M_C,Claim_Val)
