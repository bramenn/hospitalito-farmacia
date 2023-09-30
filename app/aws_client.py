import json
from typing import Dict
import boto3

from .config import (
    AWS_ACCESS_KEY_ID,
    AWS_REGION,
    AWS_SECRET_ACCESS_KEY,
    AWS_SNS_GERAR_PDF,
)

sns_client = boto3.client(
    "sns",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)


def enviar_evento_generar_pdf(data: Dict):
    response = sns_client.publish(
        TopicArn=AWS_SNS_GERAR_PDF,
        Message=json.dumps(data),
    )
