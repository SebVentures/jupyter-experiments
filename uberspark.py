from pyspark.sql import SparkSession, DataFrame

def doSomething(self):
    print("Let's do something with spark")

def predict(self, target, features):
    print(f"Predicting {target} with {features}")


def uber_init():
    setattr(SparkSession, "doSomething", doSomething)
    setattr(DataFrame, "predict", predict)
    