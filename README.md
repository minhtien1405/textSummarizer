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