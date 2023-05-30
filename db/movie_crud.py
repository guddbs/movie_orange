# CRUD
# - CREATE : 생성
# - READ : 조회
# - UPDATE : 생성
# - DELETE : 삭제

from db.connection import conn

# 리뷰를 저장(MongoDB)
def add_review(data):
    collection = conn()
    collection.insert_one(data)


# 리뷰 조회(MongoDB)
def get_reviews():
    pass