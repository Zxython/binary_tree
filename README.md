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
Binary Tree Example Code
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


Engineering Tools Example Code
------------------------------

from binary_tree.engineering_tools import *

H = variable("H = 2.00 +- 0.03")

h = variable("h = 0.88 +- 0.04")

Q = uncertainty(H - h, H, h)

print(f"Q = {Q[0]} +- {Q[1]}")

print()

d = variable("d = 120 +- 3")

t = variable("t = 20 +- 1.2")

v = uncertainty(d / t, d, t)

print(f"V = {v[0]} +- {v[1]}")

print()

theta = variable(["θ", deg_to_rad(20), deg_to_rad(3)])

u = uncertainty(cos(theta), theta)

print(f"cos(θ) = {round(u[0], 2)} +- {round(u[1], 2)}")

print()

z = variable("z = 3 +- 0.1")

p = variable("p = 1000 +- 5")

p0 = variable("p0 = 101325 +- 1000")

g = 9.8

pz = uncertainty(p0 + p * g * z, z, p0, p)

print(f"p(z) = {round(pz[0])} +- {round(pz[1])}")

print()

x = variable(['x', None, None])

y = variable(['y', None, None])

z = variable(['z', None, None])

equation1 = uncertainty(x ** 2 * y * z ** 3 + x * y ** 3 * z ** 2, x, y, z, equation=True)

print(f"∂g/∂x = {equation1[0]}")

print(f"∂g/∂y = {equation1[1]}")

print(f"∂g/∂z = {equation1[2]}")

print()

equation2 = uncertainty(x ** 2 * y - x * y ** 2, x, y, equation=True)

print(f"δq = sqrt(({equation2[0]}) ** 2 * δx ** 2 + ({equation2[1]}) ** 2 * δy ** 2)")
