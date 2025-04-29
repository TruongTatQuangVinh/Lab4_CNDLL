from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.evaluation import RegressionEvaluator
import os

def train_model(data_dir):
    spark = SparkSession.builder \
        .appName("Train Model") \
        .config("spark.driver.extraJavaOptions", "-Djava.security.manager=allow") \
        .getOrCreate()

    # Path to the received train file
    received_file_path = os.path.join(data_dir, "received_train.csv")

    # Load the training data
    data = spark.read.csv(received_file_path, header=True, inferSchema=True)

    data = data.dropna()

    # Convert string columns to numeric using StringIndexer
    string_columns = [col for col, dtype in data.dtypes if dtype == "string" and col != "exam_score"]
    for col in string_columns:
        indexer = StringIndexer(inputCol=col, outputCol=f"{col}_indexed")
        data = indexer.fit(data).transform(data)

    # Update feature columns to include indexed columns
    feature_columns = [f"{col}_indexed" if col in string_columns else col for col in data.columns if col != "exam_score"]

    # Assemble features into a single vector
    assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
    data = assembler.transform(data)

    # Split Data into Training and Test Sets
    train_data, test_data = data.randomSplit([0.8, 0.2], seed=42)

    # Train a Machine Learning Model
    lr = LinearRegression(featuresCol="features", labelCol="exam_score")  # Replace "target_column" with the actual column name
    lr_model = lr.fit(train_data)

    # Evaluate the Model
    predictions = lr_model.transform(test_data)
    evaluator = RegressionEvaluator(labelCol="exam_score", predictionCol="prediction", metricName="rmse")  # Replace "target_column" with the actual column name
    rmse = evaluator.evaluate(predictions)
    print(f"\nRoot Mean Squared Error (RMSE): {rmse}")

    evaluator_mae = RegressionEvaluator(labelCol="exam_score", predictionCol="prediction", metricName="mae")
    mae = evaluator_mae.evaluate(predictions)
    print(f"Mean Absolute Error (MAE): {mae} \n")

    spark.stop()

if __name__ == "__main__":
    # Directory containing the train files
    train_data_dir = "../Lab4/data"
    train_model(train_data_dir)