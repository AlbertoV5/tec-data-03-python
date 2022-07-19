|                                                |                          |                          |                                      |
|----------------------------------------------- |------------------------- |------------------------- |------------------------------------- |
| [<<<Home](https://albertov5.github.io/tec-data) | [Lesson-1](./lesson-1.md) | [Lesson-2](./lesson-2.md) | [Challenge>>>](./challenge/readme.md) |


# Introduction

Python is one of the most popular languages in the world, used in many industries to accomplish different goals. It&rsquo;s very easy to use, as you can focus on the problem and not the intricacies of the language.

Here is a YouTube playlist of keynotes that I&rsquo;ve collected over the past month while practicing and studying Python:

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PLdswL3Tb01gznKrZf0_XeOc6ftUO3yZhn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---


## Git

Version control tool that will allow us to interact with GitHub from the Terminal.

Installing homebrew

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

Installing git

`brew install git`

`brew install git-lfs`

Checking versions

```shell
git --version
```

    git version 2.24.3 (Apple Git-128)

```shell
git-lfs --version
```

    git-lfs/3.2.0 (GitHub; darwin amd64; go 1.18.2)


# Python

We can check the version with:

```shell
python --version
```

    Python 3.7.13

We can run an interactive Python REPL from the terminal with:

```shell
python
```


## Python versions - End of life

[End of life](https://endoflife.date/python) is a website that shows the dates of when a Python version is not longer receiving security updates. For example:

| Version | Released    | End of life |
|------- |----------- |----------- |
| 3.7     | 26 Jun 2018 | 27 Jun 2023 |
| 2.7     | 03 Jul 2020 | 01 Jan 2020 |

The Python version is best chosen depending on the libraries you are planning on using, and most of the time the better supported versions are the ones released 2+ years ago.


# Working with Python files


## Creating a file from the Terminal

Let&rsquo;s list our working directory.

```shell
ls
```

    LICENSE
    challenge
    index.html
    lesson-1.html
    lesson-1.md
    lesson-1.org
    lesson-2.html
    lesson-2.md
    lesson-2.org
    publish.inc
    readme.html
    readme.md
    readme.org
    resources

We can create a new Python file in the resources directory.

```shell
touch resources/hello_world.py
```


## Editing a file

Start working in the current directory.

```shell
code .
```

We can use `Shift+P` in VS Code to open a file. Then find out `hello_world.py` file and input some Python code.

```python
print("Hello Wold!")
```

In VSCode we can use `Shift-Cmd-P` and search for the `Python: Select Interpreter` command to make sure we are working with the Python version we want to work with.


## Running a file

```shell
python resources/hello_world.py
```

    Hello World!


# Python Types

Determining the type of a variable or constant.

```python
print(type(2019))
print(type(73.81))
print(type("hello"))
print(type(""))
print(type(None))
print(type(False))
```

    <class 'int'>
    <class 'float'>
    <class 'str'>
    <class 'str'>
    <class 'NoneType'>
    <class 'bool'>

| Data Type           | Python Classification       |
|------------------- |--------------------------- |
| Integers            | <class &rsquo;int&rsquo;>   |
| Float point numbers | <class &rsquo;float&rsquo;> |
| Strings             | <class &rsquo;str&rsquo;>   |
| Boolean             | <class &rsquo;bool&rsquo;>  |


## Creating a variable

```python
num_candidates = 3
winning_percentage = 73.81
candidate = "Diane"
won_election = True
```

There are a few naming conventions in Python, for example using snake case for variables <sup><a id="fnr.1" class="footref" href="#fn.1" role="doc-backlink">1</a></sup> or general style guides like PEP 8 <sup><a id="fnr.2" class="footref" href="#fn.2" role="doc-backlink">2</a></sup>.


## Keywords

```python
help("keywords")
```

```org

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

```


## Python Operations

| Operator | Meaning                                                                                                                                  | Use                       |
|-------- |---------------------------------------------------------------------------------------------------------------------------------------- |------------------------- |
| +        | Adds two numbers.                                                                                                                        | x + y                     |
| –        | Subtracts one number from another.                                                                                                       | x – y                     |
| \*       | Multiplies two numbers.                                                                                                                  | x \* y                    |
| %        | The “%” is known as the modulus When used in place of “/” it will divide one number by another and return the remainder of the division. | x % y (remainder of x/y)  |
| //       | Divides one number by another and returns an integer. This is known as floor division.                                                   | x // y                    |
| \*\*     | Raises a number to a power.                                                                                                              | x\*\*y (x to the power y) |

Order of operations must follow the order of precedence of mathematics.

```python
print(5 + 2 * 3)
print(8 // 5 - 3)
print(8 + 22 * 2 - 4)
print(16 - 3 / 2 + 7 - 1)
print(3 ** 3 % 5)
print(5 + 9 * 3 / 2 - 4)
```

    11
    -2
    48
    20.5
    2
    14.5

```python
print((5 + 2) * 3)
print((8 //5) - 3)
print((8 + (22 * (2 - 4))))
print(16 - 3 / (2 + 7) - 1)
print(3 ** (3 % 5))
```

    21
    -2
    -36
    14.666666666666666
    27

```python
print(5 + (9 * 3 / 2 - 4))
print(5 + (9 * 3 / (2 - 4)))
```

    14.5
    -8.5


# Python Lists

A list is an array that contains multiple data items.

```python
counties = ["Arapahoe", "Denver", "Jefferson"]
print("This is the list:", counties)
print("This is the first item:", counties[0])
print("This is the last item:", counties[-1])
print("This is the length of the list:", len(counties))
print("This is a slice of the list:", counties[0:2])
print("This is other way to slice:", counties[:2])
```

    This is the list: ['Arapahoe', 'Denver', 'Jefferson']
    This is the first item: Arapahoe
    This is the last item: Jefferson
    This is the length of the list: 3
    This is a slice of the list: ['Arapahoe', 'Denver']
    This is other way to slice: ['Arapahoe', 'Denver']

Appending items to a list.

```python
counties = ["Arapahoe", "Denver", "Jefferson"]
counties.append("El Paso")
counties.insert(2, "El Paso")
print("We added El Paso twice to the list.")
print(counties)
counties.remove("El Paso")
print("We removed the first instance of El Paso.")
print(counties)
counties.pop(-1)
print("We removed the last element in the list.")
print(counties)
```

    We added El Paso twice to the list.
    ['Arapahoe', 'Denver', 'El Paso', 'Jefferson', 'El Paso']
    We removed the first instance of El Paso.
    ['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
    We removed the last element in the list.
    ['Arapahoe', 'Denver', 'Jefferson']

Changing elements from a list.

```python
counties = ["Arapahoe", "Denver", "Jefferson"]
counties[2] = "El Paso"
print("We replace index at 2 with El Paso.")
print(counties)
```

    We replace index at 2 with El Paso.
    ['Arapahoe', 'Denver', 'El Paso']

Let&rsquo;s try it all together.

```python
counties = ["Arapahoe", "Denver", "Jefferson"]
counties.insert(1, "El Paso")
counties.remove("Arapahoe")
jefferson = counties[2]
counties[2] = counties[1]
counties[1] = jefferson
counties.append("Arapahoe")
print(counties)
```

    ['El Paso', 'Jefferson', 'Denver', 'Arapahoe']


# Python Tuples

Tuples are immutable data structures that contain one or more items.

```python
counties = ("Arapahoe", "Denver", "Jefferson")
print(counties[:-1])
```

    ('Arapahoe', 'Denver')


# Python Dictionaries

A dictionary is an object that stores a collection of data. It has a key and a value (key-value pairs).

```python
counties = {}
counties["Arapahoe"] = 422829
print(counties)
counties["Denver"] = 463353
counties["Jefferson"] = 432438
print(counties)
print(counties.keys())
print(counties.values())
print(counties.get("Denver"))
```

    {'Arapahoe': 422829}
    {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
    dict_keys(['Arapahoe', 'Denver', 'Jefferson'])
    dict_values([422829, 463353, 432438])
    463353

List of dictionaries.

```python
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters":422829})
voting_data.append({"county":"Denver", "registered_voters":463353})
voting_data.append({"county":"Jefferson", "registered_voters":432438})
print(voting_data)
```

    [{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]

The previous dictionary is the equivalent of this table.

| county    | registered<sub>voters</sub> |
|--------- |--------------------------- |
| Arapahoe  | 422829                      |
| Denver    | 463353                      |
| Jefferson | 432438                      |

```python
voting_data = [{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]

voting_data.insert(1, {"county":"El Paso", "registered_voters":461149})
arapahoe = voting_data.pop(0)
denver = voting_data[1]
jefferson = voting_data[2]
voting_data[2] = denver
voting_data[1] = jefferson
voting_data.append(arapahoe)
print(voting_data)
```

    [{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Arapahoe', 'registered_voters': 422829}]

For more info on dictionaries and built-in Python functions, we can go to the documentation <sup><a id="fnr.3" class="footref" href="#fn.3" role="doc-backlink">3</a></sup>.


# Decision Statements

If statements represent different paths in a flow chart. Where if the statement is true, false or equal, we proceed with the following block of code.

```python
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])
```

    Denver

```python
temperature = 79
if temperature > 80:
    print("Hot")
else:
    print("Not so hot.")
```

    Not so hot.


## Nested if statements

```python
score = 85
if score >= 90:
    print("Your grade is A")
else:
    if score >= 80:
        print("Your grade is B")
    else:
        ...
```

    Your grade is B


## Elif

```python
score = 90
if score >= 90:
    print("Grade is A")
elif score >= 80:
    print("Grade is B")
elif score >= 70:
    print("Grade is C")
else:
    ...
```

    Grade is A


## Logical Operators

```python
counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list.")
else:
    print("El Paso is not in the list.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Both in list.")
else:
    print("Either one is not in the list.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("One of them in the list.")
else:
    print("None of them in the list.")

 if "Arapahoe" in counties and "El Paso" not in counties:
    print("Arpahoe is but El Paso isn't.")
else:
    ...

```


# Loops

A single instruction that is repeated multiple times.

```python
x = 0
while x <= 3:
    print(x)
    x += 1
```

    0
    1
    2
    3

```python
numbers = [0, 1, 2, 3]
for number in numbers:
    print(number)

print("Now with a range.")
for n in range(4):
    print(n)

num_dict = {"a":0, "b":1, "c":2, "d":3}
print("Now over dict keys.")
for k in num_dict:
    print(k, num_dict[k])
```

    0
    1
    2
    3
    Now with a range.
    0
    1
    2
    3
    Now over dict keys.
    a 0
    b 1
    c 2
    d 3


## Iterating over Dictionaries

```python
data = [{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
for i in range(len(data)):
    print(data[i]["county"])
    print(data[i]["registered_voters"])
```

    Arapahoe
    422829
    Denver
    463353
    Jefferson
    432438


# F-Strings and Printing

Printing with f-strings

```python
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")
```

    Arapahoe county has 369237 registered voters
    Denver county has 413229 registered voters
    Jefferson county has 390222 registered voters

Point decimals formatting1.

```python
candidate_votes = 313123
total_votes = 1203920
print(f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
```

    You received 26.01% of the total votes.

## Footnotes

<sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> <https://en.wikipedia.org/wiki/Snake_case>

<sup><a id="fn.2" class="footnum" href="#fnr.2">2</a></sup> <https://peps.python.org/pep-0008/>

<sup><a id="fn.3" class="footnum" href="#fnr.3">3</a></sup> <https://docs.python.org/3.7/library/functions.html>
