def preorder_iterate(root):
    """

    :param root: 待遍历的树的根结点
    :return:
    """
    # 栈使用列表模拟，用于记录暂时未访问的结点
    stack = []
    while root or stack:
        while root:
            # 先序遍历，先访问根结点
            print(root.val)
            # 因为右子结点再左子结点后面访问，所以要先记录
            stack.append(root.right)
            # 沿左分支下行，直到叶子结点
            root = root.left
        # 回溯,处理右子结点
        root = stack.pop()


def inorder_iterate(root):
    """
    中序遍历（迭代）

    :param root: 待遍历的树的根结点
    :return:
    """
    # 栈使用列表模拟，用于记录暂时未访问的结点
    stack = []
    while root or stack:
        while root:
            # 根结点在左子结点后面访问，所以先记录
            stack.append(root)
            # 沿左分支下行，直到叶子结点
            root = root.left
        # 回溯
        root = stack.pop()
        # 处理根结点
        print(root.val)
        # 处理右结点
        root = root.right


def postorder_iterate(root):
    """
    后序遍历（迭代）

    :param root: 待遍历的树的根结点
    :return:
    """

    # 栈使用列表模拟，用于记录暂时未访问的结点
    stack = []
    while root or stack:
        while root:  # 内层循环，找到叶子结点
            # 因为是后续遍历，所以当前结点先入栈
            stack.append(root)
            root = root.left if root.val else root.right
        # root可能是叶子结点（左右子结点都为None的根结点），也可能是左右子结点已经遍历了的根结点
        root = stack.pop()
        # 处理根结点
        print(root.val)
        # 如果栈不为空，栈顶元素即为当前结点的父结点，将父结点的左结点与当前结点比较，判断当前结点是左子结点还是右子结点
        # 如果是左子结点，转去处理右子结点
        if stack and stack[-1].left == root:
            root = stack[-1].right
        # 1、如果栈为空：说明遍历全部完成，退出循环。2、如果是右子结点，那么父结点应该出栈，此时继续跳出大循环，然后再入循环
        else:
            root = None










