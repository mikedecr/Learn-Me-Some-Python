# ----------------------------------------------------
#   SSC Data Wrangling
#   chapter 2: data frames
# ----------------------------------------------------

import pandas as pd
from pathlib import Path


# ---- data frame basics -----------------------

# pd.DataFrame() has different ways to supply data
# we will do data = column by column

# assigning
df = pd.DataFrame(
    data = {
      "A": [1, 2, 3, 4, 5], 
      "B": [5, 4, 3, 2, 1] 
    }
)


# attributes
type(df)  # class
df.shape  # dims (as an attribute of object)
df.dtypes # data types


# working with data frames
df.head()
df.head

help(df.head)  # learn more
df.head(n = 3) # n = argument


# ---- from file -----------------------

# args to read_csv():
# - header: boolean, does first row of the data contains the variable names 
# - skiprows: number of lines at the front of the file to be ignored
# - na_values: list of characters that indicate missing data

# regular file path also works, but this looks {here}-ish!
chile = pd.read_csv(Path() / "data" / "Chile.csv")

chile.shape
chile.dtypes
chile.head


# ---- nastier data -----------------------

# this has a header of metadata
attnd = pd.read_csv(Path() / "data" / "attendance.csv")

# which is why it looks dopey
attnd.head
attnd.head()
attnd.shape

attnd[:][0:1]

# skip top row
attnd = pd.read_csv(
    Path() / "data" / "attendance.csv", 
    skiprows = 2, 
    header = 0
)

attnd.head()

# if I had an IDE this would apparently look better formatted
attnd.head().to_string()



# ---- Missing data -----------------------

# some characters are used to delineate what's missing
attnd.iloc[9:13, 13:15]

# read with NA codes
attnd = pd.read_csv(
  Path() / "data" / "attendance.csv", 
  skiprows = 2, 
  keep_default_na = True, 
  na_values = ['?', '(?)']
)

# now NaN (what if a string though?)
attnd.iloc[9:13, 13:15]


attnd.dtypes


# ---- troubleshooting errors while reading -----------------------

# you can specify variable names with `names` argument
# doing head at the same time
pd.read_csv(
  Path() / "data" / "attendance.csv", 
  names = ["a", "b", "c", "d"], 
  nrows = 25
).head()

# read rows as columns, sep = "^"
pd.read_csv(
  Path() / "data" / "attendance.csv", 
  sep = "^", 
  nrows = 15
).head()


# ---- exercises -----------------------

# 1. Import the "amis.csv" data set.
# we his error
pd.read_csv(Path() / "data" / "amis.csv")

# 2. Are there any rows that need to be ignored in the amis data set? If so, modify your import to account for them.

# read rows into one column
pd.read_csv(Path() / "data" / "amis.csv",
            sep = "^")

# print first 20 rows
pd.read_csv(Path() / "data" / "amis.csv",
            sep = "^")[0:20]

# skip first 10 rows
amis = pd.read_csv(Path() / "data" / "amis.csv", skiprows = 10)


# 3. Are there any special symbols that need to be set to missing in the amis data set? If so, modify your import to account for them.

# everything reads as an integer so I don't think so?
amis.dtypes


# 4. Import the "mifem.csv" data set.
mifem_path = Path() / "data" / "mifem.csv"
mifem = pd.read_csv(mifem_path)


# 5. Is there any meta data at the top or bottom of the mifem data set? You will need to determine how to view the bottom of a data set. If so, modify your import to account for them.

mifem
# no this looks OK?

# 6. Are there any special symbols that need to be set to missing in the mifem data set? If so, modify your import to account for them.

# kinda stupid to ask about this kind of stuff without showing how to tabulate variables but OK.
# I guess you just use the codebook and infer that the "nk" values are supposed to be implicitly missing.
# also let empty strings be missing

mifem = pd.read_csv(mifem_path,  na_values = ["", "nk"])




