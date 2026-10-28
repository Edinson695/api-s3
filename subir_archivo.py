import boto3
import base64

def lambda_handler(event, context):
    nombre_bucket = event['body']['bucket']
    directorio = event['body']['directorio'].strip('/')
    nombre_archivo = event['body']['nombre_archivo']
    contenido = event['body']['contenido']

    s3 = boto3.client('s3')
    
    s3.head_bucket(Bucket=nombre_bucket)

    ruta_directorio = directorio + '/'
    response = s3.list_objects_v2(
        Bucket=nombre_bucket,
        Prefix=ruta_directorio,
        MaxKeys=1
    )

    if response['KeyCount'] == '0':
        return (
            'statusCode':200,
            'mensaje': 'El directorio no existe'
        )

    ruta = directorio + '/' + nombre_archivo

    s3.put_object(
        Bucket=nombre_bucket,
        Key=ruta,
        Body=contenido.encode('utf-8'),
        ContentType='text/plain'
    )
    
    return {
        'statusCode': 200,
        'bucket': nombre_bucket,
        'archivo': nombre_archivo,
        'ruta': ruta,
        'mensaje': 'Archivo subido correctamente'
    }