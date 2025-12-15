/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public static void PreOrder(TreeNode root,Set<TreeNode> hs)
    {
        if(root==null) return;
        hs.add(root);
        PreOrder(root.left,hs);
        PreOrder(root.right,hs);
    }
    public int countNodes(TreeNode root) {
        Set<TreeNode> hs=new HashSet<>();
        PreOrder(root,hs);
        return hs.size();
    }
}