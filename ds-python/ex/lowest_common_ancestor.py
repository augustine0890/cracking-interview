# Problem: https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/

def lca(root, v1, v2):
    if root is None:
        return
    if v1 > v2:
        v1, v2 = v2, v1
    if (root.info == v1) or (root.val == v2):
        return root
    
    left_lca = lca(root.left, v1, v2)
    right_lca = lca(root.right, v1, v2)

    if left_lca and right_lca:
        return root
    return left_lca if left_lca is not None else right_lca
    
    