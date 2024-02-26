# Oozie

## Bash Script to schedule an incremental load
```
#!/bin/bash

########### Modified to use ################
HOSTNAME=''
DBNAME=''
TABLE=''
USERNAME=''
PASSWORD=''
TARGET_DIR=""
IMPALA_ADDR=''
###########################################


max_id=$(impala-shell -i ${IMPALA_ADDR} -d default -q "SELECT max(id)
 FROM ${TABLE};" | grep -oP '^\|\s+\K\d+' | head -1)

query="SELECT * FROM ${TABLE} WHERE id > $max_id "
query+='AND $CONDITIONS'

sqoop import \
    --connect  jdbc:postgresql://${HOSTNAME}:5432/${DBNAME} \
    --username ${USERNAME} \
    --password ${PASSWORD} \
    --query "${query}" \
    --target-dir ${TARGET_DIR} \
    --split-by id \
    --as-textfile \
    --incremental append \
    --check-column id \
    --last-value ${max_id}
```
