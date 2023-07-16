# Text Summarizer
Finetune HuggingFace model, CICD deploy this project to AWS


## WorkFlows:

1. Update config.yaml file
2. Update params.yaml file
3. Update entity // is the return type of the function
4. Update configuration manager in src/config
5. update components
6. Update the pipeline
7. Update main.py
8. Update the app.py

delete artifacts/ and run main.py


1. Data Ingestion:
    Downloading the data/ unziped/ preparing data

2. Data Validations:
    Giving data to your model, you have to verity whether those data files are correct or not.

3. Data Transformations:
    First, data as text file need to be tokenized to become feature.

4. Training Model

5. Evaluating ML model

6. Create prediction pipeline

## For deployement
1. Create CICD job in Gitbu

2. Create Docker image

## Deployment:
  Using Elastic container in AWS
  1. Build a docker image of our source code
  2. Push that image to AWS
  3. Run that image in the EC2 instance

  CI/CD tools is using in Github


  ## How to Run:


Clone the repository

```bash
https://github.com/entbappy/End-to-end-Text-Summarization
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n summary python=3.8 -y
```

```bash
conda activate summary
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now, open up you local host and port





# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws

    Adding 2 policies here:
      
    #Policy:

        1. AmazonEC2ContainerRegistryFullAccess

        2. AmazonEC2FullAccess

  Then save access key to file.

	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	
	
## 3. Create ECR (Elastic Container Registry) repo to store/save docker image
    - Save the URI: 012047122186.dkr.ecr.us-east-1.amazonaws.com/text-s
	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app