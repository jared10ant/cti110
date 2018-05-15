#CTI-110
#Jared Tennant
#Distance Traveled
#3/25/18

print('Lets calculate the distance for every hour you have traveled')
speed = int(input('What was your speed in mph? '))
hour = int(input('How many hours did you travel? '))
distance = speed * hour
print('Hour\tDistance Traveled')
print('-------------------------')
hour2 = hour + 1
for count in range(1, hour2, 1):
     speed2 = count * speed
     print(count, '\t', speed2)

