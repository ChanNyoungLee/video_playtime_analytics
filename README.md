# video_playtime_analytics


video_playtime_analytics

조회를 원하시는 강의명을 입력하시면 초당 재생 빈도 수 그래프와 pickle 파일이 생성됩니다.

ex) high_nasin_2019_soc_dapum_han_003 

해당 파일의 최상단 경로에 .env을 만들어서 
1. aws_access_key_id
2. aws_secret_access_key
3. region_name
4. s3_staging_dir
을 입력해주셔야 합니다.

aws_access_key : Access key ID

aws_secret_access_key : Secret access key

region_name : 로그가 쌓인 region

s3_staging_dir : 강의 재생 수를 조회할 때 생기는 데이터가 s3에 적재됩니다. 데이터가 적재되어도 되는 s3 경로를 작성 부탁드리겠습니다.
