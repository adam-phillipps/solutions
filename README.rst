Solutions Readme
================
===========
Description
===========
This package provides a function to tally words in a given string or file and a function
to remove overlapping times from a list of start and end times.  The methods are documented in the __doc__ variables and a little more in the 'Using the Package' section

===================
Getting the Package
===================
*There are two easy ways to obtaining the code...*

- ``git clone git@github.com:adam-phillipps/solutions.git``
- ``pip install solutions`` # This doesn't really work because I read it wasn't nice to push stuff like this up to the production server but it did pass all tests on the test server.

=================
Using the Package
=================
To use the methods, you will need to import the package.  At the top of your file or in the python console, add ``import solutions`` and to use the methods, ``solutions.word_count(file_path)`` or ``solutions.condense_meeting_times(times)``.  The ``word_count`` method accepts a string and returns a dictionary.  The string parameter can be any old string or it can be a file path.  In either case, the funcion tallies the number of occurrences of each word and keeps track of it in a dicionary that gets returned after the input has been read through.
THe ``condense_meeting_times`` function allows you to pass in any number of start and end times in a list of tuples and it gives back a new list that shows a view of all the intersecting time blocks without all the extra noise.