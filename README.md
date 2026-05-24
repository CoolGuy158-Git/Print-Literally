# Print Literally

---

## What is it?

It is a python module that lets you print text simply by calling ```literal_print(text)```.

It is a wrapper around win32print.

---

## Why?

Well I made this to learn Windows API and stuff but the possible usage are:

    - Text dumping
    - Printing logs
    - etc.

---

## Commands

print to printer
```python
from print_literally import literal_print

literal_print("Hello world\n", True) # Leave blank for no logs
```

print to printer but binary (1's and 0's)
```python
from print_literally import bin_print

bin_print("Hello world\n", True) # Leave blank for no logs
```

---

## Backstory

I'm not sure if I'm the only one, but as a kid (around 9), when I watched movies and shows,
and someone is coding and types ```print```, I always thought that actually printed straight to the printer,
I was shocked that when the code was ran no printer started "Brrr, BZZZ, BRRRRRR".

And now I can code! Yay! so I decided I wanted to make a module that literally prints.
