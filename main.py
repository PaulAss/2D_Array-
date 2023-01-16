#Display the temperature values that less than 0.
from array import *
temperature = array("i",[25, 12, 5, -2, 38, 0, 19]) 

for i in range(len(temperature)):
  #print(temperature[i])
  if temperature[i] < 0:
    print(temperature[i])
#Display the maximum temperature in the array

max = temperature[0] #Max is set to the value at index position zero
for i in range(len(temperature)):
  #print(temperature[i])
  if temperature[i] > max:
    max=temperature[i]
    
print(max)

facebook_followers = [[11, 120, 35], [15, 86, 90], [44, 8, 250]]
#The 2D array contains the number of followers for a particular facebook account. This values were recorded for the first three day of the week for three weeks. How many users are following this facebook account?

total=0 #set a total variable and initialise to zero
for i in range(len(facebook_followers)): 
  for j in range(len(facebook_followers[i])):
    total=total+ facebook_followers[i][j] #Adding the values
print("The number of followings  for this facebook account is: ",total)

max1=facebook_followers[0][0]#set max to the first value of the array. 
for i in range(len(facebook_followers)): 
  for j in range(len(facebook_followers[i])): 
    if facebook_followers[i][j] >max1:
      max1 = facebook_followers[i][j]
      
    
print("The maximum followings for this facebook account is: ",max1)