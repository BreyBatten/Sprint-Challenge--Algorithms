#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The run time would be O(2^n). As n grows, the number of loops the function runs grows at an exponential rate. For example, if n = 2, the while loop would be 2 * 2 * 2 = 6. The loop would run 6 times. If n = 3, the loop runs 27 times. So adding 1 to n increases the loop by a lot.

b) This run time would be O(n^2) because the for loop is going to run n times. Each of those iterations will have a while loop that runs n-1 times. We can drop the `-1` from n - 1 leaving us with n * n or n^2.


c) This is a recursive call, so each time the function runs, it calls itself again with one less bunny, until it reaches 0 bunnies. Essentially, as n grows, it just adds another function call to the stack, so the run time would be O(n).

## Exercise II
I believe the best strategy would be a binary search method. Divide the `n` floors / 2, which would place you on the middle floor. If the egg breaks, you know you can focus on the lower half, if it doesn't focus on the upper half. Repeat the process of dividing remaining floors in half and testing above or below, depending on whether or not the egg broke, until you reach the final answer. The run time would be O(n).


