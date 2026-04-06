"""
scikit-learn 은 파이썬 기반 머신러닝 라이브러리로,
데이터 분석과 예측 모델을 쉽게 만들 수 있도록 도와주는 도구
설치 : pip install scikit-learn 또는 python -m pip install scikit-learn
사용 : from sklearn.linear_model import LogisticRegression

머신런닝 기본 : 데이터 준비 -> 모델 선택 -> 학습 -> 예측

LinearRegression() : 숫자를 예측할 때 사용
선형 회귀 분석 : 입력값 X 와 결과값 y 사이를 직선 관계로 보고, 가장 잘 맞는 직선을 찾아 예측합니다. 
예) 공부시간과 점수사이의 관계, 평수와 집값, 광고비와 매출관계 (결과가 숫자일때 주로 사용)


LogisticRegression() : 분류(종류)를 예측할 때 사용합니다.
예) 합격/불합격, 구매함/구매안함, 예방접종 함/예방접종 안함 (결과가 종류일때 주로 사용)
"""
# # 1. 라이브러리 import
# from sklearn.linear_model import LinearRegression
# from sklearn.linear_model import LogisticRegression

# # 입력 데이터: 공부시간
# X = [[1], [2], [3], [4], [5]] #입력 데이터 변수는 주로 X 대문자를 사용한다.

# # 결과 데이터: 시험점수
# y = [50, 60, 70, 80, 90] #결과 데이터는 주로 소문자 y를 사용

# # 모델 생성
# model = LinearRegression()

# # 학습
# model.fit(X, y)

# # 기울기와 절편 확인
# print("기울기:", model.coef_) #입력값이 결과에 얼마나 영향을 주는지 보여줌
# print("절편:", model.intercept_) #x값이 0일때 y값

# #점수 게산 : 40 + 10 * 공부시간

# stud = int(input ("시간을 입력하세요:"))
# # 예측
# print("공부 점수 예측:", model.predict([[stud]]))

# print(model.score(X,y)) #1에 가까울수록 잘 맞는 모델로 인식함.


# print("-"*50)
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


# # 입력 데이터: 공부시간
# X = [[1], [2], [3], [4], [5], [6]]

# # 결과 데이터: 불합격(0), 합격(1)
# y = [0, 0, 0, 1, 1, 1]

# # 모델 생성
# model = LogisticRegression()

# # 학습
# model.fit(X, y)

# # 예측
# print("3시간 공부:", model.predict([[3]])) #분석 결과
# print("5시간 공부:", model.predict([[5]]))

# # 확률 확인
# print("3시간 공부 확률:", model.predict_proba([[3]]))#3시간 공부 확률: [[0.63650301 0.36349699]] 클래스가 0일 확률이 약 63%, 클래스가 1일 확률이 약 30%
# print("5시간 공부 확률:", model.predict_proba([[5]]))#5시간 공부 확률: [[0.15694029 0.84305971]] 클래스가 0일 확률이 약 15%, 클래스가 1일 확률이 약 84%
"""
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

sd = pd.read_csv("cacl.csv", encoding='cp949') 

X = sd[['공부시간']]
y = sd['점수']

model = LinearRegression()
model.fit(X,y)

sdp = int(input("숫자를 입력하세요:"))
print("점수 예측:", model.predict([[sdp]]))
print(model.score, X,y)

from sklearn.linear_model import LinearRegression
import pandas as pd

try:
    sd = pd.read_csv("cacl.csv", encoding='cp949')
except:
    sd = pd.read_csv("cacl.csv", encoding='utf-8')

# [해결책] 파일의 컬럼명을 강제로 '공부시간', '점수'로 고정합니다.
# 이렇게 하면 CSV 파일의 제목이 무엇이든 상관없이 작동합니다.
sd.columns = ['공부시간', '점수'] 

# 2. 데이터 설정 (X는 반드시 2차원 [[]])
X = sd[['공부시간']]
y = sd['점수']

# 3. 모델 학습
model = LinearRegression()
model.fit(X, y)

# 4. 입력 및 예측
try:
    sdp = int(input("공부 시간을 입력하세요(숫자만): "))
    prediction = model.predict([[sdp]])
    
    print(f"\n[예측 결과]")
    print(f"{sdp}시간 공부 시 예상 점수: {prediction[0]}점")
    print(f"모델 정확도(R²): {model.score(X, y)}")
except ValueError:
    print("오류: 숫자만 입력해 주세요.")   
    """
from sklearn.linear_model import LinearRegression
import pandas as pd

# 1. 데이터 생성 및 CSV 저장
items_info = {
    "키보드": 15000,
    "마우스": 12000,
    "캠": 25000,
    "마우스패드": 5000
}

data = []
for name, price in items_info.items():
    for qty in range(1, 6):  # 수량 1~5
        data.append([name, qty, price, qty * price])

# 데이터프레임 생성 및 저장
df = pd.DataFrame(data, columns=['물품', '수량', '단가', '금액'])
df.to_csv('sales_data.csv', index=False, encoding='utf-8-sig')
print("시스템: 'sales_data.csv' 파일이 생성되었습니다.")

# 2. 모델 학습 (딕셔너리 사용)
models = {}  # 수정: 리스트[] 대신 딕셔너리{} 사용
for name in items_info.keys():
    item_df = df[df['물품'] == name]
    X = item_df[['수량']]  # 학습 데이터 (수량)
    y = item_df['금액']    # 결과 데이터 (금액)

    model = LinearRegression()
    model.fit(X, y)
    models[name] = model

print("시스템: 예측 모델 학습이 완료되었습니다.")
print("-" * 30)

# 3. 예측 프로그램 실행 (무한 루프)
while True:
    print("\n[물품 판매 금액 예측 (종료: q)]")
    item_name = input("물품명을 입력하세요 (키보드, 마우스, 캠, 마우스패드): ").strip()
    
    if item_name.lower() == 'q':
        print("프로그램을 종료합니다.")
        break
        
    if item_name not in models:
        print(f"오류: '{item_name}'은(는) 목록에 없는 물품입니다.")
        continue
        
    quantity_input = input("수량을 입력하세요: ").strip()
    if quantity_input.lower() == 'q':
        break
        
    try:
        quantity = int(quantity_input)
        
        # 모델을 사용하여 금액 예측
        prediction = models[item_name].predict([[quantity]])
        print(f"결과: {item_name} {quantity}개의 예측 금액은 {int(prediction[0]):,}원입니다.")
        
    except ValueError:
        print("오류: 수량은 숫자로 입력해 주세요.")