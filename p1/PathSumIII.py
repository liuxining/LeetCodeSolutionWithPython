# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    n = 0
    l = []
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        n = 0#找到的总和为sum的个数
        i = 1#遍历变量，从1开始
        s = [root]#模拟栈
        l = []#和列表
        #先序遍历二叉树
        while len(s) != 0:
            p = s[0]
            if p:
                #p非空
                l.append(p.val)
                t = i
                if t % 2 == 0:
                    while t / 2 != 0:
                        l[t / 2] += p.val
                        if t / 2 == sum:
                            n += 1
                        t = t / 2
                else:
                    while (t - 1) / 2 != 0:
                        l[(t - 1) / 2] += p.val
                        if (t - 1) / 2 == sum:
                            n += 1
                        t = (t - 1) / 2
                s.append(p.left)
                s.append(p.right)
            s.remove(p)
        return n

if __name__ == "__main__":




