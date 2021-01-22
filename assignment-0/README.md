# num2words

num2words is a program written as part of a programming assignment by [thinkbridge](https://thinkbridge.com/), which takes in a currency value between 0 - 999999 (including up to 2 decimal places), and returns the text representation of that number.


## Examples

```python
n2w.num_to_words(11124)
# returns 'Rs. Eleven Thousand One Hundred And Twenty-Four ONLY'

n2w.num_to_words(123456.78)
# returns 'Rs. One Lakh Twenty Three Thousand Four Hundred And Fifty-Six 78/100 ONLY'
```

## Requirements

Python 3.x


## Usage
1) Clone repository using ```git clone https://github.com/blazyy/thinkbridge-programming-assignment```
2) Open PowerShell or cmd in the directory where the cloned files are.
3) For checking test cases, run ```python test_n2w.py```
4) For custom input, run ```python n2w_custom_input.py```

## Source Code
The main source code can be found in *[n2w.py](n2w.py)*
