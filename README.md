# Overview

`csv_to_tab` is a wrapper for python's `tabulate` that handles input from stdin that is CSV compatible. The purpose was to make a generic interface for output
data from some of my other python CLIs and not have to repeat all the pretty output. Note that normally something like `column``would be used, but `column` does
not seem to understand escaping of commas in text.

# Notes

Currently this requires click and tabulate. Proper dependency management is forthcoming. 
