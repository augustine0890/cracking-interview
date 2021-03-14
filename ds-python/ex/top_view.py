# Problem: https://www.hackerrank.com/challenges/tree-top-view/

def topView(root):
    # Create a dictionary
    d = {}

    def traverse(root, key, level):
        if root:
            if key not in d:
                d[key] = [root, level]
            elif d[key][1] > level:
                d[key] = [root, level]
            
            # traverse to left and right of tree
            traverse(root.left, key-1, level+1)
            traverse(root.right, key+1, level+1)
    
    traverse(root, 0, 0)
    for key in sorted(d):
        print(d[key][0], end=" ")
    
    
    
    

    
    
    

    
    
    
    


