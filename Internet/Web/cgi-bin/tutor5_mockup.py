#!/usr/bin/python3
"""
run tutor5 logic with formMockup instead of cgi.FieldStorage()
to test: python tutor5_mockup.py > temp.html, and open temp.html
"""

from formMockup import formMockup
form = formMockup(name='Bob',
                  shoesize='Small',
                  language=['Python', 'C++', 'HTML'],
                  comment='ni, Ni, NI')

print("Content-type: text/html")

html = """
<TITLE>tutor5.py</TITLE>
<H1> Greetings</H1>
<HR>
<H4>Your name is %(name)s</H4>
<H4>You wear rather %(shoesize)s shoes</H4>
<H4>Your current job:  %(job)s</H4>
<H4>You program in %(language)s</H4>
<H4>You also said:</H4>
<P>%(comment)s</P>
<HR>
"""

data = {}
for field in ('name', 'shoesize', 'job', 'language', 'comment'):
    if not field in form:                       # if the 'field' is not in the form
        data[field] = '(unknown)'
    else:
        if not isinstance(form[field], list):   # if the value of 'field' in the form is not a list object
            data[field] = form[field].value
        else:
            values = [x.value for x in form[field]]
            data[field] = ' and '.join(values)

print(html % data)
