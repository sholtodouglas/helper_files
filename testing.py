import reacher_mod

import gym
import time
env = gym.make('reacher_mod-v0')
env.render(mode='human')
env.reset()
env.camera_adjust()

for i in range(0,1000):
	env.step(env.action_space.sample())
	
	