Bayesian Optimization
---------------------

https://research.sualab.com/introduction/practice/2019/02/19/bayesian-optimization-overview-1.html https://research.sualab.com/introduction/practice/2019/04/01/bayesian-optimization-overview-2.html

**AutoML의 3가지 방향** 1) Automated Feature Learning </p> 2) Architecture Search</p> 3) Hyper parameter Optimization <- 여기</p>**1. Manual Search** </p> -> 수동으로 하나씩 탐색하여 그 중 가장 최선의 값을 취하는 방식 </p> 1) 가장 직관적으로 손에 잡히는 방식 </p> 2) 그러나 직관에 크게 의존하기 때문에 최선의 결과임을 보장할 수 없음 </p>3) 두 개 이상의 HP를 튜닝할 경우 둘 사이의 상호 영향 관계가 있을 때 이를 보정해 줄 방법이 부재함

**2. Grid Search** </p>-> 일정 구간을 나누어 각각에 대해 성능을 측정한 뒤, 가장 높은 성능을 보이는 HP를 선택함 </p>1) Manual Search에 비해 비교적 균등하고 전역적인 탐색이 가능 </p>2) 탐색 대상 HP를 여러 종류로 가져갈수록 탐색 시간이 기하급수적으로 증가 </p>3) 이전 시행의 성능 결과에 대한 사전 지식이 전혀 반영되지 않음.

**3. Random Search** </p>-> Grid Search와 유사하나, 탐색 대상 구간 내의 후보 HP값들을 랜덤 샘플링을 통해 선정함. </p>1) Grid Search에 비해 불필요한 반복을 대폭적으로 줄일 수 있음 </p>2) 동시에 정해진 간격 사이에 위치한 값들에 대해서도 확률적으로 탐색이 가능함. </p>3) 이전 시행의 성능 결과에 대한 사전 지식이 전혀 반영되지 않음.

**4. Bayesian Optimization** </p>

1) 기존의 Bayesian Optimization의 의미 </p>: 입력값 x를 받는 미지의 목적함수 f를 상정하여 그 함숫값 f(x)를 최대로 만드는 최적해 x'를 찾는 것을 목적으로 함 </p>: 일반적으로 목적함수의 표현식을 명시적으로 알지 못할 때(i.e. black-box function) 하나의 함숫값 f(x)를 계산하는 데 오랜 시간이 소요되는 경우를 가정함 </p>: 가능한 한 적은 수의 입력값 후보들에 대해서만 그 함숫값을 순차적으로 조사하여, f(x)를 최대로 만드는 최적해 x'를 빠르고 효과적으로 찾는 것이 주요 목표.</p>

2) 두가지 필수 요소  
- **Surrogate Model**:  
현재까지 조사된 입력값-함숫값 점들 (x_1,f(x_1)), ... , (x_t,f(x_t))를 바탕으로 미지의 목적함수의 형태에 대한 확률적인 추정을 수행하는 모델을 이름. </p>-> 가장 많이 사용되는 확률 모델: Gaussian Process </p>-> 그 외에 사용되는 모델: Tree-structured Parzen Estimators(TPE), Deep Neural Networks

-	**Acquisition Function**:  
	목적 함수에 대한 현재까지의 확률적 추정 결과를 바탕으로, "최적 입력값 x*를 찾는 데 있어 가장 유용할만한" 다음 입력값 후보 x_t+1을 추천해주는 함수를 지칭.

[Gaussian Process] </p> 1) 특정 변수에 대한 확률분포를 표현하는 일반적인 확률분포와는 달리, 모종의 함수들에 대한 확률분포를 나타내기 위한 확률 모델 </p> 2) 그 구성 요소들 간의 결합 분포(joint distribution)가 가우시안 분포(gaussian distribution)를 따른다는 특징이 있음 </p> 3) GP는 평균함수 mu와 공분산 함수 k를 사용하여 함수들에 대한 확률분포를 표현 </p> 4) 현재까지 조사된 입력값-함숫점들 (x_1,f(x_1)), ... , (x_t,f(x_t))를 바탕으로, 목적함수에 대한 확률적 추정을 다음과 같이 수행 </p> 5) (x_1,f(x_1)), ... , (x_t,f(x_t))를 기준으로 x 위치별 평균과 표준편차를 나타냄. </p> 6) mu의 경우 조사된 지점을 모두 지나가게 그 형태가 결정됨 </p> 7) 조사 지점부터 가까울 경우 표준편차가 작고, 멀수록 큼. 이는 조사된 점으로부터 먼 x일수록 해당 지점에 대해 추정한 평균값의 추정의 불확실성이 크다는 의미를 내포함.</p> 8) 조사된 점의 갯수가 증가할수록 목적함수의 추정결과에 대한 불확실성이 감소되었다는 것을 의미 -> 해당 경향이 강해질수록 목적함숫값을 최대로 만드는 입력값 x*를 제대로 찾을 가능성이 계속해서 높아질 것으로 짐작 가능.

3) Acquisition Function  
-> exploitation: 가장 높은 지점의 주변에 최대값이 있을 것이라 가정하고 주변을 추천하는 전략 </p>-> exploration: 불확실성인 표준편차가 가장 큰 영역을 추가로 탐색하는 전략 </p>-> 이 두가지 전략은 trade-off, 따라서 이 상대적 강도를 조절하는 것이 필요함. </p>-> 아래에서는 EI를 사용, 그러나 그 중 PI만을 사용하는 방법과 UCB (Upper Confidence Bound), ES(Entropy Search) 등의 방법이 존재 -> MAB에서 사용되는 방법들

4) Expected Improvement (EI) </p>-> exploitation과 exploration을 내재적으로 일정수준 포함하도록 설꼐된 함수. </p>-> 지금까지 추정된 목적 함수를 바탕으로, 후보 입력값 x에 대해 다음 두가지를 종합적으로 고려하여 해당 입력값 x의 유용성을 나타내는 숫자를 출력함.</p> - 현재까지 조사된 점들의 목표함수 함숫값 중 최대 함숫값보다 더 큰 함숫값을 도출할 확률 (Probability of Improvement) </p>- 그 함숫값과 기존 최대 함숫값 간의 차잇값(magnitude) </p>- PI 값에 magnitude를 가중하여 EI 값을 계산.
