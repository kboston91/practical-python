# bounce.py
#
# Exercise 1.5
start_height = 100.00
end_height = 0.0
num_bounces = 10
i = 1 


for i in range(num_bounces): 
   end_height = start_height * .6
   print(i, round(end_height, 4))
   start_height = end_height
   i = i + 1