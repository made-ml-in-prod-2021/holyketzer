import os
import pandas as pd
import joblib
import click


@click.command("predict")
@click.option("--input-dir")
@click.option("--output-dir")
@click.option("--model-dir")
def predict(input_dir: str, output_dir, model_dir):
    data = pd.read_csv(os.path.join(input_dir, "data.csv"))
    model = joblib.load(os.path.join(model_dir, "model.pkl"))

    features = ["FirstLength", "LastLength"]
    predicted = model.predict(data[features])
    predicted = pd.DataFrame(predicted, columns=["Age"])

    os.makedirs(output_dir, exist_ok=True)
    predicted.to_csv(os.path.join(output_dir, "predictions.csv"), index=False)


if __name__ == '__main__':
    predict()
