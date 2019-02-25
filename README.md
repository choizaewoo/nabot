# 나이키 코리아 구매 봇입니다.
봇을 돈주고 사서 그들만의 리그를 도저히 보다 못해 우리도 봇으로 경쟁한다는 목표를 가지고 개발.  
실착러들의 권익을 위해 무료로 만들어서 배포.

## 필요 스펙.
1. 크롬
2. 크롬 웹드라이버 http://chromedriver.chromium.org/
3. python 3.7 https://www.python.org/
4. selenium 
  명령창 : pip install selenium

## 사용 방법.
- 크롬 웹 드라이버를 nabot.py와 동일한 경로에 위치
- config.txt에 자신의 나이키id, password, 신발 사이즈, 구매하고자 하는 url 설정
- config.txt의 is_time_check 는 오전 10:00가 될때까지 대기할지 여부를 설정  
  => False는 대기하지 않는다.
  
## 팁.
오전 9:55분쯤 실행하여 10시가 되면 자동으로 동작하도록 하고,
카드결제창이 뜰때 잽싸게 구매.

