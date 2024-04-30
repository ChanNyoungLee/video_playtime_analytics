import pandas as pd


def play_info(dataframe):
            
    user_set = pd.DataFrame()
    play_time_list = []

    object_duration = dataframe['object_duration'].unique()[0]

    for user in dataframe['actor_extensions_userid'].unique():

        user_df = dataframe[dataframe['actor_extensions_userid'] == user].copy()
        user_df.sort_values('eventtime',inplace = True)
        user_df.reset_index(drop = True , inplace = True)

        for user_df_len in range(len(user_df)):

            if user_df['action'][user_df_len] != 'Restarted':

                user_set = pd.concat([user_set,pd.DataFrame(user_df.loc[user_df_len]).T])
                user_set.reset_index(drop = True , inplace = True)
            
                if user_df_len +1 == len(user_df):
                    for max_playtime in range(user_set['playtime_edited'].max()):
                        play_time_list.append(max_playtime)

                    try:
                        user_set = user_set['action'] == 'JumpedTo'
                        for user_set_len in range(len(user_set)):
                            if (user_set['playtime_edited'][user_set_len] - user_set['changedplaytime_edited'][user_set_len]) > 0:
                                for replay_time in range(user_set['playtime_edited'][user_set_len] - user_set['changedplaytime_edited'][user_set_len]):
                                    play_time_list.append(user_set['changedplaytime_edited'][user_set_len]+replay_time)

                        for user_set_len in range(len(user_set)):        
                            if (user_set['playtime_edited'][user_set_len] - user_set['changedplaytime_edited'][user_set_len]) < 0:  
                                for skip_time in range(user_set['playtime_edited'][user_set_len] - user_set['changedplaytime_edited'][user_set_len]):
                                        play_time_list.remove(user_set['changedplaytime_edited'][user_set_len]+skip_time)

                        user_set = pd.DataFrame()
                    except:
                        continue

                try:

                    if user_df['action'][user_df_len+1] == 'Restarted':

                        for max_playtime in range(user_set['playtime_edited'].max()):
                            play_time_list.append(max_playtime)

                        user_set = user_set['action'] == 'JumpedTo'
                        for user_set_len in range(len(user_set)):
                            if (user_set['playtime_edited'][user_set_len] - user_set['changedplaytime_edited'][user_set_len]) > 0:
                                for replay_time in range(user_set['playtime_edited'][user_set_len] - user_set['changedplaytime_edited'][user_set_len]):
                                    play_time_list.append(user_set['changedplaytime_edited'][user_set_len]+replay_time)

                        for user_set_len in range(len(user_set)):        
                            if (user_set['playtime_edited'][user_set_len] - user_set['changedplaytime_edited'][user_set_len]) < 0:  
                                for skip_time in range(user_set['playtime_edited'][user_set_len] - user_set['changedplaytime_edited'][user_set_len]):
                                    try:
                                        play_time_list.remove(user_set['playtime_edited'][user_set_len]+skip_time)
                                    except:
                                        continue

                        user_set = pd.DataFrame() ###
                    else:
                        continue
        
        
                except:
                    continue
                        
            elif user_df['action'][user_df_len] == 'Restarted':
                user_set = pd.DataFrame()
                user_set = pd.DataFrame(user_df.loc[user_df_len]).T

    outlier_list = []

    for play_sec in play_time_list:
        # if play_sec > float(dataframe['object_duration'].unique()[0]*1.1):
        if play_sec > float(object_duration*1.1):
            outlier_list.append(play_sec)

    for outlier_sec in outlier_list:
        play_time_list.remove(outlier_sec)

    return play_time_list, object_duration
