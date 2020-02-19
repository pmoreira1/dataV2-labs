## Coding Best Practices

Extracted from the PEP-8 Agreement (https://realpython.com/python-pep8/)

### Naming:

**Variables:**
Use a lowercase single letter, word, or words. Separate words with underscores to improve readability.
`x, var, my_variable`

**Functions:**
Use a lowercase word or words. Separate words by underscores to improve readability.
`function, my_function`

**Class:**
Start each word with a capital letter. Do not separate words with underscores. This style is called camel case.	
`Model, MyClass`

**Method:**
Use a lowercase word or words. Separate words with underscores to improve readability.
`class_method, method`

**Constant:**
Use an uppercase single letter, word, or words. Separate words with underscores to improve readability.
`CONSTANT, MY_CONSTANT, MY_LONG_CONSTANT`

**Module:**
Use a short, lowercase word or words. Separate words with underscores to improve readability.
`module.py, my_module.py`

**Package:** Use a short, lowercase word or words. Do not separate words with underscores.
`package, mypackage`
		
		
### Code Layout:

**Surround top-level functions and classes with two blank lines**

**Surround method definitions inside classes with a single blank line**

**Use blank lines sparingly inside functions to show clear steps**

**Maximum Line Length and Line Breaking** - Try to maintain lines with a maximum of 78 characters

**Indentation** - Use of 4 consecutive spaces, using spaces instead of Tabs;


### Code Comments:

**Relevance** - Comments should not state the obvious, but the actual functionality of what's being commented. 

**Block Comments** - Use multiple lines to prevent exceeding the 72 characters. When using multiple lines maintain the indentation.

Example:

```
for i in range(0, 10):
    # Loop over i ten times and print out the value of i, followed by a
    # new line character
    print(i, '\n') 
```

**Inline comments** - Keep to bare minimum. Only if absolutely necessary.

