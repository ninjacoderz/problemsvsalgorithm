
I solved this problem following the guided steps and using the Trie data structure learned previously
Suppose n is the length of the word => worst case there are n non-duplicate characters
Since storing children is a dictionary, accessing each child node is only O(1)
=> The insert and find operation that needs to be performed to a depth of n will have a time complexity of O(n)
Algorithm needs to store n characters and it doesn't take extra memory to store extra words => Space complexity is O(n)

# TrieNode
* __init__(self):
- Time complexity analysis: O(1)
- Space complexity analysis: O(1)

* insert(self, char):
- Time complexity analysis: O(1)
- Space complexity analysis: O(1)

* suffixes(self, suffix = ''):
- Time complexity analysis: O(n)
- Space complexity analysis: O(n)

# Trie
* __init__(self):
- Time complexity analysis: O(1)
- Space complexity analysis: O(1)

* insert(self, word):
- Time complexity analysis: O(n)
- Space complexity analysis: O(n)

* find(self, prefix):
- Time complexity analysis: O(n)
- Space complexity analysis: O(1)
