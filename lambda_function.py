import json
import boto3
import os

s3_client = boto3.client('s3')
polly_client = boto3.client('polly')

def lambda_handler(event, context):
    # Get the S3 bucket and file key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Read the text file from S3
    response = s3_client.get_object(Bucket=bucket, Key=key)
    text = response['Body'].read().decode('utf-8')
    
    # Call Amazon Polly to synthesize the text to speech
    polly_response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna'  # You can change the voice
    )
    
    # Save the synthesized speech to a new S3 key (output folder)
    output_key = key.replace('input-texts/', 'output-audios/').replace('.txt', '.mp3')
    
    # Store the audio file back in S3
    s3_client.put_object(
        Bucket=bucket,
        Key=output_key,
        Body=polly_response['AudioStream'].read(),
        ContentType='audio/mpeg'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(f"Text converted to speech and saved as {output_key}")
    }
