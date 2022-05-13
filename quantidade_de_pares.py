# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# Example:
# n=7
# ar=[1,1,2,1,2,3,2]

# There is one pair of color and one of color. There are three odd socks left, one of each color. The number of pairs is 2.

# Function Description
# Complete the sockMerchant function in the editor below.
# sockMerchant has the following parameter(s):
#     int n: the number of socks in the pile
#     int ar[n]: the colors of each sock

# Returns
#     int: the number of pairs

# Input Format
# The first line contains an integer n, the number of socks represented in ar.
# The second line contains space-separated integers, , the colors of the socks in the pile.


def sockMerchant(n, ar):
    pair_array = []
    pair = 0
    for item in range(n):
        count = 1
      
        for index in range(n):
        
            if (n - (index + 1)) > item:
          
                if ar[n - (index + 1)] == ar[item]:
                    count = count + 1
                    
        pair_array.append(count)
    
    for item in pair_array:
        if (item % 2) == 0:
            pair = pair + 1
    
    return pair

    