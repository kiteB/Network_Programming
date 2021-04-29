# 코루틴 함수 내에서 다른 코루틴 실행하기
# - await: 해당 코루틴이 끝날 때까지 기다린 뒤 결과를 반환
import asyncio


async def add(a, b):
    print('add: {0} + {1}'.format(a, b))
    await asyncio.sleep(1)              # 1초 대기. asyncio.sleep도 네이티브 코루틴
    return a + b                        # 두 수를 더한 결과 반환


async def print_add(a, b):
    result = await add(a, b)            # await로 다른 네이티브 코루틴 실행하고 반환값을 변수에 저장
    print('print_add: {0} + {1} = {2}'.format(a, b, result))


loop = asyncio.get_event_loop()             # 이벤트 루프를 얻음
loop.run_until_complete(print_add(1, 2))    # print_add가 끝날 때까지 이벤트 루프를 실행
loop.close()
