In order to find the square root of `number` the algorithm first divides the `number` by 2.
The result is >= square root of number.
If the result is grater than the real root, recurse by dividing again by 2 that result + a small fraction. I followed a method from https://www.mathsisfun.com/square-root.html.

The time complexity is O(log n).
The space complexity is O(log n), corresponding with the call stack of recursion.