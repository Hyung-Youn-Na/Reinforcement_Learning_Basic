from ex010 import BanditTwoArmedHighLowFixed
import numpy as np

env = BanditTwoArmedHighLowFixed()

# the table
count = np.zeros(2)
sum_rewards = np.zeros(2)
Q = np.zeros(2)

def softmax(T):
    denom = sum([np.exp(i/T) for i in Q])
    probs = [np.exp(i/T)/denom for i in Q]
    arm = np.random.choice(env.action_space.n, p=probs)
    return arm

num_rounds = 100000
T = 50
for i in range(num_rounds):
    arm = softmax(T)
    next_state, reward, done, info = env.step(arm)
    count[arm] += 1
    sum_rewards[arm] += reward
    Q[arm] = sum_rewards[arm] / count[arm]
    T = T * 0.9999

print(Q)
print(count)
print('The optimal arm is arm {}'.format(np.argmax(Q)+1))

