import numpy as np

from measure_time import measure_time


class QAgent:
    def __init__(self, env, state_size, action_size, parameters):
        self.q_table = np.zeros((state_size, action_size))

        self.learning_rate = parameters.get("learning_rate")
        self.gamma = parameters.get("gamma")
        self.epsilon = parameters.get("epsilon")
        self.decay = parameters.get("decay")

        self.env = env

    @measure_time
    def learn(self, plot=True, max_steps=10, total_episodes=1000):
        self.episode_rewards = np.zeros(total_episodes)
        self.episode_epsilon = np.zeros(total_episodes)

        for episode in range(total_episodes):
            observation = self.env.reset()

            for step in range(max_steps):
                action = self.get_action(observation)
                new_observation, reward, done, info = self.env.step(action)
                self.q_table[observation, action] = self.update_q_table(
                    observation, new_observation, action, reward
                )
                observation = new_observation
                self.episode_rewards[episode] += reward

                if done:
                    break

            self.episode_rewards[episode] /= step
            self.episode_epsilon[episode] = self.epsilon
            self.update_epsilon(episode)

            if episode % 100 == 0:
                print(f"episode: {episode}")

    def update_q_table(self, observation, new_observation, action, reward):
        return self.q_table[observation, action] + self.learning_rate * (
            reward
            + self.gamma * np.max(self.q_table[new_observation, :])
            - self.q_table[observation, action]
        )

    def update_epsilon(self, episode):
        self.epsilon = np.exp(-self.decay * episode)

    def get_action(self, observation):
        if np.random.uniform() >= self.epsilon:
            action = np.argmax(self.q_table[observation, :])
        else:
            action = self.env.action_space.sample()

        return action
