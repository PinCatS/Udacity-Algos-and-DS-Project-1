# File recursion impleamntation explanation

Since file system is a tree, we can use tree traversal algorithm for searching files that satisfy our input requirements (in this case is match with the suffix).

There was a requirement that there are no limit to the depth of the subdirectories can be. This requirement means we can't use recursion to implement the tracersal.

We still can use DFS with stack but I selected BFS only because I get used to implement DFS using recursion and BFS using queue.

The time complexity of the algorithm is O(n) where n is all directories and files because we need to traverse all these.

The space comlexity is O(m) where m is max number of sibling directories or files within a level.