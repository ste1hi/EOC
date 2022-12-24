# About this program
This is a program to remind teacher to finish the class.
# Download
[Download it.](./alarm/download)
# Use
It's quite simple to use it.
## Basic use
There must be the `csv` file named after the abbreviation of the 
week in the same folder as the main program.In the `csv` file, the
first column is subject, the next three columns are the time of class
beginning, the last three columns are the time of class over. [For 
example](./Mon.csv).

The button of `准时下课` is refresh the time of class over.It will
find next class over time that is not reached.
## Advanced usage
If you want to change the character displayed, you can look up
the following form to find where you should change.

The class has not finished yet.

| object          | object name | position |
| :-------------: | :---------: | :------: |
|the present time | label       | None     |
|the time of class over| label_2| None     |
| time remaining | label_3|[main.py](./main.py)  line 61|
|sentence|label_4|[main.py](./main.py)  line 60|
|now lesson|label_5|None|
|lesson|now_subject|csv file first line|

The class has finished.

| object          | object name | position |
| :-------------: | :---------: | :------: |
|the present time | label       | None     |
|the time of class over| label_2| None     |
| time remaining | label_3|[main.py](./main.py)  line 57|
|sentence|label_4|[main.py](./main.py)  line 50|
|now lesson|label_5|None|
|lesson|now_subject|[main.py](./main.py)  line 55|

Ps. "None" means don't recommend changing, but if you 
really want to change, you can [visit](./alarm/Dialog.py) `Dialog.py retranslateUi()`method or use
`OBJECT_NAME.setText()`method.
# Warning
This program has not exception handling.So if today is Monday and `Mon.csv` not exist or
all class of today has finished, the program will exit with exit code -1.
# Contribution
This is not a formal project.You can pull request anything you want.But I strongly recommend 
you to submit an issue before writing code.
# License
Copyright ste1hi, 2022.

Distributed under the terms of the [MIT License](./LICENSE).
