from botocore import UNSIGNED
from botocore.config import Config

import boto3
import click
import logging

from src.config import config

@click.command()
@click.argument('output_filepath', type=click.Path())
def main(output_filepath):
    data_config =  config['data']
    session = boto3.session.Session()

    s3 = boto3.resource(
        's3',
        config=Config(signature_version=UNSIGNED),
        endpoint_url=data_config.get('endpoint_url'),
    )

    s3.Bucket(data_config['bucket']).download_file(data_config['path'], output_filepath)
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    logger = logging.getLogger(__name__)
    logger.info(f'Dataset downloaded to {output_filepath}')

if __name__ == '__main__':
    main()