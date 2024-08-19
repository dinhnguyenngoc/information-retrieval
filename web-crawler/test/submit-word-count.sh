#!/bin/bash

# Set the path to your Spark installation
SPARK_HOME="/opt/spark"

# Submit the PySpark script to the cluster
# $SPARK_HOME/bin/spark-submit word-count.py

$SPARK_HOME/bin/spark-submit \
  --master yarn \
  --deploy-mode client \
  word-count.py