from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel

spark = SparkSession.builder.appName("NewsSentimentStreaming").getOrCreate()

# Load trained model
model = PipelineModel.load("models/news_sentiment_pipeline_v1")

# Read JSON stream
input_path = "stream_input/"
output_path = "stream_output/"

df = spark.read.json(input_path)
predictions = model.transform(df)

predictions.write.mode("overwrite").parquet(output_path)
