import random
import time

Eng_list = {
    'Eng': [
        'free', 'life', 'flow', 'important', 'however', 'tap water', 'avoid', 'near', 'charity',
        'care', 'beg', 'journey', 'source', 'cliff', 'think', 'skip', 'breakfast', 'know',
        'despite', 'jar', 'must', 'actually', 'killed', 'decade', 'disease', 'Africa', 'ultimately',
        'relationship', 'try', 'clean', 'ability', 'protect', 'planet', 'recommend', 'interested',
        'waste', 'annoying', 'sign', 'sink', 'save', 'mean', 'environmentally friendly', 'annoyed',
        'close', 'car', 'park', 'backpack', 'love', 'follow', 'watch', 'eat', 'turn', 'find',
        'would', 'marry'
    ],
    'Kor': [
        '무료', '삶', '흐르다', '중요한', '그렇기는 하지만', '수돗물', '피하다', '가까운', '자선단체',
        '신경쓰다', '간청하다', '여정', '수원', '절벽', '생각하다', '거르다', '아침식사', '알다',
        '에도 불구하고', '항아리', '해야 한다', '실제로', '죽임을 당한', '10년', '질병', '아프리카', '궁극적으로',
        '관계', '노력하다', '깨끗하게 하다', '능력', '보호하다', '행성', '추천하다', '관심있는',
        '낭비하다', '짜증나는', '표지', '싱크대', '아끼다', '의미하다', '환경 친화적인', '짜증난',
        '가까운', '차', '주차하다', '배낭', '사랑하다', '따라가다', '보다', '먹다', '돌다', '찾다',
        '~할 것이다', '결혼하다'
    ]
}

correct = 0
Hint = 0

def next():
    print("\n다음 문제 준비중...\n")
    time.sleep(0.5)

def Eng(Eng_list, correct, Hint, next):
    random_index = random.randint(0, len(Eng_list['Eng']) - 1) #Eng_list에 Eng에서 랜덤으로 인덱스 값을 뽑아온다
    random_word = Eng_list['Eng'][random_index] #뽑은 인덱스 값을 이용해서 단어와 매칭 시킨다
    random_kor = Eng_list['Kor'][random_index]
    hint_index = random.randint(0, len(random_kor) - 1) #랜덤으로 선택된 단어에서 랜덤으로 인덱스 값을 뽑아 한 단어를 저장한다
    random_hint_kor = list(random_kor)
    for i in range(len(random_kor)): #기존에 뽑은 단어와 랜덤으로 선택된 알파벳의 인덱스를 읽어 빈곳에 _을 넣는다
        if random_kor[i] != random_hint_kor[hint_index]:
            random_hint_kor[i] = '_'
    random_hint_kor = ''.join(random_hint_kor) #저장한다
    next() #쉬는 시간
    print(f"랜덤 단어!: {random_word}")
    while True:
        answer = input("정답을 입력해 주세요: ")
        if answer == "힌트":
            Hint += 1
            print(f"랜덤 글자: {random_hint_kor}")
            continue
        break

    if answer == random_kor:
        correct += 1
        print(f"정답입니다. {correct}/55")
        print(f"힌트 사용 {Hint}/55")
        del Eng_list['Eng'][random_index]
        del Eng_list['Kor'][random_index]
    else:
        print("오답입니다.")
    return Eng_list,correct, Hint
 
def Kor(next): #위에랑 같다 하지만 여기는 매개변수가 없다
    global Eng_list, correct, Hint
    random_index = random.randint(0, len(Eng_list['Kor']) - 1)
    random_word = Eng_list['Kor'][random_index]
    random_Eng = Eng_list['Eng'][random_index]
    hint_index = random.randint(0, len(random_Eng) - 1)
    random_hint_Eng = list(random_Eng)
    for i in range(len(random_Eng)):
        if random_Eng[i] != random_hint_Eng[hint_index]:
            random_hint_Eng[i] = '_'
    random_hint_Eng = ''.join(random_hint_Eng)
    next()
    print(f"랜덤 단어!: {random_word}")
    while True:
        answer = input("정답을 입력해 주세요: ")
        if answer == "힌트":
            Hint += 1
            print(f"랜덤 글자: {random_hint_Eng}")
            continue
        break

    if answer == random_Eng:
        correct += 1
        print(f"정답입니다. {correct}/55")
        print(f"힌트 사용 {Hint}/55")
        del Eng_list['Eng'][random_index]
        del Eng_list['Kor'][random_index]
    else:
        print("오답입니다.")
    return correct

print("tip!.//힌트// 힌트는 랜덤글자를 알려줍니다..\n tip!. 힌트는 한단어당 한번만....\n  tip!. 나가기. 진행하던걸 멈출수 있음.")
while True:
    choose = input("한글 외우기 or 영어 외우기....한/영: ")
    if choose == "한":
        while Eng_list['Eng']:
            Eng_list, correct, Hint =Eng(Eng_list, correct, Hint,next)
            
        print("모든 단어를 맞추셨습니다!")
        break
    elif choose == '영':
        while Eng_list['Kor']:
            Kor(next)
        print("모든 단어를 맞추셨습니다!")
        break
    else:
        print("잘못된 입력")
