# Implementation & testing of the BinaryTree traversal methods

# Import file
from TEST_CODE import *
import os
from BinaryTree import BinaryTree

'''
Testing details can be found in TEST_CODE.py

ENSURE ALL TESTS PASS BEFORE SUBMITTING

IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama
'''


def main():
    BT = BinaryTree()
    initialize(BT)

    # Tree Review!
    # This is not a test and has nothing to do with your code
    VIEW_tree()

    # TEST 1 - Test BinaryNode preorder traversal
    # BEFORE TESTING: implement preorder_traversal
    TEST_preorder(BT)

    # TEST 2 - Test BinaryNode postorder traversal
    # BEFORE TESTING: implement postorder_traversal
    TEST_postorder(BT)

    # TEST 3 - Test BinaryNode inorder traversal
    # BEFORE TESTING: implement inorder_traversal
    TEST_inorder(BT)

    # TEST 4 - Test docstrings
    # BEFORE TESTING: implement all docstrings
    TEST_docs(BT)


if __name__ == "__main__":
    os.system("cls")
    main()