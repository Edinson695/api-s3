import boto3

def lambda_handler(event, context):
    nombre_bucket = event['body']['bucket']
    nombre_directorio = event['body']['directorio'].strip('/')

    s3 = boto3.client('s3')

    s3.put_object(
        Bucket=nombre_bucket,
        Key=nombre_directorio + '/',
        Body=b''
    )

    return {
        'statusCode': 200,
        'bucket': nombre_bucket,
        'directorio': nombre_directorio,
        'mensaje': 'Directorio creado correctamente'
    }

    