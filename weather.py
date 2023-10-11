#program to display weather using if,elif,if-else

temp=75
if temp > 80:
    print("It's too hot!")
    print("Stay inside")
elif temp < 60:
    print("It's too cold!")
    print("stay inside")
else:
    print("Enjoy outdoors")

temp2= 60
if temp2 > 80 or temp2 < 60:
    print("stay inside!")
else:
    print("Enjoy the outdoors!")

rain=True

if rain:
    print("stay inside!")