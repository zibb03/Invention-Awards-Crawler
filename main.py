from bs4 import BeautifulSoup
import urllib.request
import csv

award_list = []


def crawler(data, page=11, filename ="award_data.csv"):
    for i in range(1, page):
        print(str(i) + ' 페이지')

        # 전국학생과학발명품경진대회
        # url = 'https://www.science.go.kr/mps/1075/bbs/424/moveBbsNttList.do?page=' + str(i) + '&searchCnd=&aditfield10=&aditfield8=&searchKrwd='

        # 전국과학전람회
        url = 'https://www.science.go.kr/mps/1079/bbs/423/moveBbsNttList.do?page=' + str(i) + '&searchCnd=&aditfield10=&aditfield4=&searchKrwd='

        webpage = urllib.request.urlopen(url)
        soup = BeautifulSoup(webpage, 'html.parser')

        table = soup.find_all('tbody', class_='singlerow')

        if table:
            rows = table

            for row in rows:
                columns = row.find_all('td')

                if len(columns) == 7:
                    number = columns[0].text.strip()
                    year = columns[1].text.strip()
                    field = columns[2].text.strip()
                    title = columns[3].text.strip()
                    award = columns[4].text.strip()
                    teacher = columns[5].text.strip()
                    winner = columns[6].text.strip()

                    title = title.replace(u'\xa0', u' ')

                    award_info = {
                        '번호': number,
                        '연도': year,
                        '분야': field,
                        '제목': title,
                        '수상': award,
                        '지도교사': teacher,
                        '수상자': winner
                    }
                    award_list.append(award_info)

    fieldnames = award_list[0].keys()  # 첫 번째 딕셔너리의 키를 헤더로 사용

    try:
        with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()  # 헤더 행 쓰기
            writer.writerows(award_list)  # 데이터 행 쓰기

        print(f"'{filename}' 파일에 성공적으로 저장되었습니다.")

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    crawler(award_list)
