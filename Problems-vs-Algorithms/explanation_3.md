
In order to find the maximum sum of two numbers from array of digits, the algorithm first finds the first two highest value digits which will come on left of numbers (highest place order), then next two hightest value numbers which will come after the first tow on the right of the numbers and so on. 
To achieve this, first creates heap by inserting elements from `input_list`. Inserting takes O(log n) time. Inserting all (n) elements takes O(n log n). Then constructs the digits for numbers by deleting from heap. This takes O(n log n).

Time complexity is 2 * O(n log n) -> O(n log n)

Space complexity is O(2 * n).
