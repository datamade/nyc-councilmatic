#!/bin/bash

# Make project directory if it doesn't exist. This is mainly to ensure that these scripts work on a bare server

rm -Rf /home/datamade/nyc
mkdir -p /home/datamade/nyc

if [ "$DEPLOYMENT_GROUP_NAME" == "staging" ]
then
    rm -Rf /home/datamade/nyc-staging
    mkdir -p /home/datamade/nyc-staging
fi
if [ "$DEPLOYMENT_GROUP_NAME" == "production" ]
then
    rm -Rf /home/datamade/nyc-councilmatic
    mkdir -p /home/datamade/nyc-councilmatic
fi

# Decrypt blackbox-encrypted files
cd /opt/codedeploy-agent/deployment-root/$DEPLOYMENT_GROUP_ID/$DEPLOYMENT_ID/deployment-archive/ && chown -R datamade.datamade . && sudo -H -u datamade blackbox_postdeploy