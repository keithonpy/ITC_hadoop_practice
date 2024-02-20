# Hadoop Command Line 

** [Basic operation on Hadoop](#Basic-operation-on-Hadoop)

** [Python on HDFS](#Python-on-HDFS)

** [Hive on HDFS](#Hive-on-HDFS)

** [HiveQL](#HiveQL)

** [Impala](#Impala-Query)

## Basic operation on Hadoop
- Show the files within the directory
  ```
  hdfs dfs -ls /path/to/directory
  ```
  
- Remove the file 
  ```
  hdfs dfs -rm /path/to/file
  ```

- change ownership of the file
  ```
  sudo -u hdfs hdfs dfs -chmod [number] [/path/to/file]
  ```

- Push the file to HDFS
  ```
  hdfs dfs -put [/path/to/file] [/path/at/HDFS]
  ```

- Pull the file from HDFS
  ```
  hdfs dfs -get [/path/at/HDFS]
  ```

- Do the wordcount example on Hadoop 
  ```
  sudo -u hdfs hadoop jar [path/to/hadoop-streaming.jar] wordcount [/path/to/file] [/path/to/output/directory]
  ```

- Display the info inside file on Hadoop
  ```
  hdfs dfs -cat [/path/to/file]
  ```
  
## Python on HDFS
- Run Python Scripts on Hadoop
  ```
  sudo -u hdfs hadoop jar [path/to/hadoop-streaming.jar] -files mapper.py reducer.py
  -mapper "/usr/bin/python mapper.py" -reducer "/usr/bin/python reducer.py" -input [/path/to/file] -output [/path/to/output/directory]
  ```

## Hive on HDFS
- Run hive on HDFS
  ```
  beeline -u jdbc:hive2://[hostname]:[portNumber]/[databaseName] -n [username] -p [password]
  ```
## HiveQL

- Create a external table
```
CREATE EXTERNAL TABLE [tableName]
([variables] [type]) 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
location "[path/to/directory/storing/tables]";
```

- Create an internal CRUD table
```
CREATE TABLE [tableName]
([variables] [type]);
```

- Create an insert-only internal table
```
CREATE TABLE [tableName]
([variables] [type])
STORED AS ORC
TBLPROPERTIES
('transactional' = true,
'transactional_properties'= 'insert_only');
```
- Load data into internal table
```
LOAD DATA INPATH 'path/to/the/data/file'
INTO TABLE [tableName]

```

- Create temporary table
```
CREATE TEMPORARY TABLE [tableName]
([variables] [type])
```

## Impala Query
- Run impala on command prompt
```
impala-shell -i [ip-address] -d default
```

- Refresh the cache data since impala get the data from cache
```
INVALIDATE METADATA;
```

