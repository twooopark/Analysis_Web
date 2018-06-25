import pandas as pd
'''
# pelicana
pelicana_table = pd.DataFrame.from_csv(
    '__result__/crawling/pelicana_table.csv',
    encoding='utf-8',
    index_col=0,
    header=0
).fillna('') # 비어있는 애들 처리(어떻게?? ㅠㅠ)

# # 비어있는 sido 컬럼이 있다면 제외 (각 지사 주소 데이터가 비어있음)
pelicana_table = pelicana_table[pelicana_table.sido != '']
pelicana_table = pelicana_table[pelicana_table.sido != '테스트']
pelicana_table = pelicana_table[pelicana_table.gungu != '']

# # v : row가 하나씩 들어올 것인데, 인덱스(name) 기준으로 각 컬럼이 묶임
# pelicana_table.apply(lambda v : print(v))
# pelicana_table.apply(lambda v : print(v), axis=1)

# 전체 매장 수
s1 = pelicana_table.apply(lambda r : str(r['sido'] + ' ' + r['gungu']), axis=1)
s2 = s1.value_counts()
print(s2)
'''
cfs_name = ['bbq','goobne','kyochon','nene','pelicana']
for cf_name in cfs_name :
    cf_table = pd.DataFrame.from_csv(
        '__result__/crawling/%s_table.csv' %(cf_name),
        encoding='utf-8',
        index_col=0,
        header=0
    ).fillna('')  # 비어있는 애들 처리(어떻게?? ㅠㅠ)

    # # 비어있는 sido 컬럼이 있다면 제외 (각 지사 주소 데이터가 비어있음)
    cf_table = cf_table[cf_table.sido != '']
    cf_table = cf_table[cf_table.sido != '테스트']
    cf_table = cf_table[cf_table.gungu != '']

    # # v : row가 하나씩 들어올 것인데, 인덱스(name) 기준으로 각 컬럼이 묶임
    # pelicana_table.apply(lambda v : print(v))
    # pelicana_table.apply(lambda v : print(v), axis=1)

    # 전체 매장 수
    s1 = cf_table.apply(lambda r: str(r['sido'] + ' ' + r['gungu']), axis=1)
    s2 = s1.value_counts()
    print(s2)
