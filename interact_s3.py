import boto3
import pandas as pd 

# Criar um cliente para interagir com o AWS S3

s3_client = boto3.client('s3')

s3_client.download_file('datalake-marcoresende-igti', 
                        'data/cidades.csv', 
                        'data/cidades.csv')

df = pd.read_csv('data/cidades.csv', sep=";")
print(df)

s3_client.upload_file("data/pessoas.csv",
                      "datalake-marcoresende-igti",
                      "data/pessoas.csv")