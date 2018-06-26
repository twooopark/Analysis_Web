import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

RESULT_DIRECTORY = '__result__/visualization'

def showmap(blockedmap, targetdata, title, color):
    BORDER_LINES = [
        [(3, 2), (5, 2), (5, 3), (9, 3), (9, 1)],  # 인천
        [(2, 5), (3, 5), (3, 4), (8, 4), (8, 7), (7, 7), (7, 9), (4, 9), (4, 7), (1, 7)],  # 서울
        [(1, 6), (1, 9), (3, 9), (3, 10), (8, 10), (8, 9),
         (9, 9), (9, 8), (10, 8), (10, 5), (9, 5), (9, 3)],  # 경기도
        [(9, 12), (9, 10), (8, 10)],  # 강원도
        [(10, 5), (11, 5), (11, 4), (12, 4), (12, 5), (13, 5),
         (13, 4), (14, 4), (14, 2)],  # 충청남도
        [(11, 5), (12, 5), (12, 6), (15, 6), (15, 7), (13, 7),
         (13, 8), (11, 8), (11, 9), (10, 9), (10, 8)],  # 충청북도
        [(14, 4), (15, 4), (15, 6)],  # 대전시
        [(14, 7), (14, 9), (13, 9), (13, 11), (13, 13)],  # 경상북도
        [(14, 8), (16, 8), (16, 10), (15, 10),
         (15, 11), (14, 11), (14, 12), (13, 12)],  # 대구시
        [(15, 11), (16, 11), (16, 13)],  # 울산시
        [(17, 1), (17, 3), (18, 3), (18, 6), (15, 6)],  # 전라북도
        [(19, 2), (19, 4), (21, 4), (21, 3), (22, 3), (22, 2), (19, 2)],  # 광주시
        [(18, 5), (20, 5), (20, 6)],  # 전라남도
        [(16, 9), (18, 9), (18, 8), (19, 8), (19, 9), (20, 9), (20, 10)],  # 부산시
    ]

    whitelabelmin = (max(blockedmap[targetdata]) - min(blockedmap[targetdata])) * 0.25 + min(blockedmap[targetdata])

    vmin = min(blockedmap[targetdata])
    vmax = max(blockedmap[targetdata])
    mapdata = blockedmap.pivot(index='y', columns='x', values=targetdata)
    masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)
    cmapname = color
    plt.figure(figsize=(8, 13))
    plt.title(title)
    plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname, edgecolor='#aaaaaa', linewidth=0.5)
    for idx, row in blockedmap.iterrows():
        annocolor = 'white' if row[targetdata] > whitelabelmin else 'black'
        dispname = row['shortName']

        # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시한다.
        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 7.5, 1.5
        else:
            fontsize, linespacing = 11, 1.2

        plt.annotate(dispname, (row['x'] + 0.5, row['y'] + 0.5), weight='bold',
                     fontsize=fontsize, ha='center', va='center', color=annocolor,
                     linespacing=linespacing)

    for path in BORDER_LINES:
        ys, xs = zip(*path)
        plt.plot(xs, ys, c='black', lw=4)

    plt.gca().invert_yaxis()
    plt.axis('off')

    cb = plt.colorbar(shrink=.1, aspect=10)
    cb.set_label(targetdata)
    plt.tight_layout()
    plt.savefig(RESULT_DIRECTORY+'/' + targetdata + '.png')
    plt.show()


# pelicana
pelicana_table = pd.DataFrame.from_csv(
    '__result__/crawling/pelicana_table.csv',
    encoding='utf-8',
    index_col=0,
    header=0).fillna('')

pelicana_table = pelicana_table[pelicana_table.sido != '']
pelicana_table = pelicana_table[pelicana_table.gungu != '']
pelicana = pelicana_table.apply(lambda r: str(r['sido']) + ' ' + str(r['gungu']), axis='columns').value_counts() # 'SIDO GUNGU' 별 매장수
# print(pelicana)

# nene
nene_table = pd.DataFrame.from_csv(
    '__result__/crawling/nene_table.csv',
    encoding='utf-8',
    index_col=0,
    header=0).fillna('')

nene_table = nene_table[nene_table.sido != '']
nene_table = nene_table[nene_table.gungu != '']
nene = nene_table.apply(lambda r: str(r['sido']) + ' ' + str(r['gungu']), axis='columns').value_counts() # 'SIDO GUNGU' 별 매장수
# print(nene)

# kyochon
kyochon_table = pd.DataFrame.from_csv(
    '__result__/crawling/kyochon_table.csv',
    encoding='utf-8',
    index_col=0,
    header=0).fillna('')

kyochon_table = kyochon_table[kyochon_table.sido != '']
kyochon_table = kyochon_table[kyochon_table.gungu != '']
kyochon = kyochon_table.apply(lambda r: str(r['sido']) + ' ' + str(r['gungu']), axis='columns').value_counts() # 'SIDO GUNGU' 별 매장수
# print(kyochon)

# goobne
goobne_table = pd.DataFrame.from_csv(
    '__result__/crawling/goobne_table.csv',
    encoding='utf-8',
    index_col=0,
    header=0).fillna('')

goobne_table = goobne_table[goobne_table.sido != '']
goobne_table = goobne_table[goobne_table.gungu != '']
goobne = goobne_table.apply(lambda r: str(r['sido']) + ' ' + str(r['gungu']), axis='columns').value_counts() # 'SIDO GUNGU' 별 매장수
# print(goobne)



