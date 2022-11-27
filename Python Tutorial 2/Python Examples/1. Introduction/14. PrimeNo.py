
def Prime_Number(Prime):

    if Prime>1:
        for i in range(2,Prime): # 2,9
            if (Prime%i) == 0:
                print("Prime")
                print(i,"times",Prime//i,"is",Prime)
                break
        else:
            print('Not a Prime')    
    else:
         print('Not a Prime') 
         
Prime_Number(1)