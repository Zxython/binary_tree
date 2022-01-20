# binary_tree
This is a very simple package I made

To install just run this command in your terminal

pip install https://github.com/Zxython/binary_tree/archive/refs/heads/main.zip
  
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

from binary_tree.binary_tree import binary_tree as tree

my_tree = tree([1, 2, 3, 4, 5])

my_tree.append(3)

print(my_tree)

my_tree.append([0, 6])

my_tree -= 3

print(f"Tree: {my_tree}")

print(f"Mean: {my_tree.mean}")

print(f"Standard Deviation: {my_tree.standard_deviation}")
