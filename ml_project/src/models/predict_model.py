import click
import joblib

import pandas as pd

from src.config import config
from src.logging import logger


@click.command()
@click.argument('model_path', type=click.Path(exists=True))
@click.argument('test_path', type=click.Path(exists=True))
def main(model_path, test_path):
    df_test = pd.read_csv(test_path)[config['features']]

    model = joblib.load(model_path)
    predictions = model.predict(df_test)

    output_path = "data/predictions/predictions.csv"
    res_df = pd.DataFrame(predictions, columns=[config['target']])
    res_df.to_csv(output_path, index=False)
    logger.info(f"Predicted {len(res_df)} records to {output_path}")


if __name__ == '__main__':
    main()
