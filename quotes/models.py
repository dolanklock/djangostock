from django.db import models

# This is where we setup out data bases
# each data table should be its own class, for example.
"""
if you had a data table of employees and had column for their first name, last name, and email, then the model class would look
something like this...

class Employee(models.Model):
    f_name = models.CharField()
    l_name = models.CharField()
    email = models. CharField()

"""

# CharField in Django is a small amount of text (someones name)
# TextField in Djnago is a lot of text (paragraph)

# see this link below for field types documentation django (scroll down to see methods "CharField")
# https://docs.djangoproject.com/en/1.11/ref/models/fields/

# always two step process when creating django database object. 1. create the model. and 2. migrate to the database (push into database)
# to push the migration you need to go to your terminal "git bash"
# make sure you are in correct directory so when you type "ls" you see manage.py, and then type these commands
# python manage.py makemigrations
# python manage.py migrate


class Stock(models.Model):  # all models need to inherit from models.Model
    ticker = models.CharField(max_length=100)  # CharField is a database datatype. Telling Django here what type of data will be stored in this field in the database
    
    def __str__(self):
        return self.ticker

