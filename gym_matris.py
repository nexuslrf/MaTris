from matris import *
from actions import ACTIONS
import numpy as np
import gym
from gym import error, spaces, utils
from gym.utils import seeding

class MatrisEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, no_display=True):
        if not no_display:
            pygame.init()
            pygame.display.set_caption("MaTris")

            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        else:
            self.screen = None
        self.game = Game()
        self.game.gym_init(self.screen)

        self.action_list = ACTIONS
        self.action_space = spaces.Discrete(len(ACTIONS))

        # self.timepassed = 20

    def step(self, action_id):
        timepassed = self.game.clock.tick(50)
        # timepassed = 20
        reward = self.game.matris.step_update(self.action_list[action_id], timepassed/1000)
        done = self.game.matris.done
        state = self.game.matris.get_state()
        info = None
        return reward, done, state, info

    def reset(self):
        self.game.gym_init(self.screen)

    def render(self, mode='human', close=False):
        if close:
            self.game.matris.gameover()
            return
        if self.game.matris.needs_redraw and self.screen:
            self.game.redraw()

if __name__ == "__main__":
    env = MatrisEnv(no_display=False)
    for i in range(1000):
        reward, done, state, info = env.step(env.action_space.sample())
        print(f"Reward: {reward}")
        if not done:
            env.render()
        else:
            env.reset()
            
    print("Game over!")