import os
import pandas as pd
import click
import joblib

from sklearn.ensemble import RandomForestRegressor


@click.command("train")
@click.option("--input-dir")
@click.option("--output-dir")
def train(input_dir: str, output_dir):
    data = pd.read_csv(os.path.join(input_dir, "data.csv"))
    target = pd.read_csv(os.path.join(input_dir, "target.csv"))
    data["Age"] = target["Age"]

    features = ["FirstLength", "LastLength"]

    model = RandomForestRegressor()
    model.fit(data[features], data["Age"])

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "model.pkl")
    joblib.dump(model, path)


if __name__ == '__main__':
    train()
