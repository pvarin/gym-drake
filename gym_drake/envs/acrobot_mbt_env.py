import numpy as np

from multi_body_tree_env import MultiBodyTreeEnv


class AcrobotMBTEnv(MultiBodyTreeEnv):
    def __init__(self):
        # Call super-class constructor
        print('AcrobotMBTEnv init')
        super(AcrobotMBTEnv, self).__init__("models/acrobot.sdf")

    @property
    def action_limits(self):
        return (np.array([-2.0]), np.array([-2.0]))

    @property
    def observation_limits(self):
        return (np.array([-np.inf, -np.inf]),
                        np.array([np.inf, np.inf]))

    @property
    def dt(self):
        return 0.1

    def get_reward(self, state, action):
        '''
        Subclasses should implement their own reward functions
        '''
        return 1 # TODO


if __name__ == "__main__":
    AcrobotMBTEnv()
