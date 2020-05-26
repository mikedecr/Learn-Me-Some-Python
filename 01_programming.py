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



