You are given pointer to the root of the binary search tree and two values  and . You need to return the lowest common ancestor (LCA) of  and  in the binary search tree.

        2
       / \
      1   3
         / \
        4   5
             \
              6
 
In the diagram above, the lowest common ancestor of the nodes  and  is the node . Node  is the lowest node which has nodes and  as descendants.

**Function Description**

Complete the function lca in the editor below. It should return a pointer to the lowest common ancestor node of the two values given.

lca has the following parameters: 
- root: a pointer to the root node of a binary search tree 
- v1: a node.data value 
- v2: a node.data value

**Input Format**

The first line contains an integer, , the number of nodes in the tree. 
The second line contains  space-separated integers representing  values. 
The third line contains two space-separated integers,  and .

To use the test data, you will have to create the binary search tree yourself. Here on the platform, the tree will be created for you.

**Constraints**

 1 <= n, node.data <= 25
 1 < v1, v2 <= 25
 v1 != v2
 The tree _will_ contain data equal to v1 an v2
 
 
The tree will contain nodes with data equal to  and .

**Output Format**

Return the a pointer to the node that is the lowest common ancestor of  and .

**Sample Input**

    6
    4 2 3 1 7 6
    1 7

v1 = 1 and v2 = 7


           4
          / \
         2   \
        / \   \
       1   3   7
              /
             6


**Sample Output**

[reference to node 4]

Explanation

LCA of 1 and 7 is 4, the root in this case. 
Return a pointer to the node.