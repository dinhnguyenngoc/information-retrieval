#!/bin/bash

# Set the path to your Spark installation
SPARK_HOME="/opt/spark"

# Submit the PySpark script to the cluster

pip install requests
pip install beautifulsoup4

$SPARK_HOME/bin/spark-submit \
  --master yarn \
  --deploy-mode client \
  web-crawler-dfs.py