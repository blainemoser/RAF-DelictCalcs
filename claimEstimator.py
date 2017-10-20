# uncomment out to apply the cap
# Also set the cap

def Projection(starting_age,career_ceiling_age,cap,x,a):

    from acc_convert import AccConv

    y = a/(career_ceiling_age - starting_age) #salary increases
    z = 0

    for i in range(starting_age,65):
        if x >= cap:
                x = cap
        z += x
        if i <= career_ceiling_age - 2:
            print(i,"-",i+1," ","R",AccConv(x)," ","R",AccConv(z), sep = "")
            x += y
        else:
            print(i,"-",i+1," ","R",AccConv(x)," ","R",AccConv(z), sep = "")

cap = 201337
starting_age = 22
career_ceiling_age = 35
x = 50000 #starting yearly earnings
a = 935269
Projection(starting_age,career_ceiling_age,cap,x,a)
