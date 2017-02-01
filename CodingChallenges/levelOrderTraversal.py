def LevelOrder(root):
    if not root:
        return
    ans , level = [] , [root]
    ans.append([n for n in level])
    print ans



LevelOrder([3,9,20,None,None,15,7])