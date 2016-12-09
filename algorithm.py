#Create a random list using the following
import random
import time

l = range(15000)
random.shuffle(l)
start_time = time.time()

#Write an alogorithm that sorts the list by looking at 2 elements at a time and swaps them if the first element is larger.  Loop through the list until it is sorted from smallest to largest element

# so like, you create a function to do the thing.
def bubbleSort(l):
#create a variable like 'n' that determines the length of whatever 'l' is, so like, 100 or whatever.
    n = len(l)

    #this is like, the thing that makes it loop through the array. So like, for 'i' (each integer) in the range of 'n', which is the length of the range, remember? so this says, "okay get ready to do the following to each integer in your range or whatever"
    for i in range(n):

        # Last i elements are already in place. Like, this is pretty straightforward?
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1 (This means loop through the array from 0 to the highest number minus one because we're keeping it within the range.)
            # Swap if the element found is greater
            # than the next element
            # So like j is whatever the number is as it's looping, then it's comparing it and then swapping em accordingly.
            if l[j] > l[j+1] :
                l[j], l[j+1] = l[j+1], l[j]

#Call that shit, gurl!
bubbleSort(l)

print ("Sorted array is:")
#calling bubbleSort only makes it perform the action, you're not gonna see it until you tell it to fucking print.
print l

# Bonus, measure how long it takes to sort
# Created a variable called running_time that calculates how long it took by subtracting the time you started the process from the time it is currently when you finished.
running_time = time.time() - start_time
print running_time


#try changing the list size and see how the time is affected
