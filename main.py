from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainningPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainningPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
  logger.info(f"Starting {STAGE_NAME}...")
  data_ingestion = DataIngestionTrainningPipeline()
  data_ingestion.main()
  logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
  logger.exception(e)
  raise e



STAGE_NAME = "Data Validation Stage"
try:
  logger.info(f"Starting {STAGE_NAME}...")
  data_ingestion = DataValidationTrainningPipeline()
  data_ingestion.main()
  logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
  logger.exception(e)
  raise e



STAGE_NAME = "Data Transformation Stage"
try:
  logger.info(f"\nStarting {STAGE_NAME}...")
  data_transformation = DataTransformationTrainingPipeline()
  data_transformation.main()
  logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
  logger.exception(e)
  raise e



STAGE_NAME = "Model Trainning Stage"
try:
  logger.info(f"\nStarting {STAGE_NAME}...")
  model_trainer = ModelTrainerTrainingPipeline()
  model_trainer.main()
  logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
  logger.exception(e)
  raise e



STAGE_NAME = "Model Evaluation Stage"
try:
  logger.info(f"\nStarting {STAGE_NAME}...")
  model_evaluation = ModelEvaluationTrainingPipeline()
  model_evaluation.main()
  logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
  logger.exception(e)
  raise e