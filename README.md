TIL
===

> Today I Learned - :memo: 오늘 배운 것들을 기록합니다.

오늘 배운 것들, 새롭게 찾은 사실들, 복습한 내용, 우연히 찾은 해결의 실마리 등을 기록합니다.

A collection of what I learned day by day, what I found interesting today, what I reviewed today, and what I come up with as a hint of solution on my recent or old problems.

---

### Categories

##### Main Languages

-	[Python](/python)
-	[R](/R)
-	[SQL](/sql)

##### Machine Learning

-	[Statistics](/statistics)
-	[Mathematics](/math)
-	[Classical Machine Learning](/classicalml)
-	[Hyperparameter Optimization](/hptuning)
-	[Recommender Systems](/Recsys)
-	[NLP (Natural Language Preprocessing)](/NLP)
-	[MAB (Multi Armed Bandits)](/MAB)
-	[Image processing](/imageprocessing)
-	[Graph Neural Network](/graphnetworks)
-	[Data preprocessing](/preprocessing)
-	[Anormaly detection](/anormaly)

##### Other tools for ML

-	[Visualization](/Visualization)
-	[XAI (eXplainable AI)](/XAI)

##### Miscellaneous

-	[Git](/git)
-	[Linux](/linux)
-	[Vim](/vim)
-	[VS Code](/vscode)
-	[Google Colab](/colab)
-	[Jupyter](/jupyter)
-	[markdown](/markdown)
-	[LaTex](/latex)
-	[Algorithms](/algorithms)
-	[Computer Science](/cs)
-	[Database](/db)
-	[Web](/web)
<!-- ### Python -->

<!-- - [-](ack/ack-bar.md) -->



[최적 모델 선정 로직 변경]
-> 에러 발생으로 인해 최적 모델 선정이 이루어지지 않는 현상을 방지하기 위해 설정한 예외 처리 구문 수정


[기타 유종 예측 모델 에러 처리]

Found unknown categories [53] in column 3 during transform
-> one-hot encoding 시 encoder의 학습에 발견되지 않은 공휴일 정보가 예측용 test 데이터에 포함될 경우 발생하는 오류
-> 학습에 사용된 공휴일 피처만 모델 예측에 활용할 수 있도록, one-hot encoder의 parameter로 "handle_unknown='ignore'"을 추가

