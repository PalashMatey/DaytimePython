def ZigZagLevelOrderTraversal(root):
    #Solution is using two stacks
    s1_lr,s2_rl = [root], []
    #the idea is that, popping from stack s1_lr we look and left then right and push it onto s2_rl
    #It is the other way for s2_rl: We look for right and then left
    output, rl = [], True
    #rl is used technically as an alternator
    while s1_lr or s2_rl:
        temp = []
        if rl:
            while s1_lr:
                node = s1_lr.pop()
                temp.append(node.val)
                if node.left:
                    s2_rl.append(node.left)
                if node.right:
                    s2_rl.append(node.right)
        else:
            while s2_rl:
                node = s2_rl.pop()
                temp.append(node.val)
                if node.right:
                    s1_lr.append(node.right)
                if node.left:
                    s1_lr.append(node.left)
        rl = not rl
        output.append(temp)
    return output

