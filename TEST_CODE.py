##### Global color variables #####
from colorama import Fore

R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
W = Fore.RESET
P = Fore.CYAN
Y = Fore.YELLOW

'''IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama'''


##################################

def result(flag):
    if flag:
        return f"{G}PASSED{W}"

    return f"{R}FAILED{W}"


def initialize(BT):
    a = BT.add_root("A")
    b = BT.add_left(a, "B")
    c = BT.add_right(a, "C")
    d = BT.add_left(b, "D")
    e = BT.add_right(b, "E")
    f = BT.add_left(e, "F")


def VIEW_tree():
    print("~" * 50)
    print(f"{P}This is what your tree will look\nlike for the next round of tests. {W}\n")

    print("""
            (A)
            / \\
          (B) (C)
          / \\ 
        (D) (E)
            /
          (F)

    """)
    print("~" * 50, "\n\n")


def TEST_preorder(BT):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Preorder Tree Traversal{W}\n")

    exp = ['A', 'B', 'D', 'E', 'F', 'C']
    order = BT.preorder_traversal()

    print(f"{B}Expected result of Preorder Traversal:{W} {exp}")
    print(f"{B}Actual result of Preorder Traversal:{Y} {order}{W}\n")

    test = type(order) == list
    print(f"Method returns a list: {result(test)}")

    test = order == exp
    print(f"Traversal result is correct: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_postorder(BT):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Postorder Tree Traversal{W}\n")

    exp = ['D', 'F', 'E', 'B', 'C', 'A']
    order = BT.postorder_traversal()

    print(f"{B}Expected result of Postorder Traversal:{W} {exp}")
    print(f"{B}Actual result of Postorder Traversal:{Y} {order}{W}\n")

    test = type(order) == list
    print(f"Method returns a list: {result(test)}")

    test = order == exp
    print(f"Traversal result is correct: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_inorder(BT):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Inorder Tree Traversal{W}\n")

    exp = ['D', 'B', 'F', 'E', 'A', 'C']
    order = BT.inorder_traversal()

    print(f"{B}Expected result of Inorder Traversal:{W} {exp}")
    print(f"{B}Actual result of Inorder Traversal:{Y} {order}{W}\n")

    test = type(order) == list
    print(f"Method returns a list: {result(test)}")

    test = order == exp
    print(f"Traversal result is correct: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_docs(BT):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Docstrings{W}\n")

    doc = BT.preorder_traversal.__doc__
    if doc != None:
        print(f"{B}preorder_traversal() Documentation:{W} {doc}\n")
    else:
        print(f"{R}preorder_traversal() Documentation Missing{W}\n")

    doc = BT.postorder_traversal.__doc__
    if doc != None:
        print(f"{B}postorder_traversal() Documentation:{W} {doc}\n")
    else:
        print(f"{R}postorder_traversal() Documentation Missing{W}\n")

    doc = BT.inorder_traversal.__doc__
    if doc != None:
        print(f"{B}inorder_traversal() Documentation:{W} {doc}\n")
    else:
        print(f"{R}inorder_traversal() Documentation Missing{W}\n")

    print("~" * 50, "\n\n")

# print(f":{result(test)}")