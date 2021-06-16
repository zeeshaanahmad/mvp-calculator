# MVP Calculator

The script uses pandas data frame to find Most Valuable Player from matches data. It also validates if the data follows the correct formatting.

# Requirement

Python 3.6 above
Pandas

```
$ pip install pandas
```

# Run

```
$ python main.py
```

# Test invalid input

In `main.py`, uncomment lines 5, 6 and comment lines 10 and 11 and run `main.py` again using `python main.py`

# How to modify input data?

In metadata.py, you can find `input_data` and `invalid_input_data` variables. You can modify the data and follow above instructions to test.

# Known issues

Code still needs refactoring to make it more generic in order to handle any additional game types in future.