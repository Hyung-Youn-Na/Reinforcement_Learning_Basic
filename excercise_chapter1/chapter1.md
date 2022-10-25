# 강화학습 청강 수업 요약

* 강화학습의 기본 개념: 경험으로 부터 보상을 받고, 보상이 최대화 되는 방향으로 action을 정하는 방식
* 강화학습의 기본 용어
  * Agent: 합리적인 결정을 내리도록 학습되는 소프트웨어 프로그램 예시) 체스 선수, 마리오 게임의 마리오
  
  * Environment: 용어 그대로 Agent가 존재하는 환경, 예시) 체스판, 마리오 월드
  
  * State: Agent를 포함한 환경의 어떤 한 순간의 snapshot, 예시) 체스 기물들의 위치와 보드판의 상태, 마리오 월드맵의 순간적인 상황
  
  * Action: Agent 취한 행동, 움직임, 예시)체스 기물을 특정위치로 이동
  
  * Action Space: 가능한 action들의 집합
    * Discrete action space: up, down, left, right 처럼 이산구조로 Action이 구성되어 있는 경우
    * Continuous action space: 자율주행 차의 속도 조절과 같은 연속적인 구조로 Action이 구성된 경우
  
  * Reward: Action으로 받는 피드백, 예시) 상대편의 체스 기물을 제거하거나, 마리오 월드의 목표점에 도달하는 것
  
  * Policy: Agent가 environment에서 어떻게 행동할지 정의하는 것(정책)
    * Deterministic Policy: 특정 state에서 수행할 action을 하나만 정하는 것 <-> Stochastic Policy
    * Stochastic Policy: 가능한 action중에서 확률적으로 골라 수행하는 것 <-> Deterministic Policy
  
  * episode: 처음 state에서 종료 state까지 environment와 주고받은 상호작용(수행한 action까지 포함하여), 종종 trajectory라고 부름
  
  * Return: episode에서 획득한 reward의 총합
    * Discount Factor: Terminate state가 딱히 존재하지 않는 continous task에서는 reward가 무한대로 증가하므로 episode가 진행될수록 reward가 감소하게 되는 인자를 넣음(0~1사이 소수)
        
* 다른 학습 방법들간의 차이점
  * Supervised Learning
    * Label이 존재하는 Dataset(input, label)을 통해 학습
    * 모델은 Label과 input관의 관계를 학습
  * Unsupervised Learning
    * Label이 존재하지 않는 Dataset을 학습
    * 학습된 모델은 data를 clustering 하던가 이질적인 데이터를 찾는데 사용할 수 있음
  * Reinforcement Learning
    * Agent는 action을 취하는 것을 통해 주어진 environment와 상호작용
    * Agent는 이전 episode에서 좋은 action을 취했을 때 reward를 통해 학습
    
* Markov  Property and Markov Chain
  *  Markov Decision Process(MDP)
     * optimization 문제를 풀기 위한 mathematical framework
     * RL에서도 문제를 해결하기 위해 사용
  * Markov Property
    * 미래가 과거에 독립적인 조건
    * A memoryless property 라고 부름
  * Markov Chain (Markov Process)
    * Markov Property를 만족하는 연속된 State
    * 확률 모델이 다음 확률을 예측하는데 현재 state에만 의존하는 모델
    * 예시) '오늘이 흐리니 내일은 비가 올것 같다.'
  
   