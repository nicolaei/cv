Nicolas Harlem Eide's CV
========================

Yup, this is my CV! It's tested, scalable and continuously deployed!

Running
-------

To view my CV, you can either check out the prettified PDF, or check it out
in your local python REPL!

To start off, you'll have to install the requirements.

.. code:: bash

    pip install -r requirements.txt

Now you can try to run it in your local python REPL!

.. code:: python

    >>> from nicolas import cv, formatting

    >>> help(cv)
    # [Help text for CV]

    >>> help(formatting)
    # [Help text for formatting]

The formatting module will let you view the data from the CV in a more pretty
format. Give it a try!

.. code:: python

    >>> print(formatting.header(cv.name))
    ===================================================================
    ===================================================================
    ======================                       ======================
    ======================  Nicolas Harlem Eide  ======================
    ======================                       ======================
    ===================================================================
    ===================================================================
