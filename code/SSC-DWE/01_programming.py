# ----------------------------------------------------
#   SSC Data Wrangling
#   chapter 1: programming
# ----------------------------------------------------

# ---- basics -----------------------

# assignment & implied print
a = 4
a


# line-breaking
(3 + 9) / 2

(3 + 9) / \
2


# ---- paths -----------------------

import os

# output as string
os.getcwd()

# printed output in the open
print(os.getcwd())


# ---- functions and methods -----------------------

# functions
round(5 / 3, ndigits = 5)

# methods
# in R: function.class()
# in python: class.method() and called more explicitly

# always call functions in a pkg as alias.function()
import pandas as pd

# read the documentation for pd.read_csv
docs_url = "https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html"

read_csv_docs = pd.read_csv(
  docs_url, 
  sep=', ', 
  delimiter = None, 
  header = 'infer', 
  names = None, 
  index_col = None, 
  usecols = None, 
  squeeze = False, 
  prefix = None
)

read_csv_docs


# ---- exercises -----------------------

# make a list
my_list = [1, 2, "a", list, pd]

my_list

# delete it
del my_list

my_list


# ----------------------------------------------------
#   extras
# ----------------------------------------------------

# ---- https://www.programiz.com/python-programming/list ---------

my_list = ['p', 'r', 'o', 'b', 'e']

# zero indexed!
my_list[0]
my_list[1]

# nested lists
n_list = ["hello", [2, 0, 1, 5]]

# indexing a nested list
n_list[0][0]
n_list[0][3]
n_list[1][1]

# honestly a little weirded out that each character is indexed



# negative indexing goes from reverse
my_list[-1]

# index by vector.
# in this example, 3 means third, and not 0 + 3?
my_list[0:3]

# which is why this is length 1 and 4
my_list[0:1]
my_list[0:4]

# from beginning, to end
my_list[ :4]
my_list[3: ]
my_list[ : ] # lol ok

# assign into list
my_list[0] = "hello"

my_list

