import gym_maze
import gymnasium as gym
import random

env = gym.make("maze-sample-5x5-v0", enable_render=True)

env.reset()
env.render()

done = False
while not done:
    state, reward, done, _, info = env.step(random.choice([0, 1, 2, 3]))
    env.render()
    print(reward)
