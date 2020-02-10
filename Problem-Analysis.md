	Problem #1
I used binary search to get the square root. Each time the search array can be narrowed 
down to half of the last search array.
So, the run time is O(log(n)).

	Problem #2
The whole array is rotated, which means this array is composed with two sorted array.
So I first use a helper function "find_max()" to return the maximum value's index. With the location of maximum number, we can easily locate a rough area of the target number, ie. left part or right part. Then we can find the target use a binary search.
I used two search function, both in binary search to meet the specification that run time
complexity is O(log(n)).

	Problem #3
My thoughts were to sort the input list first. As the digits of two numbers cannot differ by one. Assume the final numbers are a and b. We can access the sorted list from the largest to the smallest, and assign number to a and b in turn one by one from higer digit to lower digit.
I used merge sort here, which has a run time of nlog(n) and a iteration to assign numbers that has a run time of n. So the final run time complexity would be nlog(n).

	Problem #4
As the input list has only 0, 1, and 2. Zeros and twos are respectively smallest and largest numbers here. So, I created a list with all 'ones'. Then, I wanted to append zeros from the left of the list and append twos from the right of the list. 
A while loop here represents the single traversal, and has a run time of O(n).

	Problem #5
In this problem, I basically defined the class "TrieNode" with initial function ,insert  character function, and a finding suffixes function, and the class "Trie" with initial function, insertion, and a find function. 
The function "finding suffixes" and "finding prefix node" both have a complexity of O(n).

	Problem #6
First I initialized the "min" and "max" as the first number in the array. In the iteration or traversal, if the number is bigger, assigning it to the "max", similar for the "min".
So, with a single traversal, the run time is O(n).

	Problem #7
In this problem, I defined "RouteTrie" and "RouteTride" classes first. With "trie", we can access different paths, as we can split the path using "/". The process to build three classes are similar to problem #5.
There are several iterations in this problem.The run time complexity would be n.
