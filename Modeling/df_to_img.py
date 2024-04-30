import os
import matplotlib.pyplot as plt

from collections import Counter

def df_to_img(lecture_name, play_time_list, object_duration):

    counts = Counter(play_time_list)
    counts_outlier_list = []
    for counts_index in counts.most_common(len(counts)):
        if counts_index[1] < counts.most_common(1)[0][1]*0.01:
            counts_outlier_list.append(counts_index[0])

    counts_outlier = Counter(counts_outlier_list)
    counts = counts - counts_outlier

    # gradient = 0

    # for second in range(len(counts)):
    #     if second != len(counts) - 1:
    #         gradient += (-(counts[second] - counts[second+1])) 
    #     elif second == len(counts) - 1:
    #         gradient = gradient/(len(counts)-1)

    # area = 0

    # for second in range(len(counts)):
    #     if second != len(counts) - 1:
    #         area += counts[second]/counts.most_common(1)[0][1]
    #     elif second == len(counts) - 1:
    #         area = area/(len(counts)-1)

    plt.clf()
        
    lecture_time_list = []
    for counts_len in range(len(counts)):
        lecture_time_list.append(counts.most_common(counts_len+1)[-1][0])
    max_time = max(lecture_time_list) 

    plt.xlim([-round(max_time*0.01),round(max_time*1.01)])
    plt.ylim(round(counts.most_common(len(counts))[-1][1]*0.9),round(counts.most_common(1)[0][1]*1.1))

    plt.grid(True)

    plt.hist(play_time_list,bins = max(play_time_list), color='cornflowerblue')
    
    # plt.xlabel('gradient : ' + str(gradient) + '/ area : ' + str(area))
    # plt.xlabel('area : ' + str(area))

    plt.title(lecture_name)

    if 'image' not in os.listdir('./'):
        os.mkdir('./image')

    # 과목별 이미지 저장        
    # if 'korean' not in os.listdir('./image/'):
    #     os.mkdir('./image/korean')

    # if 'math' not in os.listdir('./image/'):
    #     os.mkdir('./image/math')

    # if 'english' not in os.listdir('./image/'):
    #     os.mkdir('./image/english')

    # if 'science' not in os.listdir('./image/'):
    #     os.mkdir('./image/science')

    # if 'kor' in lecture_name:
    #     plt.savefig(f'./image/korean/{lecture_name}.png')
        
    # elif 'eng' in lecture_name:
    #     plt.savefig(f'./image/english/{lecture_name}.png')
        
    # elif 'mat' in lecture_name:
    #     plt.savefig(f'./image/math/{lecture_name}.png')
        
    # elif 'sci' in lecture_name:
    #     plt.savefig(f'./image/science/{lecture_name}.png')
        
    # else:
    #     plt.savefig(f'./image/{lecture_name}.png')

    plt.savefig(f'./image/{lecture_name}.png')


    # return counts, area
    return counts
