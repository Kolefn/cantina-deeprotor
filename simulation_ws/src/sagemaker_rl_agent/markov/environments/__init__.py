from gym.envs.registration import register

MAX_STEPS = 1000

register(
    id='RoboMaker-DeepRotor-v0',
    entry_point='markov.environments.deeprotor_env:DeepRotorDiscreteEnv',
    max_episode_steps=MAX_STEPS,
    reward_threshold=200
)