# cv
##### 마하밴드
### 연산(Operation)
##### 합성곱(Convolution) 연산자
##### 프리윗 엣지 연산자
##### 소벨 엣지 연산자
### 효과(Effect)
##### 동시대비효과
##### 표본화(Sampling)
##### 양자화(Quantizing)
##### 평활화(Smoothing)
##### 나이키스트-새넌의 표본화 정리
### 함수(Function)
##### 점 확산 함수(Point Spread Function)
### 필터(Filter)
##### 저역통과 필터(low-pass filter)
##### 쌍방 필터(Bilateral Filter)
##### 중간값 필터(Median Filter)
### 검출기
#### 엣지(Edge)
##### 마르-힐드레스 엣지 검출기
##### 캐니 엣지 검출기 https://koreascience.kr/article/JAKO201134036350233.pdf
##### 1. 스무딩smoothing(블러blur) : 노이즈 제거 -> 가우시안 필터 사용 (함수 속의 함수 : 고차함수)
##### 2. 그레디언트gradient : 경사(=미분)값을 통해서 에지를 찾는다
##### 3-1. 노름norm(강도)를 구한다 -> 피타고라스 정리 이용
##### 3-2. 디렉션direction(방향)을 구한다 -> 삼각함수
##### 4. 극한값과 임계값을 구한다
##### 5. 엣지트래킹
##### or
##### 1. 스무딩(블러): 가우시안 필터를 이용한 노이즈 제거한다
##### 2. 그레디언트: 소벨필터를 이용한 그래디언트의 크기(intensity)를 찾는다
##### 3. Non-maximum suppression을 적용하여 거짓 반응을 제거한다.
##### 4. 경계선으로써 가능성 있는 픽셀을 골라내기 위해 double threshold 방식을 적용한다.
##### 5. 앞서 double threshold 방식에서 maxVal을 넘은 부분을 strong edge, minVal과 maxVal 사이의 부분을 weak edge로 설정하여 strong edge와 연결되어 있는 weak edge를 edge로 판단하고 그렇지 않는 부분은 제거한다. (Hysteresis thresholding)
### 잡음(Noise)
##### 가우시안 잡음(Gaussian Noise)
##### 점 잡음(Salt-And-Pepper Noise) https://www.google.com/search?q=Salt-And-Pepper+Noise&sxsrf=ALiCzsY-hf4FLI_sce-4NqD98nkk5WSBvA:1667267437020&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjqx9Ca74v7AhXHTmwGHbjYBh8Q_AUoAXoECAEQAw&biw=1920&bih=969&dpr=1#imgrc=SjMpGIat1Vcx0M
### 수학적 형태학
##### 적중-비적중 변환
##### 세션화
### 구조화 요소
##### 침식
##### 팽창
##### 열기
##### 닫기
### 이진화
##### 전역 임계치 결정
##### 적응적 임계치 결정
### 영상처리
##### HoG(Histogram of Oriented Gradient) 서술자
##### blob(Binary Large Object)
##### LoG(Laplacian of Gaussian)
##### DoG(Difference of Gaussian)
##### SIFT(Scale Invariant Feature Transform)
##### 동차좌표
##### k-d 트리
##### RANSAC(RANdom SAmple Consensus)