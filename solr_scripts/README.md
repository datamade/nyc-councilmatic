#Solr Configuration

The [main README](../README.md) file in this repo should have all the details you need to get
Solr configured for your councilmatic instance. You should really only need to
refer to this file if you need to configure Solr to run more than one
Councilmatic instance on the same hardware.

###Multicore setup

**Before taking the following steps, make sure you follow the instructions in the
[main README](../README.md) file and have a working Solr setup.**

**Create configurations for your Councilmatic instances**

Inside the `/opt/solr/` folder (or wherever you placed your Solr installation),
you should see another folder called `multicore`. In there you should see a 
file called `solr.xml`. Open this file in your favorite editor and find the
lines that look like this:

```xml 
  <cores adminPath="/admin/cores" host="${host:}" hostPort="${jetty.port:8983}" hostContext="${hostContext:solr}">
    <core name="core0" instanceDir="core0" />
    <core name="core1" instanceDir="core1" />
    
    <shardHandlerFactory name="shardHandlerFactory" class="HttpShardHandlerFactory">
      <str name="urlScheme">${urlScheme:}</str>
    </shardHandlerFactory>
  </cores>
```

Update the `<core>` directives to something sane that you'll remember (probably
relating to the Councilmatic instances you're setting up). So, if you want to
setup Councilmatics for New York and Chicago, you might change them to look
like so:

```xml
    <core name="nyc" instanceDir="nyc" />
    <core name="chicago" instanceDir="chicago" />
```

Next, move the folders that were referenced by those `<core>` directives to
match the new names you've chosen:

```bash
mv multicore/core0 multicore/nyc
mv multicore/core1 multicore/chicago
```

There are a few files that Solr expects to be in those folders that, for some
reason, are not there by default. However, you can find them and copy them over
from the default configuration folder:

```bash
sudo cp solr/collection1/conf/stopwords.txt multicore/nyc/conf/
sudo cp solr/collection1/conf/synonyms.txt multicore/nyc/conf/

sudo cp solr/collection1/conf/stopwords.txt multicore/chicago/conf/
sudo cp solr/collection1/conf/synonyms.txt multicore/chicago/conf/

sudo cp -R solr/collection1/conf/lang multicore/nyc/conf/
sudo cp -R solr/collection1/conf/lang multicore/chicago/conf/

sudo cp -R solr/collection1/conf/protwords.txt multicore/nyc/conf/
sudo cp -R solr/collection1/conf/protwords.txt multicore/chicago/conf/

sudo cp solr/collection1/conf/admin-extra.* multicore/nyc/conf
sudo cp solr/collection1/conf/admin-extra.* multicore/chicago/conf
```

Lastly, you'll need to copy the `schema.xml` files over from the `solr_scripts`
folder located in your Councilmatic project folder:

```
sudo cp /path/to/nyc-councilmatic/solr_scripts/schema.xml /opt/solr/multicore/nyc/conf/
sudo cp /path/to/chi-councilmatic/solr_scripts/schema.xml /opt/solr/multicore/chicago/conf/
```

Whenever you want to update the schema, you'll need to copy it to the
appropriate folder, instead of what it says in the main README.

To run the Solr, you'll need to tell it to use the `multicore` folder as the
Solr home. To do that, you can pass it as an option when you start the process:

```bash
java -Dsolr.solr.home=multicore -jar start.jar
```

If you're using the example `jetty.conf` files, you can just use
`jetty_multicore.conf`.
