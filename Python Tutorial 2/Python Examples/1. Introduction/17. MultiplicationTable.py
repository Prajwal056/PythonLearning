#  Python Program to Display the multiplication Table

def MulTabel(Table):
    for i in range(1,10+1): 
        res = Table * i
        print('{}*{} ={}'.format(Table,i,res))
MulTabel(2)