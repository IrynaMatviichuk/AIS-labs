import gym
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from QAgent import QAgent


def main():
    env = gym.make("NChain-v0")
    env.env.slip = 0

    action_size = env.action_space.n
    state_size = env.observation_space.n
    parameters = {
        "learning_rate": 0.1,
        "gamma": 0.9,
        "epsilon": 1,
        "decay": 0.008,
    }

    q_agent = QAgent(env, state_size, action_size, parameters)
    q_agent.learn(plot=False, max_steps=50, total_episodes=1000)

    print("Q table:\n", q_agent.q_table)
    with sns.axes_style("whitegrid"):
        plt.figure(figsize=(20, 15))
        sns.lineplot(data=q_agent.episode_rewards)
        plt.show()

    with sns.axes_style("whitegrid"):
        plt.figure(figsize=(20, 15))
        sns.lineplot(data=q_agent.episode_epsilon)
        plt.show()


if __name__ == "__main__":
    main()
