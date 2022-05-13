# There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game. For each game, you will get an array of clouds numbered if they are safe or if they must be avoided.

# Example
# c = [0,1,0,0,0,1,0]
# Index the array 0...6 from . The number on each cloud is its index in the list so the player must avoid the clouds at indices 1 and 5. They could follow these two paths: 0-> 2 ->4 ->6 or 0->2->3 ->4 ->6 . The first path takes 3 jumps while the second takes 4. Return 3.

# Function Description
# Complete the jumpingOnClouds function in the editor below. jumpingOnClouds has the following parameter(s):
#     int c[n]: an array of binary integers

# Returns
#     int: the minimum number of jumps required

# Input Format

# The first line contains an integer n, the total number of clouds. The second line contains space-separated binary integers describing clouds c[i] where 0<= i<=n.


def jumpingOnClouds(c):
    jumps = 0
    
    skip_next_cloud = False
    for index in range(len(c)):

        if skip_next_cloud:
            skip_next_cloud = False
            continue

        if c[index] == 1:
            continue

        if index < (len(c) - 2) and c[index + 2] == 0:
            jumps = jumps + 1
            skip_next_cloud = True
        elif index < len(c) - 1 and c[index + 1] == 0:
            jumps = jumps + 1
            
    return jumps


# c for em python 

# for (i = 0; i < 10; i++)
#    if someCondition:
#       i+=1
# print i

# In python would be written as

# i = 0
# while i < 10
#    if someCondition
#       i += 1
#    print i
#    i += 1
