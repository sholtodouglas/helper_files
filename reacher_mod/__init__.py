from gym.envs.registration import register

register(
    id='reacher_mod-v0',
    entry_point='reacher_mod.envs:ReacherBulletEnv',
)