import sys
from NetworkSecurity.component.data_ingestion import DataIngestion
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging
from NetworkSecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig

if __name__=="__main__":
    try: 
        trainingpiplelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpiplelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        datainsectionartifact = data_ingestion.initiate_data_ingestion()
        print(datainsectionartifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)