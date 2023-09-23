import pandas as pd
import os

from .pick_regno import pick_regno


def csv_reader(test_data):
    df = pd.read_csv(test_data)
    result = []
    for index, row in df.iterrows():
        nn_len_scores = row['afts_regno_ai_length_scores']
        camera_regno = row['regno_recognize']
        nn_regno = row['afts_regno_ai']
        camera_score = row['recognition_accuracy']
        nn_score = row['afts_regno_ai_score']
        nn_sym_scores = row['afts_regno_ai_char_scores']
        camera_type = row['camera_type']
        camera_class = row['camera_class']
        time_check = row['time_check']
        direction = row['direction']
        model_name = os.path.join(os.path.dirname(__file__), 'micromodel.cbm')
        pick_regno_result = pick_regno(camera_regno, nn_regno, camera_score, nn_score, nn_sym_scores, nn_len_scores, camera_type, camera_class, 
            time_check, direction, model_name)
        result.append(pick_regno_result)
    list_of_lists = [arr.tolist() for arr in result]
    return list_of_lists
