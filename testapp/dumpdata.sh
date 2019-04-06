#!/bin/sh

# Dump a snapshot of the database to stdout
#
# JSON format, indented with 2 spaces.
#
# --natural-foreign and --natural-primary to ensure compatibility across
# different developer's databases
#
# --exclude any data that's unecesarry. Data such as auth.permission will
# have defaults created by the initial database migration and we don't care
# about the value of these objects.
#
# Pipe this output into the json file: ./dumpdata.sh > testdata.json

python manage.py dumpdata \
  --format=json \
  --indent=2 \
  --natural-foreign \
  --natural-primary \
  --exclude sessions.session \
  --exclude auth.permission \
  --exclude wagtailcore.groupcollectionpermission \
  --exclude wagtailcore.grouppagepermission \
  --exclude contenttypes.contenttype
