from mlproject_0_1 import logger
from mlproject_0_1.pipeline.stage01_data_ingesion import DataIngestionTrainingPipeline

STAGE_NAME = " Data ingestion step"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
