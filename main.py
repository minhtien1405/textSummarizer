from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainningPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainningPipeline

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