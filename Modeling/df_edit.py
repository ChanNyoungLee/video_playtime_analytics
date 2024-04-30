def df_edit(dataframe):

    changedplaytime_edited_list = []
    playtime_edited_list = []

    for count in range(len(dataframe)):

        try:
            changedplaytime_edited_list.append(int(dataframe['generated_extensions_changedplaytime'][count][:2])*60 + int(dataframe['generated_extensions_changedplaytime'][count][3:]))
        except:
            changedplaytime_edited_list.append(0)

        try:
            playtime_edited_list.append(int(dataframe['object_extensions_playtime'][count][:2])*60 + int(dataframe['object_extensions_playtime'][count][3:]))
        except:
            playtime_edited_list.append(0)

    dataframe.insert(loc = dataframe.shape[1] , column = 'changedplaytime_edited', value = changedplaytime_edited_list)
    dataframe.insert(loc = dataframe.shape[1] , column = 'playtime_edited', value = playtime_edited_list)

    return dataframe