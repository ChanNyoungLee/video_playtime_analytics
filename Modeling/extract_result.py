import os
import configs

from pyathena.pandas.util import as_pandas

conn = configs.conn

def extract_result(lecture_name):

    query = f"""
    SELECT action, object_duration, generated_extensions_changedplaytime, object_extensions_playtime,actor_extensions_userid, eventtime, target_id
    FROM mmilkt_caliper.m_media
    WHERE 1 = 1
        AND target_id LIKE '%{lecture_name}.%'
        AND (action = 'Started' OR action='Ended' OR action ='JumpedTo' OR action='Restarted' OR action='Paused')
    """
    result = as_pandas(conn.execute(query))
    # result = pd.DataFrame(result)

    if 'lecture_pickle' not in os.listdir():
        os.mkdir('./lecture_pickle')

    result.to_pickle(f'./lecture_pickle/{lecture_name}.pkl')

    return result