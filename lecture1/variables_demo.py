"""Python variables: names, objects, identity, and mutability (Lecture 1)."""

print("== Assignment styles ==")
name = "rover"  # Standard assignment
x = y = 10  # Chained: two names, one object
robot, speed_mps, battery_pct = "rover", 0.5, 87  # Unpacking
a, b = 1, 2
a, b = b, a  # Swap, no temporary variable
print(name, x, y, robot, speed_mps, battery_pct, a, b)

print("== Object types ==")
count = 10
ratio = 3.14
word = "hello"
print(type(count))  # <class 'int'>
print(type(ratio))  # <class 'float'>
print(type(word))  # <class 'str'>
print(type(print))  # <class 'builtin_function_or_method'>

print("== The id() function ==")
a = 10
b = 10.5
c = "hello"
print(id(a))
print(id(b))
print(id(c))
print(id(10))  # Same as id(a)?
print(id("hello"))  # Same as id(c)?

print("== Dynamic typing ==")
x = "hello"
print(type(x))  # <class 'str'>
x = 10.5
print(type(x))  # <class 'float'>

print("== Immutability and mutability ==")
x = 10
print(id(x))
x = x + 1  # New object created
print(id(x))  # Different from the line above

my_list = [1, 2, 3]
print(id(my_list))
my_list.append(4)  # Same object
print(id(my_list))  # Same as the line above

print("== Aliasing ==")
a = [1, 2, 3]
b = a  # b refers to the same list
print(id(a))
print(id(b))  # Same as id(a)
print(a is b)  # True
b.append(4)
print(a)  # [1, 2, 3, 4]: a changed too

print("== The None object ==")
result = None  # A name with no value yet
print(result)


def greet(name):
    print(f"Hello, {name}")


x = greet("Alice")  # Prints "Hello, Alice"
print(x)  # None
print(type(x))  # <class 'NoneType'>

print("== is versus == ==")
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)  # True: same values
print(a is b)  # False: different objects
print(a is c)  # True: same object

print("== The print() function ==")
print("Hello")
print(3)
print(2.4)
print(2 + 3)
print("*" * 10)
print("Welcome", "to", "ENPM", 605)
print("a", "b", "c", sep="-")
print("No newline", end="")
print()
