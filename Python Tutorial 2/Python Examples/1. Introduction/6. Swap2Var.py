def SwapUsingtempVar(a,b):
    print('Before Swaping {} {}'.format(a,b))
    temp = a
    a = b
    b = temp
    print('After Swaping {} {}'.format(a,b))
def SwapWithoutUsingTemp(a,b):
    print('Before Swaping {} {}'.format(a,b))
    a = a+b
    b = a-b  # 5 - 3 = 2
    a = a-b # 5 - 2 = 3
    print('After Swaping {} {}'.format(a,b))

SwapUsingtempVar(1,2)
SwapWithoutUsingTemp(3,2)