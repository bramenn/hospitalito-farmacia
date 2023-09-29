import json
from typing import Dict
import boto3
from dotenv import load_dotenv
from os import getenv

load_dotenv()

AWS_SNS_GERAR_PDF = getenv("AWS_SNS_GENERAR_PDF")


sns_client = boto3.client(
    "sns",
    aws_access_key_id=getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=getenv("AWS_REGION"),
)


def enviar_evento_generar_pdf(data: Dict):
    response = sns_client.publish(
        TopicArn=AWS_SNS_GERAR_PDF,
        Message=json.dumps(data),
    )
