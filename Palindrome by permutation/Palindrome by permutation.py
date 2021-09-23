"""
<< 아이디어 >>
: 문자열이 짝수던, 홀수던 가운데를 기준으로 대칭이면 된다는 생각에서부터 알고리즘을 떠올렸다.

두개의 리스트를 준비한다.
- 문자열을 입력받을 리스트
- 짝이 없는 문자를 담을 리스트 (편의상 싱글리스트)

문자열을 입력받아서,
문자열의 길이만큼 for문을 돌면서
만약 싱글리스트에 없다면 싱글리스트에 넣고,
싱글리스트에 있다면 싱글리스트에서 삭제한다.
(싱글에 이미 준비되어 있다면 짝이 있다는 개념)

끝까지 돌았을 때 싱글리스트에 2개 이상 남아있다면 palindrome을 만들 수 없다.
0개 남아있다면 짝수 길이의 문자열이 들어와서 모두 짝이 있는 경우이고,
1개 남아있다면 홀수 길이의 문자열이 들어와서 1개를 제외하고 모두 짝이 있는 경우이다.

<< 수행시간 >>
입력받은 문자열을 한번씩만 확인하면 되므로, O(n)
"""


def Palindrome(input_string):
    # 짝이 없는 문자열
    single = []

    size = len(input_string)
    for i in range(size):
        if input_string[i] not in single:
            single.append(input_string[i])
        else:
            single.remove(input_string[i])

    if len(single) > 1:
        return False
    else:
        return True

# 입력받은 문자열
input_string = list(input())
print(Palindrome(input_string))