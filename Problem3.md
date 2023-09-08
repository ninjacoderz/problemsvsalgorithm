To have the biggest total, we need to have 2 biggest numbers
With condition "The number of digits in both the numbers cannot differ by more than 1": 
    so the numbers should alternatively created by getting digits from sorted array of digit.
I will use the "marker" array for represent the number of appearance of digits.
I using "while" loop to create num_1 & num_2 arrays

We use 1 "for" loop to create "marker" array, the 2 nested "while", but the nested while is reduced 1 by the outer "while"
    Complexity: 0(n.log(n)) 
Because we need store marker and num_1, num_2 array:
    Auxiliary Space: O(n) 