# 데이터베이스 사용방법

# 1. Connetion 맺기   (Python ===== db)
# - IP       : 컴퓨터 주소
# - Port     : 27017(MONGODB)
# - ID & PW  : 계정정보
# 2. 명령 보내기       (Python ------> db)
# 3. 결과 받기         (Python <----- db)
# 4. Connection 끊기  (Python XXXXX db)

# MongoDB 구조
# - MongoDB(DBMS): 데이터 베이스 관리 시스템
#    ㄴ DB(NAVER): 프로젝트 단위
#       ㄴ collection(회원) - CRUD
#       ㄴ collection(카페) - CRUD
#       ㄴ collection(쇼핑) - CRUD
#       ㄴ collection(메일) - CRUD
#    ㄴ DB(KAKAO)
#    ㄴ DB(BLOG)

# MongoDB 데이터 주고받기
# - MongoDB는 BSON Type으로 데이터를 주고 받음
# - BSON(Binary JSON) = JSON과 거의 동일
# - 그냥 JSON Type으로 사용하면 됨(문제없음)
# - Python에서 JSON은 Dict Type 사용!(Python Dict = JSON)

from pymongo import MongoClient

# MongoDB Connection
def conn():
    #
    client = MongoClient("mongodb+srv://cnu:cnu1234@movieorange.cofucbv.mongodb.net/")  # IP, Port, ID,PW
    db = client["review"]  # DB 선택

    collection = db.get_collection("movie")   # collection 선택
    return collection
