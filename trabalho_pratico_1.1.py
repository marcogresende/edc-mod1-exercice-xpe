import boto3
import pandas as pd 

# Criar um cliente para interagir com o AWS S3

s3_client = boto3.client('s3')

#s3_client.download_file('datalake-marcoresende-igti', 
#                        'data/cidades.csv', 
#                        'data/cidades.csv')

df = pd.read_csv('data/MICRODADOS_ENEM_2020.csv', sep=";", encoding="ISO-8859-1")
#print(df)

s3_client.upload_file("data/MICRODADOS_ENEM_2020.csv",
                      "datalake-marcoresende-377000241855",
                      "raw-data/enem/year=2020/microdados_enem_2020.csv")
