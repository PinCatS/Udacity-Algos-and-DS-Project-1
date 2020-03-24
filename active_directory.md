# Active directory look up implementation

The structure is a general tree structure.
Thus I decided to use BFS traversing using Queue as a helper data structure.

Time complexity of the traversal is O(m*n) where m is a number of users and n is a number of groups.

Space complexity is O(n) where n is max(of groups on levels) since on each level we queue all groups of the next level.