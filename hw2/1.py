# 다음과 같은 게임 프로그램을 작성하라.
# 플레이어가 처음에 $50을 가지고 있다. 동전을 한 번 던져서 앞면(1) 또는 뒷면(2)이 나온다.
# 맞추면 $9을 따고 틀리면 $10을 잃는다. 플레이어가 돈을 모두 잃거나 $100이 되면 게임이 종료된다.
from random import randint
import sys

money = 50  # 플레이어의 돈

while True:
    guess = int(sys.stdin.readline())   # 추측
    coin = randint(1, 2)        # 동전 던지기의 결과

    if money <= 0 or money >= 100:
        break
    else:
        if guess == coin:
            money += 9
        else:
            money -= 10

    # 매 게임마다 결과 출력
    print('guess: {}, coin: {}'.format(guess, coin))
    print('money: {}'.format(money))