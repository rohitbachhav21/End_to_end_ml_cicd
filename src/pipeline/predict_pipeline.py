import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        try:
            self.model_path = "artifacts/model.pkl"
            self.preprocessor_path = "artifacts/preprocessor.pkl"
            self.model = load_object(self.model_path)
            self.preprocessor = load_object(self.preprocessor_path)
        except Exception as e:
            logging.error("Error in loading model or preprocessor")
            raise CustomException(e, sys)

    def predict(self, features):
        try:
            logging.info("Starting prediction process")
            data_scaled = self.preprocessor.transform(features)
            preds = self.model.predict(data_scaled)
            logging.info("Prediction process completed")
            return preds
        except Exception as e:
            logging.error("Error during prediction")
            raise CustomException(e, sys)
        
class CustomData:
    def __init__(self,
                gender: str,
                race_ethnicity: str,
                parental_level_of_education: str,
                lunch: str,
                test_preparation_course: str,
                reading_score: int,
                writing_score: int):
        
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
    
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],

                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }
            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            return CustomException(e,sys)