#
chicken_table = pd.DataFrame({'pelicana': pelicana, 'nene': nene, 'kyochon': kyochon, 'goobne': goobne}).fillna(0)
chicken_table = chicken_table.drop(chicken_table[chicken_table.index == '00 18'].index)
chicken_table = chicken_table.drop(chicken_table[chicken_table.index == '테스트 테스트구'].index)
chicken_sum_table = chicken_table.sum(axis=0)

'''
plt.figure()
chicken_sum_table.plot(kind='bar')
plt.show()
'''

data_draw_korea = pd.read_csv('data_draw_korea.csv', index_col=0, encoding='utf-8')
data_draw_korea.index = data_draw_korea.apply(lambda r: r['광역시도'] + ' ' + r['행정구역'], axis=1)


chicken_merge = pd.merge(
    data_draw_korea,
    chicken_table,
    how='outer',
    left_index=True,
    right_index=True)

# # 면적이 NaN인 충청북도 청원군 같은 요소가 에러를 발생시킨다.
# print(chicken_merge['면적'])

chicken_merge = chicken_merge[~np.isnan(chicken_merge['면적'])]
print(chicken_merge)


# 경로가 없으면 만들자
if not os.path.exists(RESULT_DIRECTORY):
    os.makedirs(RESULT_DIRECTORY)

# 페리카나 매장 분포
showmap(chicken_merge, 'pelicana', '페리카나 매장 분포', 'Blues')
# 네네 매장 분포
showmap(chicken_merge, 'nene', '네네 매장 분포', 'Greens')
# 굽네 매장 분포
showmap(chicken_merge, 'goobne', '굽네 매장 분포', 'Reds')
# 교촌 매장 분포
showmap(chicken_merge, 'kyochon', '교촌 매장 분포', 'Oranges')

chicken_merge['total'] = chicken_table.sum(axis=1)
# 치킨 프랜차이즈 매장 분포
chicken_merge = chicken_merge[~np.isnan(chicken_merge['total'])]
showmap(chicken_merge, 'total', '치킨 프랜차이즈 매장 분포', 'rainbow')

# 인구 만명 당 매장 수
chicken_merge['total10k'] = chicken_merge['total'] / chicken_merge['인구수']
chicken_merge = chicken_merge[~np.isnan(chicken_merge['total10k'])]
showmap(chicken_merge, 'total10k', '치킨 프랜차이즈 매장 분포', 'Purples')

# 면적 당 매장 수
chicken_merge['area'] = chicken_merge['total'] / chicken_merge['면적']
chicken_merge = chicken_merge[~np.isnan(chicken_merge['area'])]
showmap(chicken_merge, 'area', '치킨 프랜차이즈 매장 분포', 'Greys')





'''
import pandas as pd

# pelicana
pelicana_table = pd.DataFrame.from_csv(
    '__result__/crawling/pelicana_table.csv',
    encoding='utf-8',
    index_col=0,
    header=0
).fillna('') # 결측값을 특정 값으로 채우기 (결측값을 ''로 채움)

# # 비어있는 sido 컬럼이 있다면 제외 (각 지사 주소 데이터가 비어있음)
pelicana_table = pelicana_table[pelicana_table.sido != '']
pelicana_table = pelicana_table[pelicana_table.sido != '테스트']
pelicana_table = pelicana_table[pelicana_table.gungu != '']

# # v : row가 하나씩 들어올 것인데, 인덱스(name) 기준으로 각 컬럼이 묶임
# pelicana_table.apply(lambda v : print(v))
# pelicana_table.apply(lambda v : print(v), axis=1)

# 전체 매장 수 (옆으로 데이터 열을 연결하고 싶으면 axis=1로 인수를 설정)
pelicana_table = pelicana_table.apply(lambda r : str(r['sido'] + ' ' + r['gungu']), axis=1)
pelicana_table = pelicana_table.value_counts()
pelicana_table = pd.DataFrame(pelicana_table, columns=['count'])


cfs_name = ['bbq','goobne','kyochon','nene']#,'pelicana']
# result_table = pd.Series([0], index=['경기도 부천시'])
for cf_name in cfs_name :
    cf_table = pd.DataFrame.from_csv(
        '__result__/crawling/%s_table.csv' %(cf_name),
        encoding='utf-8',
        index_col=0,
        header=0
    ).fillna('')  # 결측값을 특정 값으로 채우기

    print(cf_name)
    print("-------------------------------------------")
    # # 비어있는 sido 컬럼이 있다면 제외 (각 지사 주소 데이터가 비어있음)
    cf_table = cf_table[cf_table.sido != '']
    cf_table = cf_table[cf_table.sido != '테스트']
    cf_table = cf_table[cf_table.gungu != '']

    # # v : row가 하나씩 들어올 것인데, 인덱스(name) 기준으로 각 컬럼이 묶임
    # pelicana_table.apply(lambda v : print(v))
    # pelicana_table.apply(lambda v : print(v), axis=1)

    # 전체 매장 수 ( Series로 변함 )
    # 1. "시도 군구" 정보를 모두 불러온다
    cf_table = cf_table.apply(lambda r: str(r['sido'] + ' ' + r['gungu']), axis=1)
    # 2. "시도 군구" 를 카운트 한다.
    cf_table = cf_table.value_counts()

    addr = list(cf_table.index)

    cf_table = pd.DataFrame(addr, cf_table, columns=['count'])
    result_table = pd.merge(cf_table, pelicana_table, )
    # print(type(cf_table), cf_table)
    # print(type(pelicana_table), pelicana_table)
    print(type(result_table), result_table)




data_draw_korea = pd.read_csv('data_draw_korea.csv', index_col=0, encoding='UTF-8')
# print(data_draw_korea)
# data_draw_korea.index = data_draw_korea.apply(lambda r: r['광역시도'] + ' ' + r['행정구역'], axis=1)
'''