from pyspark.ml import PipelineModel
from pyspark.sql import SparkSession
import pandas as pd

spark = SparkSession.builder.appName("NewsSentimentTraining").getOrCreate()

# Load training data
df = pd.read_csv("pseudo_labeled.csv")

# Convert to Spark DataFrame
spark_df = spark.createDataFrame(df)

# Load/define your pipeline here
# Example: from pyspark.ml.feature import ...
# pipeline = ...

# Fit pipeline (pseudo code)
# model = pipeline.fit(spark_df)

# Save model
# model.write().overwrite().save("models/news_sentiment_pipeline_v1")
