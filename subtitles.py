import re

import pandas as pd

def time_to_seconds(time_str):
    h, m, s = map(float, time_str.split(':'))
    return round((h * 3600) + (m * 60) + (s), 3)

def srt_to_df(srt_file_path: str) -> pd.DataFrame:
    with open(srt_file_path, 'r') as srt_file:
        srt_data = srt_file.read()

    pattern = r'(\d+)\n([\d:.]+) --> ([\d:.]+)\n(.*?)\n\n'      # NOTE: 때에 따라 개행개수 수정필요
    matches = re.findall(pattern, srt_data, re.DOTALL)

    data = []
    for match in matches:
        index, start, end, text = match
        data.append({
            'index' : int(index),
            'start' : start,
            'end' : end,
            'text' : text
        })
    
    df = pd.DataFrame(data, columns=['index', 'start', 'end', 'text'])
    df['start'] = df['start'].apply(time_to_seconds)
    df['end'] = df['end'].apply(time_to_seconds)

    return df