The idea is find the pivot first ( by binary search ), 
then depend on the pivot compare with search value, 
we use binary search one time again 


Time complexity: O(log⁡n)

The algorithm requires one binary search to locate pivot, and at most 2 binary searches to find target. Each binary search takes O(log⁡n) time.
Space complexity: O(1)

We only need to update several parameters left, right and mid, which takes O(1) space.