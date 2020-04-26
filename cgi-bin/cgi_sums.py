#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

print("Content-type: text/plain")
print()

form = cgi.FieldStorage()
stringlist = form.getlist('operand')

try:
    total = sum(map(int, stringlist))
    body = 'The sum of all operands is {}.'.format(total)
except (ValueError, TypeError):
    body = "Unable to calculate a sum: please provide integer operands"

print(body)

