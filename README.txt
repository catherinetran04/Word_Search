Name: Catherine Tran


You should assume the following:


*The letter grid parameter has width W and height H.
*The word parameter has length L.
*concatenating a letter to a string takes O(1) time
*the get_size function takes O(1) time
*accessing a list by index takes O(1) time


Your task:


#Q1 
What is the Big-O runtime of the extract function in terms of W, H, and L
(defined above)


(Please attempt to explain your reasoning. An incorrect answer with no
stated reasoning will not be subject to partial credit)


O(1) len = 0 + O(L) loop through letters + O(1) if in of grid
-> O(L) is the largest -> Big-O = O(L)


#Q2
What is the Big-O runtime of the find function in terms of W, H, and L
(defined above)
(Please attempt to explain your reasoning. An incorrect answer with no
stated reasoning will not be subject to partial credit)
O(HW) looping through each grid letter + O(4) for each direction + O(L) looping through letters in word + O(1) if out of grid + O(1) if match
-> O(HW) is the largest therefore will be the Big-O runtime