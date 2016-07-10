# 100 Door Problem. In Python

#Puzzle:
#There are 100 doors in a long hallway. They are all closed. The first time you walk by each door, you open it. The second time around, you close every second door (since they are all opened). On the third pass you stop at every third door and open it if it's closed, close it if it's open. On the fourth pass, you take action on every fourth door. You repeat this pattern for 100 passes.
#At the end of 100 passes, what doors are opened and what doors are closed?

#Solution:
#This soution is focused on high memory optimization on the cost of processing time.
#An array of four 32 bit integer is used to store status of 100 doors. Each bit in a integer represents a door. Set bit (1) represents open door and reset bit (0) represents closed door. Bitwise shifting is used to access each bit.


# MY ASSUMPTIONS ##########

# MY CONVENTIONS ##########
# 0 is closed, 1 is open

# MY CODE #################

doors = [0,0,0,0]

def print_me_in_binary(arr):
    for a in arr:
        print "{0:b}".format(a)


pass_number = 1
while pass_number <= 100:
    # create masking array
    #mask = 
    
    pass_number += 1
    
print_me_in_binary(doors)    