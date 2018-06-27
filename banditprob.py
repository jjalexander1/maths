import random
import operator


class Bandit(object):
    #todo write bandit so it updates its payout strategy, rather than having constant mean and random uniform payout
    def __init__(self, name, mean_reward):
        self.name = name
        self.mean_reward = mean_reward
        print('created bandit with mean reward ' + str(self.mean_reward))

    def payout(self):
        return random.uniform(0, 2) * self.mean_reward


def construct_bandits(num_of_bandits):
    bandits_list = []
    for i in range(num_of_bandits):
        reward = random.uniform(0,1)
        name = 'Bandit ' + str(i)
        bandits_list.append(Bandit(name, reward))
    return bandits_list


def greedy_epsilon(bandits, epsilon, iterations=1000):
    def find_max_mean_reward(bandits):
        bandit = []
        for i in bandits:
            bandit.append((i.name, i.mean_reward))
        sorted_bandits = sorted(bandit, key=operator.itemgetter(1), reverse=True)
        return sorted_bandits[0][0] # return the bandit name with highest mean reward

    history = [] # list of all past plays
    iteration = 1
    while iteration <= iterations:
        if random.random() <= epsilon:
            to_play = random.choice(bandits)
        else:
            to_play = find_max_mean_reward(bandits)
        for b in bandits:
            if b.name == to_play:
                history.append((b.name, b.payout(), b.mean_reward))
        iteration += 1
    return history


def calculate_payout(history):
    average_payout = sum(i[1] for i in history)/len(history)
    return average_payout


def calculate_regret(history):
    pass


if __name__ == '__main__':
    bandits = construct_bandits(10)
    history = greedy_epsilon(bandits, 0.2)
    payout = calculate_payout(history)
    print(payout)