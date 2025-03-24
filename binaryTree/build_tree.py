# 106. Construct Binary Tree from Inorder and Postorder Traversal

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())
        in_order_index = inorder.index(root.val)  # = 1

        root.right = self.buildTree(inorder[in_order_index+1:], postorder)
        root.left = self.buildTree(inorder[:in_order_index], postorder)

        return root


if __name__ == "__main__":
    # Arrays de teste
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    # Criando uma instância da solução
    solution = Solution()

    # Construindo a árvore
    root = solution.buildTree(inorder, postorder)

    # Função auxiliar para imprimir a árvore em ordem (in-order traversal)
    def print_inorder(node):
        if not node:
            return
        print_inorder(node.left)
        print(node.val, end=" ")
        print_inorder(node.right)

    # Função auxiliar para imprimir a árvore em pós-ordem (post-order traversal)
    def print_postorder(node):
        if not node:
            return
        print_postorder(node.left)
        print_postorder(node.right)
        print(node.val, end=" ")

    # Verificando a árvore construída
    print("Inorder da árvore construída:")
    print_inorder(root)  # Deve imprimir: 9 3 15 20 7

    print("\nPostorder da árvore construída:")
    print_postorder(root)  # Deve imprimir: 9 15 7 20 3
