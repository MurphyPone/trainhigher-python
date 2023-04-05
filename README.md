# trainhigher-python
Introductory Programming in Python Course

This course aims to cover several basic concepts for Python 3 including the following:

## 0. Working in REPL / Notebook 
- Read-Eval–Print loop

## 1. Basic Anatomy of a Program

- Python is an interpreted language as opposed to a compiled language
  - This means that the file/files comprising the whole program are only ever examined or _run_ at _runtime_ when those lines of code are being executed
  - This makes it popular for scripting since it's easy and fast to write, but it also means that the language will hide a lot of the "hairy" bits of the language from you by default, abstracting away lots of "hard programming" concepts so you can focus on _just the thing it is that you want to do_
  - A compiled language necessarily has more boilerplate/mental overhead (namely, memory management and strong types) – this lets us bake more rules into the way that our program is run and flush out errors at _compile time_ rather than runtime.  E.g. "this variable needs to be a number, but the expression you gave it evaluates to a string, that's going to be an error and I as the wise compiler can tell you this before you even run the program"
    - Python, as an interpreted language, does not have a compilation step to catch such errors.  You just _run the program_ and see what happens.  So, there's some tradeoffs
- **Variables** - store data, maintain "state" in our program
  - In general, variables can be "mutable" or "immutable" (meaning constant, or non-variable)
  - Python is mutability-agnostic, and doesn't really model immutability that much, just a programming paradigm you should be aware of
- **Expressions** - some group of operations on some data that evaluates into a single value (or collection of values) that we can bind to a variable if we want
- **Statements** - you can think of these as the specific syntax of the programming language.  How do we write if statements, for loops, define functions, etc.  These are all statements

## 2. Variables & Types
- We can store information in variables.
  - In python, we don't have to specify what the type of the value being stored is, in compiled programming languages, you usually have to specify what type you expect to be stored in a variable.  Python will try it's best until something breaks, 
  - there's still some type hints that you can optionally supply 
- **Numbers / Numeric types**
  - `int` (whole numbers) 
      - `1 // 2 == 0` since the integer one is not divisble by the integer 2.  There's no integer that satisfies this expression.  Here, we're _specifying_ the operation `//` meaning "perform integer division" since python will interpret these numbers as floats by default 
  - `float` (decimals)
      - `1 / 2 == 0.5` since python inteprets the numbers as floats and we're not specifying integer division with the double slash operator, we'll get a float back from this expression which matches what we probably expect
  - Mixing numberic types: `1.0 // 2 = 0.0` , note the added `.0` to let us know that python is still treating our number as a float, despite using integer rules to perform the division
  - There are lots of things like this.  When you're first starting out and learning, they seem like "gotchas" and footguns to make programming harder, but eventually you'll be glad that someone else has specified the rules for how these things work, and made it possible for you to do this sort of mixing and matching.
- **Strings**
  - Any sequence of letters surrounded by quotes. 
      - `"single quoted string"`
      - `"""a sentence that includes "quotation" marks"""` - you can nest quotation marks
      - `'using single "quotes" to nest double quotes'` - you can also use single quotes.
      - The point being, there's many different ways to represent strings, I'm not sure of all the rules about like "triple quotes can't be inside double quotes can't be inside single quotes" and Idek if there are hardfast rules.  It mostly just comes down to convention and I'd treat it like `"""` > `"` > `'`  if you ever needed to nest two meta quotations within one another
  - Strings are defined as a sequence of characters.  
      - A Character is just one letter or symbol.  Typically confined to ASCII table (256 characters or reserved symbols mapped to unique byte)
      - you can see what the numeric representation of any character is using `ord(c)` 
      - There's different ways to encode a string (ASCII, UTF-8, UTF-16, etc.) each with different numeric representations underlying a specific token
      - You don't need to worry about this until you do.  E.g. trying to read a stream of bytes that you know represents text, but you choose the wrong encoding and it tries to cram a UTF byte into an ASCII character, but it's not one of the defined 256 ascii characters! you'll get an error

- **Booleans**
  - just `True` or `False` 
  - All of computing is built from 1s and 0s which map to boolean values and give rise to complex logic gates, ..., hop skip and a jump and we get to write python instead of machine code
  - Combine boolean values with logical operators: 
      - python is an idiomatic language, so rather than having to use like `&&, ||, !` we can just type `and, or, not` and get all of boolean algebra from there

## (Break to Recap and Poll for Pacng, Feedback, Questions)

## 3. Basic Operators and Control Structures
- Arithmetic (think PEMDAS)
- Operators with Strings, Lists, and other types
- Control Structures
    - If/Then/\[Else\]
        - Conditionals:
            - `==`
            - `<=` 
            - `>=`
            - `!=` 
            - `not`, `and`, `or`
    - Loops:
        - `while`
        - `for` 
        - Advanced For loops (iterables)
- Data Structures (intro)
    - Lists
    - Sets
    - Maps
    - Classes

## 4. Functions
- Motivation (reausability, readibility)
- procedures (nor args)
- methods/functions (take args)

## 5. Data Structures
- lists
    - ordered
    - indexable
- dictionaries 
    - unordered key, value pairs 
    - fast

## 6. Classes
- Generally, we use classes to represent the composition of data 
- Make a person class
- Constructor
- self 

## 7. Libraries and other APIs
- requests
- Flask

## 