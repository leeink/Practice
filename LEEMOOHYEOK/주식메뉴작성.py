import requests
from bs4 import BeautifulSoup
import pandas as pd

code_dict = {
    "1": "005930",
    "2": "000660",
    "3": "005380",
    "4": "000270",
    "5": "373220"
}

headers = {"User-Agent": "Mozilla/5.0"}

while True:
    print("\n1.삼성전자 2.하이닉스 3.현대 4.기아 5.LG에너지솔루션 6.종료")
    choice = input("회사를 선택하세요 : ")

    if choice in code_dict:
        target_code = code_dict[choice]
        start_p = int(input("시작 페이지 : "))
        end_p = int(input("마지막 페이지 : "))
        
        item = []
        for page in range(start_p, end_p + 1):
            url = f"https://finance.naver.com/item/frgn.naver?code={target_code}&page={page}"
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            rows = soup.find_all("tr")

            for row in rows:
                cols = row.find_all("td")
                if len(cols) >= 7:
                    a = cols[0].text.strip()
                    b = cols[1].text.strip().replace(",", "")
                    c = cols[2].text.strip().replace(",", "")
                    d = cols[3].text.strip().replace(",", "")
                    e = cols[4].text.strip().replace(",", "")
                    f = cols[5].text.strip().replace(",", "")
                    g = cols[6].text.strip().replace(",", "")
                    
                    if a != "" and f != "":
                        print(f"[{page}페이지] {a} - {b} - {f} - {g}")
                        item.append([a, b, c, d, e, f, g])

        df = pd.DataFrame(item, columns=['날짜', '종가',
             '전일비', '등락률', '거래량', '기관매매량', '외국인매매량'])
        
        filename = f"joosik.csv"
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"{filename} 저장 완료")
    
    if choice == '6':
        break
    else:
        print("잘못된 선택입니다.")
