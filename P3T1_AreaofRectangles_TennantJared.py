#CTI-110
#Area of Rectangles
#Jared Tennant
#02/23/18

print("Lets find the area of two rectangles and which one is larger")
length_1 = int(input("What is the length of the first rectangle?"))
width_1 = int(input("What is the width of the first rectangle?"))
length_2 = int(input("What is the length of the second rectangle?"))
width_2 = int(input("What is the width of the second rectangle?"))
area_1 = length_1 * width_1
area_2 = length_2 * width_2
if area_1 > area_2:
     print("The first rectangle has a larger area")
elif area_1 < area_2:
     print("The second rectangle has a larger area")
else:
     print("The rectangles are equal in area")
