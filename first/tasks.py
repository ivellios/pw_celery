from __future__ import absolute_import, unicode_literals
from .celery import app
import urllib2

@app.task
def add(x, y):
    return x + y

@app.task
def download(page):
    response = urllib2.urlopen(page)
    with open('page.html', 'wb') as output:
        output.write(response.read())

@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)
