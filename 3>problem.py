thesum=0
count=0

number1=input('enter a number')
number2=input('enter a number')
number3=input('enter a number')
number4=input('enter a number')
number5=input('enter a number')

thesum+=float(number1)
thesum+=float(number2)
thesum+=float(number3)
thesum+=float(number4)
thesum+=float(number5)
count+=2

average=thesum/count
print('the sum :,',thesum)
print('the average:,',average)