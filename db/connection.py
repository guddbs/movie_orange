# 데이터베이스 사용방법

# 1. Connetion 맺기   (Python ===== db)
# - IP       : 컴퓨터 주소
# - Port     : 27017(MONGODB)
# - ID & PW  : 계정정보
# 2. 명령 보내기       (Python ------> db)
# 3. 결과 받기         (Python <----- db)
# 4. Connection 끊기  (Python XXXXX db)

from pymongo import MongoClient

# MongoDB Connection
def conn():
    client = MongoClient("mongodb+srv://cnu:cnu1234@movieorange.cofucbv.mongodb.net/")  # IP, Port, ID,PW
    db = client["movie"]

    collection = db.get_collection("movie")
    return collection
