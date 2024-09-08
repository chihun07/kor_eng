import random
import time

History_List = {
    'Year': [
        37, 58, 75, 90, 96, 121, 147, 158, 167, 172, 
        191, 210, 227, 245, 259, 268, 270, 274, 284, 292,
        298, 302, 313, 327, 334, 342, 355, 369, 371, 374,
        384, 395, 400, 408, 412, 419, 427, 435, 444, 453,
        469, 475, 482, 491, 496, 502, 512, 519, 529, 539
    ],
    'Correct': [
        '고구려 건국 (주몽에 의해 건국)', 
        '고구려 동명왕 사망', 
        '고구려의 영토 확장 시작', 
        '태조왕 즉위', 
        '고구려의 연나라와 전쟁 시작',
        '동천왕 즉위', 
        '동천왕 사망', 
        '봉상왕 즉위', 
        '미천왕 즉위', 
        '낙랑군 공격 시작',
        '낙랑군 정복', 
        '고구려의 북쪽 영토 확장', 
        '서안평 점령', 
        '연나라와 전쟁 종료', 
        '고국원왕 즉위', 
        '고구려의 백제와 전쟁 시작', 
        '백제의 공격으로 피해 입음', 
        '고국원왕 사망', 
        '소수림왕 즉위', 
        '소수림왕, 불교 수용',
        '율령 반포', 
        '태학 설립', 
        '소수림왕 사망', 
        '고국양왕 즉위', 
        '광개토대왕 즉위', 
        '고구려의 영토 확장 최전성기', 
        '광개토대왕 사망', 
        '장수왕 즉위', 
        '평양 천도', 
        '장수왕, 한강 유역 정복',
        '장수왕 사망', 
        '문자명왕 즉위', 
        '고구려와 신라의 연합', 
        '백제와 전쟁 재개', 
        '백제의 수도 사비 공격', 
        '백제와 신라의 동맹', 
        '백제의 사비 천도', 
        '고구려의 후연 정복', 
        '고구려의 신라 공격', 
        '백제의 신라 지원',
        '안장왕 즉위', 
        '고구려의 중흥 시도', 
        '안원왕 즉위', 
        '고구려의 정치 안정', 
        '양원왕 즉위', 
        '고구려의 경제 발전', 
        '평원왕 즉위', 
        '고구려의 문화 발전', 
        '영양왕 즉위', 
        '고구려의 수나라와 전쟁'
    ],
    'Fake': [
        '남진 정책 실패', 
        '수도를 상주로 이전', 
        '왕이 부여로 망명', 
        '북방 정복 실패', 
        '신라와 동맹 파기',
        '첫 해군 창설', 
        '내부 반란', 
        '중앙 집권제 강화 실패', 
        '새로운 수도 건설', 
        '왕이 백제에 사로잡힘',
        '대외 무역 봉쇄', 
        '새로운 군사 전략 채택', 
        '왕이 신라에 망명', 
        '새로운 법 제정 실패', 
        '내부 반란 진압 실패', 
        '외교 정책 전면 수정', 
        '경제 쇠퇴', 
        '왕이 일본으로 망명', 
        '신도시 건설 실패', 
        '새로운 종교 도입 실패',
        '북방 영토 상실', 
        '남방 진출 시도', 
        '왕이 북방으로 도피', 
        '전쟁 전략 실패', 
        '문화 혁신 실패', 
        '새로운 왕조 설립 실패', 
        '군사 혁신 실패', 
        '수도 이전 실패', 
        '대규모 토목 사업 실패', 
        '해상 무역 확대 시도 실패',
        '내분 발생', 
        '북방 민족 연합 시도 실패', 
        '왕이 북방으로 망명', 
        '외교적 고립', 
        '경제 회복 실패', 
        '왕이 백제에 망명', 
        '새로운 법 제정 성공', 
        '문화 쇠퇴', 
        '내정 개혁 실패', 
        '군사 동맹 체결 실패',
        '왕이 신라에 망명', 
        '외교 정책 실패', 
        '경제 쇠퇴', 
        '새로운 수도 건설 실패', 
        '왕이 일본에 망명', 
        '신도시 건설 성공', 
        '새로운 종교 도입 성공', 
        '남방 영토 상실', 
        '문화 혁신 성공', 
        '새로운 왕조 설립 성공'
    ]
}

def countdown():
    print("3초 뒤 문제가 나옵니다.")
    for i in range(3, 0, -1):
        time.sleep(1)

def History(History_List, add, fail, countdown):
    random_index = random.randint(0, len(History_List['Year']) - 1)
    chosen_Year = History_List['Year'][random_index]
    chosen_Correct = History_List['Correct'][random_index]
    Option = random.sample(History_List['Fake'], 4)
    Option.append(chosen_Correct)
    random.shuffle(Option)
    Correct_index = Option.index(chosen_Correct)

    countdown()
    print(f"\n== 고구려에서 {chosen_Year}년에 일어난 일을 고르시오! ==\n")
    for i in range(5):
        print(f"{i + 1}. {Option[i]}")

    while True:
        answer_input = input('정답을 입력해 주세요 (숫자 또는 "나가기"/"넘기기" 입력): ')

        if answer_input.lower() == "나가기":
            return add, fail, False
        elif answer_input.lower() == "넘기기":
            return add, fail, True
        elif answer_input.isdigit() and 1 <= int(answer_input) <= 5:
            if int(answer_input) == Correct_index + 1:
                print("정답입니다!")
                add += 1
                print(f"정답 {add}/50")
                print(f"오답 {fail}")
                del History_List['Year'][random_index]
                del History_List['Correct'][random_index]
            else:
                print("틀렸습니다...")
                fail += 1
                print("한번 더 풀어보세요!")
                if fail <= 30:
                    continue
                print("공부 하고 와서 풀어보는걸 추천해요....")
        else:
            print("유효한 숫자를 입력해 주세요 (1-5)")

    return add, fail, True

add = 0
fail = 0
print("'나가기'를 입력하면 종료됩니다.")

while History_List['Year']:
    add, fail, continue_game = History(History_List, add, fail, countdown)
    if not continue_game:
        print("게임을 종료합니다.")
        break

if not History_List['Year']:
    print("모든 단어를 맞추셨습니다!")
