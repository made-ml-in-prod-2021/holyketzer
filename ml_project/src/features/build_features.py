# -*- coding: utf-8 -*-
import click
import os
import pandas as pd

from dotenv import find_dotenv, load_dotenv
from os import listdir
from os.path import isfile, join
from pathlib import Path
from sklearn.model_selection import train_test_split

from src.config import config
from src.logging import logger


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    for f in listdir(input_filepath):
        if isfile(join(input_filepath, f)) and f.endswith('.csv'):
            process_file(f, input_filepath, output_filepath)


def process_file(f, input_filepath, output_filepath):
    out_file_path = join(output_filepath, f)
    df = pd.read_csv(join(input_filepath, f))
    df = df.dropna()

    df_train, df_test = train_test_split(
        df,
        test_size=config['test_split'],
        random_state=config['random_state'],
    )

    path, ext = os.path.splitext(out_file_path)

    save_to_file(df_train, path + "_train" + ext)
    save_to_file(df_test, path + "_test" + ext)


def save_to_file(df, path):
    df.to_csv(path)
    logger.info(f'Final data set part saved at: {path}')


if __name__ == '__main__':
    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
