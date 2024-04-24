from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.mlproject.components.data_trasformation import DataTransformationConfig, DataTransformation
from src.mlproject.components.model_trainer import ModelTrainer, ModelTrainerConfig

if __name__ == "__main__":
    logging.info("The excution has started")

    try:
        #data ingestion
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        #data transformation
        data_trasformation = DataTransformation()
        train_arr, test_arr,_ = data_trasformation.initiate_data_transformation(train_data_path, test_data_path)

        #model trainer
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr, test_arr))
        
    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e, sys)