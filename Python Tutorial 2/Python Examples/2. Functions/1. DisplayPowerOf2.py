# Display the powers of 2 using anonymous function

terms = 10

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms+1)))

print("The total terms are:",terms)
for i in range(terms+1):
   print("2 raised to power",i,"is",result[i])


res = lambda x: 2**x
for i in range(10+1):
    print('2 pow of {} = {}'.format(i,res(i)))


    