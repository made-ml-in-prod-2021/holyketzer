# -*- coding: utf-8 -*-
import click
import joblib
import os
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from src.config import config
from src.logging import logger


@click.command()
@click.argument('train_path', type=click.Path(exists=True))
@click.argument('test_path', type=click.Path(exists=True))
@click.argument('model_config')
def main(train_path, test_path, model_config):
    df_train = pd.read_csv(train_path)
    df_test = pd.read_csv(test_path)

    x_train, y_train = split_x_y(df_train, config)
    x_test, y_test = split_x_y(df_test, config)

    if model_config in config['models']:
        model = build_model(config['models'][model_config], random_state=config['random_state'])
        model.fit(x_train, y_train)

        accuracy = accuracy_score(y_test, model.predict(x_test))
        model_path = os.path.join('models', model_config + '.pkl')
        joblib.dump(model, model_path)
        logger.info(f"Model: {model_path} Accuracy: {accuracy}")
    else:
        raise ValueError(f"unknown model_config {model_config}")


def build_model(model_config, random_state):
    params = {'random_state': random_state}
    params.update(model_config['params'])

    if model_config['class'] == 'LogisticRegression':
        return LogisticRegression(**params)
    elif model_config['class'] == 'RandomForestClassifier':
        return RandomForestClassifier(**params)
    else:
        raise ValueError(f"unknown model class {model_config['class']}")


def split_x_y(df, config):
    return df[config['features']], df[config['target']]


if __name__ == '__main__':
    main()
