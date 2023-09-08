I solved this problem following the guided steps and using the Trie data structure learned previously
Instead of manipulating each character, this exercise works with each part of a url delimited by the '/' character.
Splitting the path into parts is supported by the split() method, for the rest I just apply what I have learned about Trie.

Suppose there is a path with n parts, the worst case is that there are n distinct elements

* RouteTrie's complexity:
Since storing children is a dictionary, accessing each child node is only O(1)
=> The insert and find operation that needs to be performed to a depth of n will have a time complexity of O(n)
Algorithm needs to store n characters and it doesn't take extra memory to store extra words => Space complexity is O(n)

* Router's complexity:
- With the add_path operation consisting of 2 serial operations, split_path and insert, both have O(n) time and space complexity.
=> add_path has a time and space complexity of O(n)
- With the lookup operation consisting of 2 serial operations, split_path and find, both have O(n) time and space complexity.
=> lookup has a time and space complexity of O(n)

======================= update comment's =======================
# RouteTrieNode
* __init__(self):
- Time complexity analysis: O(1)
- Space complexity analysis: O(1)

* insert(self, path):
- Time complexity analysis: O(1)
- Space complexity analysis: O(1)

# RouteTrie
* __init__(self):
- Time complexity analysis: O(1)
- Space complexity analysis: O(1)

* insert(self, path, handler):
- Time complexity analysis: O(n)
- Space complexity analysis: O(n)

* find(self, path):
- Time complexity analysis: O(n)
- Space complexity analysis: O(1)

# Router
* __init__(self):
- Time complexity analysis: O(1)
- Space complexity analysis: O(1)

* add_handler(self, path, handler):
- Time complexity analysis: O(n)
- Space complexity analysis: O(n)

* lookup(self, path):
- Time complexity analysis: O(n)
- Space complexity analysis: O(n)

* split_path(self, path):
- Time complexity analysis: O(n)
- Space complexity analysis: O(n)
