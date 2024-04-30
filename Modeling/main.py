import os
import pandas as pd

from extract_result import extract_result
from df_edit import df_edit
from play_info import play_info
from df_to_img import df_to_img


lecture_name = input('조회를 원하는 강의명을 입력해주세요.  ')

result = extract_result(lecture_name)
dataframe = df_edit(result)
play_time_list, object_duration = play_info(dataframe)
counts, _ = df_to_img(lecture_name, play_time_list, object_duration)

if 'counts' not in os.listdir('./'):
    os.mkdir('./counts')

counts = pd.DataFrame.from_dict(counts, orient='index').rename(columns={0:'count'}).reset_index(drop=True)
counts.to_pickle(f'./counts/{lecture_name}.pkl')