from botocore import UNSIGNED
from botocore.config import Config

import boto3
import click

from src.config import config
from src.logging import logger


@click.command()
@click.argument('output_filepath', type=click.Path())
def main(output_filepath):
    data_config = config['data']

    s3 = boto3.resource(
        's3',
        config=Config(signature_version=UNSIGNED),
        endpoint_url=data_config.get('endpoint_url'),
    )

    s3.Bucket(data_config['bucket']).download_file(data_config['path'], output_filepath)
    logger.info(f'Dataset downloaded to {output_filepath}')


if __name__ == '__main__':
    main()
