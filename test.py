from bs4 import BeautifulSoup
import urllib.request
import csv

'''
award_list = []

webpage = urllib.request.urlopen('https://www.science.go.kr/mps/1075/bbs/424/moveBbsNttList.do?page=1&searchCnd=&aditfield10=&aditfield8=&searchKrwd=')
soup = BeautifulSoup(webpage, 'html.parser')

# table = soup.find('table')
table = soup.find_all('tbody', class_='singlerow')
# print(table)

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
            # award_info = {
            #     number,
            #     year,
            #     field,
            #     title,
            #     award,
            #     teacher,
            #     winner
            # }
            award_list.append(award_info)

print(award_list)

# for i in award_list:
#     print(i)
'''


award_list = []
filename="award_data.csv"

for i in range(1, 2038):
    print(str(i) + ' 페이지')

    # 전국학생과학발명품경진대회
    # url = 'https://www.science.go.kr/mps/1075/bbs/424/moveBbsNttList.do?page=' + str(i) + '&searchCnd=&aditfield10=&aditfield8=&searchKrwd='

    # 전국과학전람회
    url = 'https://www.science.go.kr/mps/1079/bbs/423/moveBbsNttList.do?page=' + str(i) + '&searchCnd=&aditfield10=&aditfield4=&searchKrwd='
    # print(url)

    webpage = urllib.request.urlopen(url)
    # webpage = urllib.request.urlopen('https://www.science.go.kr/mps/1075/bbs/424/moveBbsNttList.do?page=1&searchCnd=&aditfield10=&aditfield8=&searchKrwd=')
    soup = BeautifulSoup(webpage, 'html.parser')

    # table = soup.find('table')
    table = soup.find_all('tbody', class_='singlerow')
    # print(table)

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
                # award_info = {
                #     number,
                #     year,
                #     field,
                #     title,
                #     award,
                #     teacher,
                #     winner
                # }
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

# for i in award_list:
#     print(i)


# table = soup.find('div', "table-round").get_text().strip().replace('현재 온도', '')
# table = soup.find('table', "table-round").get_text().split()

# table = np.array(table).reshape(6)

# print(table)
#print(len(table))

# def start():
#     webpage = urllib.request.urlopen('https://www.science.go.kr/mps/1075/bbs/424/moveBbsNttList.do')
#     soup = BeautifulSoup(webpage, 'html.parser')
#
#     table = soup.find('div', "temperature_text").get_text().strip().replace('현재 온도', '')
#
#     temperature_info = soup.find('div', "temperature_info")
#
#     summary_list = soup.find('dl', attrs={'class':'summary_list'})
#     humidity = summary_list.find_all('dd')[1].get_text().strip()
#     wind = summary_list.find_all('dd')[2].get_text().strip()
#
#     direction_text = summary_list.find_all('dt')[2].get_text().strip().replace('바람(', '')
#     direction = direction_text.replace(')', '')
#
#     report_card = soup.find('div', "report_card_wrap")
#
#     item1 = report_card.find('li', attrs={'class': 'item_today level1'})
#     a1 = item1.find('span', attrs={'class': 'txt'}).get_text().strip()
#
#     item2 = report_card.find('li', attrs={'class': 'item_today level2'})
#     a2 = item2.find('span', attrs={'class': 'txt'}).get_text().strip()
#
#     web_index = [temperature, humidity, direction, wind, a2, a1]
#     # print(web_index)
#     return web_index


# webpage = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8')
# soup = BeautifulSoup(webpage, 'html.parser')
#
# temperature = soup.find('div', "temperature_text").get_text().strip().replace('현재 온도', '')
#
# temperature_info = soup.find('div', "temperature_info")
#
# summary_list = soup.find('dl', attrs={'class':'summary_list'})
# humidity = summary_list.find_all('dd')[1].get_text().strip()
# wind = summary_list.find_all('dd')[2].get_text().strip()
#
# direction_text = summary_list.find_all('dt')[2].get_text().strip().replace('바람(', '')
# direction = direction_text.replace(')', '')
#
# report_card = soup.find('div', "report_card_wrap")
#
# item1 = report_card.find('li', attrs={'class':'item_today level1'})
# a1 = item1.find('span', attrs={'class':'txt'}).get_text().strip()
#
# item2 = report_card.find('li', attrs={'class':'item_today level2'})
# a2 = item2.find('span', attrs={'class':'txt'}).get_text().strip()
#
# print(a2, a1)

'''
import requests
from bs4 import BeautifulSoup

def crawl_science_award(url):
    """
    과학전람회 수상작 페이지에서 정보를 크롤링합니다.

    Args:
        url (str): 크롤링할 웹페이지 URL.

    Returns:
        list: 각 수상작에 대한 '번호', '연도', '분야', '제목', '수상', '지도교사', '수상자' 정보를 담은 딕셔너리 리스트.
              크롤링 실패 시 빈 리스트를 반환합니다.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTPError 발생 시 예외 처리
        soup = BeautifulSoup(response.text, 'html.parser')
        award_list = []
        table = soup.find('table', class_='board_list')
        if table:
            rows = table.find('tbody').find_all('tr')
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
        return award_list
    except requests.exceptions.RequestException as e:
        print(f"크롤링 오류: {e}")
        return []
    except AttributeError:
        print("테이블 구조를 찾을 수 없습니다.")
        return []

if __name__ == "__main__":
    target_url = "https://www.science.go.kr/mps/1075/bbs/424/moveBbsNttList.do"
    award_data = crawl_science_award(target_url)
    if award_data:
        for data in award_data:
            print(data)
    else:
        print("크롤링된 데이터가 없습니다.")
'''