# 🎙️ Text-to-Speech with AWS Polly, Lambda, and S3

This project automatically converts text files into audio using **Amazon Polly**, **AWS Lambda**, and **Amazon S3**. When a text file is uploaded to the S3 bucket, the Lambda function converts the text into speech and stores the resulting audio file in the same bucket.

## 🚀 Features

- **Automatic Text-to-Speech**: Converts uploaded text files to speech instantly.
- **Amazon Polly**: Uses Polly's realistic voice synthesis to generate speech.
- **S3 Bucket Storage**: Stores both text input and audio output files.
- **Lambda Automation**: Serverless execution of the process with AWS Lambda.
  
## 📋 Prerequisites

- **AWS Account**: Ensure you have an active AWS account.
- **IAM Role**: You need an IAM role with the following permissions:
  - **Amazon S3**: Read and write access.
  - **Amazon Polly**: Access to convert text to speech.
  - **CloudWatch Logs**: For Lambda execution logs.
 ![image](https://github.com/user-attachments/assets/4558b4a7-28bc-4fff-be14-4f437ec830a8)


## 🛠️ Setup Guide

### 1. Create an S3 Bucket
1. Go to the [S3 Console](https://s3.console.aws.amazon.com/s3/).
2. Create a new bucket (e.g., `text-to-speech-bucket`).
3. Create two folders inside:
   - `input-texts/` for uploading text files.
   - `output-audios/` for storing the resulting audio files.
![image](https://github.com/user-attachments/assets/6626f935-1374-44e1-be07-de7ce5b637da)

### 2. Create a Lambda Function
1. Open the [AWS Lambda Console](https://console.aws.amazon.com/lambda/).
2. Create a new function (e.g., `TextToSpeechLambda`).
3. Set up the function to trigger on S3 uploads and convert text files to speech using **Amazon Polly**.


### 3. Add S3 Trigger
1. Configure an S3 trigger in Lambda for the `input-texts/` folder.
2. Ensure the function executes when a `.txt` file is uploaded.
![image](https://github.com/user-attachments/assets/97ccda2c-c846-4c05-bcc7-6b9157a0005a)

### 4. Monitor and Test
1. Upload a sample text file (e.g., `sample_text.txt`) to the `input-texts/` folder.
2. Check the `output-audios/` folder for the generated audio file.
3. View Lambda execution logs in **CloudWatch** for debugging and monitoring.
![image](https://github.com/user-attachments/assets/6c6c4202-857f-4f40-8d9b-22b45d7865a2)
![image](https://github.com/user-attachments/assets/2e5717de-a075-4ac7-be01-fa4465c01063)
![image](https://github.com/user-attachments/assets/1ef16324-0862-4b39-bdb3-6f722a5f1928)


## 📝 Customization(optional)

- **Change Polly Voice**: Modify the Polly `VoiceId` to select different voices (e.g., `Joanna`, `Matthew`, `Ivy`).
- **Different Output Formats**: Adjust the `OutputFormat` (e.g., `mp3`, `ogg_vorbis`, `pcm`).
