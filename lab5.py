number1= int(input('enter number:'))
if(number1%3==0 and number1%5==0):
        print('Tic Tac')
elif(number1%5==0):
    print('Tac')
elif(number1%3==0):
    print('Tic')
else:
    print(number1)

count=1
while(count<20):
    print(count)
    count=count+1