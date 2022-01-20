# binary_tree
This is a very simple package I made

installation
------------

To install just run this command in your terminal

pip install https://github.com/Zxython/binary_tree/archive/refs/heads/main.zip

updating
--------
to update run these three commands and anwser yes when asked to confirm deletion

pip uninstall binary_tree

pip install https://github.com/Zxython/binary_tree/archive/refs/heads/main.zip

pip --version
  
-----------------------------------------------------------------------
Alternative Installation
------------------------
1) download this as a zip file
2) navigate to the file in file explorer
3) copy the path to the zip file
4) It should look like this C:\Users\USER\Downloads\binary_tree-main.zip
5) in pycharm terminal type pip install C:\Users\USER\Downloads\binary_tree-main.zip

-----------------------------------------------------------------------

How to use
----------

to use this simply create a new project and type these two commands.
The help command should list the binary tree commands

from binary_tree.binary_tree import binary_tree as tree

tree.help.all()

--------------------------------------------------------------------------
Example Code
------------

from binary_tree.binary_tree import binary_tree as tree, optimizeList

my_tree = tree(optimizeList([1, 2, 3, 4, 5]))

my_tree = my_tree + 2

my_tree.sort()

print(my_tree)

my_tree.append([0, 6])

my_tree -= [3, 2]

my_tree -= -1

print(f"Tree: {my_tree}")

print(f"Mean: {my_tree.mean}")

print(f"Standard Deviation: {my_tree.standard_deviation}")

tree1, tree2 = my_tree.split()

print(tree1, tree2)
