def optimizeList(items):
    def opt(items, iteration=0):
        new_list = []
        if len(items) in [0, 1]:
            return items
        new_list.append(items[len(items) // 2])
        new_list.append(optimizeList(items[:len(items) // 2], iteration + 1))
        new_list.append(optimizeList(items[len(items) // 2 + 1:], iteration + 1))
        if iteration != 0:
            return new_list
        lst = []
        while new_list:
            x = new_list.pop(0)
            if type(x) == list:
                new_list.extend(x)
            else:
                lst.append(x)
        return lst
    return opt(items)

class binary_tree:
    class help:
        class functions:
            @staticmethod
            def append():
                print("tree.append(number): This will add number into the binary_tree called tree")

            @staticmethod
            def remove():
                print("tree.remove(number): This will remove number from the binary_tree called tree\n"
                      "(note): this will remove all of that number from the tree to only remove one of that number "
                      "use tree[number] -= 1")

            @staticmethod
            def sort():
                print("tree.sort(): This will reorganize the binary_tree called tree into the most efficient "
                      "tree it can create")

            @staticmethod
            def copy():
                print("tree.copy(): This will return a copy of the tree")

            @staticmethod
            def split():
                print("tree.split(): This will remove the top value in the binary tree and return the two"
                      "resulting trees created")

            @staticmethod
            def all():
                binary_tree.help.functions.append()
                print()
                binary_tree.help.functions.remove()
                print()
                binary_tree.help.functions.sort()
                print()
                binary_tree.help.functions.copy()
                print()
                binary_tree.help.functions.split()

        class properties:
            @staticmethod
            def list():
                print("tree.list: this will return a list representation of the binary_tree called tree")

            @staticmethod
            def mean():
                print("tree.mean: this will return the mean of the binary_tree called tree")

            @staticmethod
            def median():
                print("tree.median: this will return the median of the binary_tree called tree")

            @staticmethod
            def mode():
                print("tree.mode: this will return the mode of the binary_tree called tree")

            @staticmethod
            def range():
                print("tree.range: this will return the range of the binary_tree called tree")

            @staticmethod
            def standard_deviation():
                print("tree.standard_deviation: this will return the standard deviation of the binary_tree called tree")

            @staticmethod
            def all():
                binary_tree.help.properties.list()
                print()
                binary_tree.help.properties.mean()
                print()
                binary_tree.help.properties.median()
                print()
                binary_tree.help.properties.mode()
                print()
                binary_tree.help.properties.range()
                print()
                binary_tree.help.properties.standard_deviation()
                print()

        class methods:
            @staticmethod
            def getitem():
                print("tree[number]: this will get the amount of times that number is the the binary_tree called tree")

            @staticmethod
            def setitem():
                print("tree[number] = amount: this will set the amount of times that number is the the binary_tree"
                      " called tree\n (note) this will do nothing if the amount is negative, and will delete the "
                      "number from the tree if the amount is 0")

            @staticmethod
            def add():
                print("tree + number OR tree + list:this will add the number or list values to the tree and return "
                      "a binary tree")

            @staticmethod
            def subtract():
                print("tree - number OR tree - list:this will remove one amount of the number or list values from"
                      " the tree and return a binary tree")

            @staticmethod
            def plus_add():
                print("tree += number OR tree += list:this will add the number or list values to the tree")

            @staticmethod
            def plus_subtract():
                print("tree -= number OR tree -= list:this will remove one amount of the number or list values from"
                      " the tree")

            @staticmethod
            def equals():
                print("tree == (list, int, float, tuple, binary_tree):"
                      "This will return True if the tree contains the items from the list, int, float, tuple, or "
                      "binary_tree\n(note) since a binary_tree has no order the order does not matter")

            @staticmethod
            def not_equals():
                print("tree != (list, int, float, tuple, binary_tree):"
                      "This will return False if the tree contains the items from the list, int, float, tuple, or "
                      "binary_tree\n(note) since a binary_tree has no order the order does not matter")

            @staticmethod
            def contains():
                print("number in tree: This will return True if the number exists in the tree")

            @staticmethod
            def iter():
                print("for x in tree OR iter(tree): This will iterate through the values in the tree")

            @staticmethod
            def print():
                print("print(tree): This print out a list representation of the tree")

            @staticmethod
            def len():
                print("len(tree): This returns the amount of items in the tree")

            @staticmethod
            def min():
                print("min(tree): This returns the smallest value in the tree")

            @staticmethod
            def max():
                print("max(tree): This returns the highest value in the tree")

            @staticmethod
            def sum():
                print("sum(tree): This returns the sum of all the elements in the tree")

            @staticmethod
            def all():
                binary_tree.help.methods.getitem()
                print()
                binary_tree.help.methods.setitem()
                print()
                binary_tree.help.methods.add()
                print()
                binary_tree.help.methods.subtract()
                print()
                binary_tree.help.methods.plus_add()
                print()
                binary_tree.help.methods.plus_subtract()
                print()
                binary_tree.help.methods.equals()
                print()
                binary_tree.help.methods.not_equals()
                print()
                binary_tree.help.methods.contains()
                print()
                binary_tree.help.methods.iter()
                print()
                binary_tree.help.methods.print()
                print()
                binary_tree.help.methods.len()
                print()
                binary_tree.help.methods.min()
                print()
                binary_tree.help.methods.max()
                print()
                binary_tree.help.methods.sum()

        @staticmethod
        def creating_binary_tree():
            print("Creating a tree: ____ = binary_tree()\nYou can put a list inside the parenthesis to create a binary tree with those "
                  "numbers")

        @staticmethod
        def help():
            print("""List of functions:
-------------------
append(number)
remove(number)
sort()
copy()

List of properties:
-------------------
list
mean
media
mode
range
standard_deviation

List of methods:
-------------------
[] (aka getitem)
[] = number (aka setitem)
+ (aka add)
- (aka subtract)
+= (aka plus_add)
-= (aka plus_subtract)
== (aka equals)
!= (aka not_equals)
number in ____ (aka contains)
for x in ____ (aka iter)
iter()
print()
len()
max()
min()
sum()""")

        @staticmethod
        def all():
            binary_tree.help.creating_binary_tree()
            print("\n")
            binary_tree.help.functions.all()
            print("\n")
            binary_tree.help.properties.all()
            print("\n")
            binary_tree.help.methods.all()

    class Node:
        def __init__(self, data, parent=None, duplicates = 0):
            self.left = None
            self.right = None
            self.data = data
            self.parent = parent
            self.amount = duplicates + 1

    def __init__(self, data=None):
        self.binary_tree = None
        self.list = []
        if data is None:
            return
        for datum in data:
            binary_tree.append(self, datum)

    def append(self, item):
        if type(item) is list:
            for x in item:
                self.append(x)
            return
        if self.binary_tree is None:
            self.binary_tree = binary_tree.Node(item)
            self.list = [item]
            return
        self.binary_tree = binary_tree.__add(self.binary_tree, item)
        self.list.append(item)

    def remove(self, item):
        while item in self.list:
            self.list.remove(item)
        self.binary_tree = binary_tree.__remove(self.binary_tree, item)

    def sort(self):
        self.list = self.__sort()
        lst = self.__optimizeList(self.list)
        self.binary_tree = None
        self.list = None
        self.append(lst)

    def copy(self):
        return binary_tree(self)

    def split(self):
        tree1 = binary_tree()
        tree2 = binary_tree()
        for x in self.list:
            if x < self.binary_tree.data: tree1.append(x); continue
            if x > self.binary_tree.data: tree2.append(x)
        return tree1, tree2

    @property
    def mean(self):
        return sum(self.list) / len(self.list)

    @property
    def median(self):
        temp = self.list
        temp.sort()
        index = len(temp)
        if index % 2 == 0:
            return temp[index // 2]
        return temp[index // 2], temp[index // 2 + 1]

    @property
    def mode(self):
        return max(set(self.list), key=self.list.count)

    @property
    def range(self):
        return max(self.list) - min(self.list)

    @property
    def standard_deviation(self):
        mean = self.mean
        sum = 0
        for x in self.list:
            sum += abs(x - mean) ** 2
        return (sum / len(self.list)) ** 0.5

    def __sort(self):
        temp = [None]
        tree = self.binary_tree
        done = False
        while not done:
            while tree.left is not None: tree = tree.left
            if temp[-1] != tree.data:
                for x in range(tree.amount): temp.append(tree.data)
            if tree.right is None:
                while tree.left is None:
                    if tree.parent is None: done = True; break
                    if tree.parent.right == tree: tree.parent.right = None; tree = tree.parent; continue
                    tree = tree.parent; tree.left = None; temp.append(tree.data); break
            if tree.right is not None: tree = tree.right
        temp.pop(0)
        return temp

    @staticmethod
    def __optimizeList(items, iteration=0):
        new_list = []
        if len(items) in [0, 1]:
            return items
        new_list.append(items[len(items) // 2])
        new_list.append(binary_tree.__optimizeList(items[:len(items) // 2], iteration + 1))
        new_list.append(binary_tree.__optimizeList(items[len(items) // 2 + 1:], iteration + 1))
        if iteration != 0:
            return new_list
        lst = []
        while new_list:
            x = new_list.pop(0)
            if type(x) == list:
                new_list.extend(x)
            else:
                lst.append(x)
        return lst

    @staticmethod
    def __search(tree, item):
        while 1:
            if tree.data < item:
                if tree.right is None: tree.right = binary_tree.Node(item, tree); return False
                tree = tree.right; continue
            if tree.data > item:
                if tree.left is None: tree.left = binary_tree.Node(item, tree); return False
                tree = tree.left; continue
            return tree.amount

    @staticmethod
    def __setAmount(tree, item, amount):
        while 1:
            if tree.data < item:
                if tree.right is None: tree.right = binary_tree.Node(item, tree); return False
                tree = tree.right
                continue
            if tree.data > item:
                if tree.left is None: tree.left = binary_tree.Node(item, tree); return False
                tree = tree.left
                continue
            tree.amount = amount; return

    @staticmethod
    def __add(tree, item):
        while 1:
            if tree.data < item:
                if tree.right is None: tree.right = binary_tree.Node(item, tree); break
                tree = tree.right; continue
            if tree.data > item:
                if tree.left is None: tree.left = binary_tree.Node(item, tree); break
                tree = tree.left; continue
            tree.amount += 1; break
        while tree.parent is not None: tree = tree.parent
        return tree

    @staticmethod
    def __remove(tree, item):
        while True:
            if tree.data < item:
                if tree.right is None: break
                tree = tree.right; continue
            if tree.data > item:
                if tree.left is None: break
                tree = tree.left; continue
            if tree.left is None and tree.right is None:
                if tree.parent.left is not None: tree.parent.left = None; tree = tree.parent; break
                tree.parent.right.amount = None; tree = tree.parent; break
            if (tree.left is not None and tree.right is not None) or (tree.left is None): tree.right.parent = tree.parent; tree.parent.right = tree.right; break
            tree.left.parent = tree.parent; tree.parent.left = tree.left; break
        while tree.parent is not None: tree = tree.parent
        return tree

    def __contains__(self, item):
        return binary_tree.__search(self.binary_tree, item)

    def __getitem__(self, key):
        return binary_tree.__search(self.binary_tree, key)

    def __setitem__(self, key, value):
        if value - self.list.count(key) == 0 or value < 0:
            return
        for x in range(value - self.list.count(key)):
            self.list.append(key)
        for x in range(self.list.count(key) - value):
            self.list.remove(key)
        binary_tree.__setAmount(self.binary_tree, key, value)

    def __iter__(self):
        for x in self.list:
            yield x

    def __str__(self):
        return str(self.list)

    def __add__(self, other):
        if type(other) in [list, tuple]:
            return binary_tree(self.list + other)
        if type(other) in [int, float]:
            return binary_tree(self.list + [other])
        if type(other) is binary_tree:
            return binary_tree(self.list + other.list)

    def __sub__(self, other):
        if type(other) in [list, tuple, binary_tree]:
            for x in other:
                self.__sub__(x)
        if type(other) in [int, float]:
            if other in self:
                self.list.remove(other)
                return binary_tree(self.list)
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __len__(self):
        return len(self.list)

    def __eq__(self, other):
        if type(other) in [list, tuple, binary_tree]:
            temp = self.list.copy()
            for x in list(other):
                if x not in temp:
                    return False
                temp.remove(x)
            if len(other) != len(self):
                return False
            return True
        if type(other) in [float, int]:
            if len(self) == 1 and self.list[0] == other:
                return True
        return False

    def __ne__(self, other):
        return not binary_tree.__eq__(self, other)
