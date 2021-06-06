import os
import pandas as pd
import click

from datetime import date


@click.command("preprocess")
@click.option("--input-dir")
@click.option("--output-dir")
@click.option("--mode")
def preprocess(input_dir: str, output_dir, mode):
    if mode == "data":
        data = pd.read_csv(os.path.join(input_dir, "data.csv"))
        data["FirstLength"] = data["First"].apply(len)
        data["LastLength"] = data["Last"].apply(len)
        file = "data.csv"
    elif mode == "target":
        data = pd.read_csv(os.path.join(input_dir, "target.csv"))
        today = date.today()
        data["Age"] = pd.to_datetime(data["Birthdate"]).apply(
            lambda born: today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        )
        data.drop(columns=["Birthdate"], inplace=True)
        file = "target.csv"
    else:
        raise ValueError(f"unknown mode: '{mode}'")

    os.makedirs(output_dir, exist_ok=True)
    data.to_csv(os.path.join(output_dir, file), index=False)


if __name__ == '__main__':
    preprocess()
