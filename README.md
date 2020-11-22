# pybug

In order to make this project work

Package requirement
python 3.5+
django 2.2+
sqlite3

This project was a proof of concept wasn't really written to be used in a production environment.  

With the help of 

The Definitive Guide to Django Second Edition	Adrian Holovaty and Jacob Kaplan-Moss	Paperback 2009
Python Web Development with Django Developer Library	Jeff Forcier, Paul Bissex, Wesley Chun	Paperback 2009
The Complete Reference Python	Martin C. Brown	Paperback 2001
Python Cookbook 3rd Edition	David Beazley & Brian K. Jones	Paperback 2013
Fundamentals of Python Data Structures	Kenneth A. Lambert	Paperback 2014
Python Essential Reference Third Edition	David M. Beazley	Paperback 2006
Python Essential Reference Fourth Edition	David M. Beazley	Paperback 2009

You'll need to use the django shell to make it work.
install pip
Instruction:
1.) install python
2.) install pip
3.) pip install django==2.2
4.) select a directory storing the project.  change directory to that location
5.) $> django-admin startproject pybug .
6.) $> python manage.py startapp tickets
7.) add the tickets app files to tickets directory
8.) check the pybug/settings.py.  update the file to match the repository settings.py file
9.) check the pybug/urls.py update the file to match the repository urls.py
10.) the main chunk of the code are in settings.py, urls.py, views.py, forms.py, serializer.py, models.py.

