def preorder_rec(root):
    """
    前序遍历
    :param root: 当前需要遍历的树的根结点
    :return:
    """
    # 跳出递归的条件：根结点为空树
    if root is None:
        # 只写return 默认是返回None
        return
    # 访问根结点
    print(root.val)
    # 左子结点递归
    preorder_rec(root.left)
    # 右子结点递归
    preorder_rec(root.right)


def inorder_rec(root):
    """
    中序遍历
    :param root: 当前需要遍历的树的根结点
    :return:
    """
    # 跳出递归的条件：根结点为空树
    if root is None:
        # 只写return 默认是返回None
        return
    # 左子结点递归
    preorder_rec(root.left)
    # 访问根结点
    print(root.val)
    # 右子结点递归
    preorder_rec(root.right)


def postorder_rec(root):
    """
    后序遍历
    :param root: 当前需要遍历的树的根结点
    :return:
    """
    # 跳出递归的条件：根结点为空树
    if root is None:
        # 只写return 默认是返回None
        return
    # 左子结点递归
    preorder_rec(root.left)
    # 右子结点递归
    preorder_rec(root.right)
    # 访问根结点
    print(root.val)