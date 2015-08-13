# New York City Councilmatic

Keep track of what New York City Council is doing.

## Setup

**Install OS level dependencies:** 

* Python 3.4
* PostgreSQL 9.4 +

**Install app requirements**

We recommend using [virtualenv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html) and [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html) for working in a virtualized development environment. [Read how to set up virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Once you have virtualenvwrapper set up,

```bash
mkvirtualenv nyc-councilmatic
git clone https://github.com/datamade/nyc-councilmatic.git
cd nyc-councilmatic
pip install -r requirements.txt
cp councilmatic/settings_local.py.example councilmatic/settings_local.py.example
```

Afterwards, whenever you want to work on nyc-councilmatic,

```bash
workon nyc-councilmatic
```

## Setup your database

Before we can run the website, we need to create a database.

```bash
createdb nyc-councilmatic
```

## Running NYC Councilmatic

``` bash
python manage.py runserver
```

navigate to http://localhost:8000/

## Team

* Cathy Deng
* Forest Gregg
* Derek Eder

## Errors / Bugs

If something is not behaving intuitively, it is a bug, and should be reported.
Report it here: https://github.com/datamade/nyc-councilmatic/issues

## Note on Patches/Pull Requests
 
* Fork the project.
* Make your feature addition or bug fix.
* Commit, do not mess with rakefile, version, or history.
* Send a pull request. Bonus points for topic branches.

## Copyright

Copyright (c) 2015 Participatory Politics Foundation and DataMade. Released under the [MIT License](https://github.com/datamade/nyc-councilmatic/blob/master/LICENSE).
