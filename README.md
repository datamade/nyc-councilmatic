![dungeon8807construction](https://cloud.githubusercontent.com/assets/1406537/9255913/f43087b0-41b1-11e5-9a8e-03617b660b70.gif)

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
```

Afterwards, whenever you want to use this virtual environment to work on nyc-councilmatic, run `workon nyc-councilmatic`

**Create your settings file**

```bash
cp councilmatic/settings_local.py.example councilmatic/settings_local.py
```

Then edit `councilmatic/settings_local.py`:
- `USER` should be your username

**Setup your database**

Before we can run the website, we need to create a database.

```bash
createdb nyc_councilmatic
```

Then, run migrations

```bash
python manage.py migrate --no-initial-data
```

Create an admin user - set a username & password when prompted

```bash
python manage.py createsuperuser
```

## Importing data from the open civic data api

Run the loaddata management command. This will take a few minutes.

```bash
python manage.py loaddata
```

## Running NYC Councilmatic locally

``` bash
python manage.py runserver
```

navigate to http://localhost:8000/

## Setup Search

**Install Open JDK or update Java**

On Ubuntu:

``` bash
$ sudo apt-get update
$ sudo apt-get install openjdk-7-jre-headless jetty
```

On OS X:

1. Download latest Java from
[http://java.com/en/download/mac_download.jsp?locale=en](http://java.com/en/download/mac_download.jsp?locale=en)
2. Follow normal install procedure
3. Change system Java to use the version you just installed:

``` bash
$ sudo mv /usr/bin/java /usr/bin/java16
$ sudo ln -s /Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/bin/java /usr/bin/java
```

**Download and test Solr**

``` bash 
$ wget http://mirror.sdunix.com/apache/lucene/solr/4.10.4/solr-4.10.4.tgz
$ tar -xvf solr-4.10.4.tgz
$ sudo cp -R solr-4.10.4/example /opt/solr

# Tell Django Haystack to generate a schema file for you. (Run this with your
# virtual environment activated)
$ python manage.py build_solr_schema > schema.xml

# Copy schema.xml for this app to solr directory
$ cp /path/to/search/schema.xml /opt/solr/solr/collection1/conf/schema.xml

# Test to see that it's working. If you see error output, somethings wrong
$ cd /opt/solr
$ sudo java -jar start.jar

# Now index the database
$ python manage.py rebuild_index
```

**Install and configure Jetty for Solr**

Just running Solr as described above is probably OK in a development setting.
To deploy Solr in production, you'll want to using something like Jetty. Here's
how you'd do that on Ubuntu:

``` bash 
$ sudo apt-get install jetty

# Backup stock init.d script
$ sudo mv /etc/init.d/jetty ~/jetty.orig

# Get init.d script suggested by Solr docs
$ wget http://svn.codehaus.org/jetty/jetty/branches/jetty-6.1/bin/jetty.sh
$ sudo mv jetty.sh /etc/init.d/jetty
$ sudo chown root.root /etc/init.d/jetty
$ sudo chmod 755 /etc/init.d/jetty

# Add Solr specific configs to /etc/default/jetty
$ sudo mv /etc/defualt/jetty /etc/default/jetty.orig
$ sudo vim /etc/default/jetty

# Add these lines:
JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
JAVA_OPTIONS="-Dsolr.solr.home=/opt/solr/solr $JAVA_OPTIONS"
JETTY_HOME=/opt/solr
JETTY_USER=jetty
JETTY_LOGS=/opt/solr/logs
CONFIGS=/opt/solr/etc/jetty.xml

# Change ownership of the Solr directory so Jetty can get at it
$ sudo chown -R jetty.jetty /opt/solr

# Start up Solr
$ sudo service jetty start

# Solr should now be running on port 8983


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
