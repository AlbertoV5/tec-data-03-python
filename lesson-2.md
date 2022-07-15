|                      |
|--------------------- |
| [<<Back](./readme.md) |

Notes taken during class.


# Conditional Statements

Python requires indentation after the `:` operator, which means &ldquo;this is a block of code&rdquo;. So we can nest blocks with indentation.

```python
x = 1
if x == 1:
    print("x is equal to 1")
else:
    print("x is greater than 1")
```

```org
x is equal to 1
```

Most editors will render tabs as 4 spaces, most allow you to edit that setting.


## Logical Operators

```python
x = 1
y = 10
if x == 1 and y == 10:
    print("Both values are true.")
if x < 45 or y < 45:
    print("One or more statements are true.")
```

```org
Both values are true.
One or more statements are true.
```


## Nested and Elif

These are the possible ways to evaluate logic in Python:

|    |     |     |
|--- |---- |---- |
| If | Elif | Else |

You can have as many `Elif` instances as you want. You can check out the comparison operators in the python documentation. <sup><a id="fnr.1" class="footref" href="#fn.1" role="doc-backlink">1</a></sup>

```python
height = 66
age = 16
adult_permission = True
if (height > 70) and (age >= 18):
    print("Can ride all the roller coasters")
elif (height > 65) and (age >= 18):
    print("Can ride moderate roller coasters")
elif (height > 60) and (age >= 18):
    print("Can ride light roller coasters")
elif ((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50)):
    print("Can ride bumper cars")
else:
    print("Stick to lazy river")
```

```org
Can ride bumper cars
```


## Logical Matrices

| AND | T | F |
| T   | T | F |
| F   | F | F |

| OR | T | F |
| T  | T | T |
| F  | T | F |

`False` AND `anything` will always be `False`.

`True` AND `anything` will always be `True`.


# Activity Rock, Paper Scissors.

Let&rsquo;s play rock, paper scissors!

Assumming that.

```python
computer_choice = "r"
user_choice = "r"
```

Then we can use this nested conditional.

```python
print("Let's Play Rock Paper Scissors!")
options = ["r", "p", "s"]

if user_choice == "r":
    if computer_choice == "r":
        print("We Tie.")
    elif computer_choice == "p":
        print("You loose!")
    elif computer_choice == "s":
        print("You win!")
elif user_choice == "p":
    if computer_choice == "r":
        print("You win!")
    elif computer_choice == "p":
        print("We Tie.")
    elif computer_choice == "s":
        print("You loose!")
elif user_choice == "s":
    if computer_choice == "r":
        print("You loose!")
    elif computer_choice == "p":
        print("You win!")
    elif computer_choice == "s":
        print("We tie!")
else:
    print("Pick a valid choice!")

print(f"You chose {user_choice}. I chose {computer_choice}.")
```

```org
Let's Play Rock Paper Scissors!
We Tie.
You chose r. I chose r.
```

If we pick `"p"` and computer picks `"s"`.

```org
Let's Play Rock Paper Scissors!
You loose!
You chose p. I chose s.
```

If we pick `"s"` and computer picks `"p"`.

```org
Let's Play Rock Paper Scissors!
You win!
You chose s. I chose p.
```


# Loops

Python will only iterate over a list, so we can generate one list on the fly. Using the `range` keyword.

```python
for i in range(4):
    print(i)
```

```org
0
1
2
3
```

Or we can use our own list.

```python
person_list = ["Alex", "Bob", "Alice"]
for person in person_list:
    print(person)
```

```org
Alex
Bob
Alice
```

Python also supports While loops, which will keep running forever unless we stop it with one condition.

```python
run = 0
while run < 3:
    print(f"run! {run}")
    run = run + 1
```

```org
run! 0
run! 1
run! 2
```


# Activity Number Chain

Let&rsquo;s assume we can start with these values.

```python
user_play = "y"
saved_number = 0
user_number = 3
```

Then we can run the code.

```python
while user_play == "y":
    for i in range(1, user_number + 1):
        print(f"{i + saved_number}")
    saved_number = saved_number + user_number
    user_play = "n"
```

```org
1
2
3
```

Let&rsquo;s then assume we give it an input of `6`.

```org
4
5
6
7
8
9
```

We were able to continue the sequence because we stored the last number in the `saved_number` variable. We can do it one last time for the value of `5`.

```org
10
11
12
13
14
```


# Reading and Writing Files

Let&rsquo;s move to the working directory.

```shell
cd ./material/3-2-Student-Resources/09-Evr_WritingNetflixData
echo "---this is the path---"
pwd
echo "---these are the files in the path---"
ls
```

```org
---this is the path---
/Users/albertovaldez/tec-data/tec-data-03-python/material/3-2-Student-Resources/09-Evr_WritingNetflixData
---these are the files in the path---
README.md
Resources
Unsolved
output
solved_write_netflix.py
```

Let&rsquo;s assume we are looking for this video.

```python
video = "Breaking Bad"
```

We need to iterate over the rows of the file, the structure is something like:

`csvreader[rows[columns]]`

So we need a for loop and then use `[0]` to index the first column, which will be the &ldquo;title&rdquo;, as our file looks like:

| title        | rating      | ratinglevel                        | etc&#x2026; |
|------------ |----------- |---------------------------------- |----------- |
| White Chicks | PG-13       | &ldquo;crude and humour&rdquo;     | etc&#x2026; |
| Breaking Bad | TV-MA       | &ldquo;For mature audiences&rdquo; | etc&#x2026; |
| etc&#x2026;  | etc&#x2026; | etc&#x2026;                        | etc&#x2026; |

Let&rsquo;s use the `os` and `csv` modules in order to both read and write the files.

```python
import os
import csv

csvpath = os.path.join("resources", "netflix_ratings.csv")
outputpath = os.path.join("output", "video_result.txt")
found = False

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if row[0] == video:
            found = True
            with open(outputpath, "a") as textfile:
                # title, rating, ratinglevel
                contents = f"Title: {row[0]}, Rating Level: {row[1]} ({row[2]})\n"
                textfile.write(contents)
                print(contents)
            break
    if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")
```

```org
Title: Breaking Bad, Rating Level: TV-MA (For mature audiences.  May not be suitable for children 17 and under.)

```

Then our output file will look like this:

```shell
cat output/video_result.txt
```

```org
echo $?Title: Breaking Bad, Rating Level: TV-MA (For mature audiences.  May not be suitable for children 17 and under.)
```

Now let&rsquo;s try to find it using `video = Scream`.

```org
Title: Scream, Rating Level: TV-14 (Parents strongly cautioned. May be unsuitable for children ages 14 and under.)

```

Let&rsquo;s take a look at the file again.

```shell
cat output/video_result.txt
```

```org
echo $?Title: Breaking Bad, Rating Level: TV-MA (For mature audiences.  May not be suitable for children 17 and under.)
Title: Scream, Rating Level: TV-14 (Parents strongly cautioned. May be unsuitable for children ages 14 and under.)
```

Extra tip: We can empty the .txt file with this command.

```shell
> output/video_result.txt
```


# Office hours.

Make sure you are in the right directory!

## Footnotes

<sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> <https://docs.python.org/3/reference/expressions.html#comparisons>
