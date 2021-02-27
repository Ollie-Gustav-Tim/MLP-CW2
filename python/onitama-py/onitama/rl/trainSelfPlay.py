from onitama.rl import OnitamaEnv, OnitamaSelfPlayEnv, MaskedCNNPolicy, SimpleAgent, RandomAgent
from onitama.rl.eval import EvalCB
from stable_baselines.deepq import DQN
from stable_baselines.common.callbacks import CheckpointCallback, EvalCallback, CallbackList
import argparse


def train_rl(seed):
    env = OnitamaSelfPlayEnv(seed, verbose=False)
    # TODO: SimpleAgent once got working with Random
    eval_env = OnitamaEnv(seed, RandomAgent, verbose=False)
    policy = DQN(MaskedCNNPolicy,
                 env,
                 seed=seed,
                 prioritized_replay=True
                 )
    env.setSelfPlayer(policy)

    checkpoint_callback = CheckpointCallback(save_freq=1e4, save_path='./logs/',
                                             name_prefix='rl_model', verbose=2)
    eval_policy_cb = EvalCB()
    eval_callback = EvalCallback(eval_env, best_model_save_path='./logs/',
                             log_path='./logs/', eval_freq=500,
                             deterministic=True, render=False,
                                 evaluate_policy_callback=eval_policy_cb)
    callback = CallbackList([checkpoint_callback, eval_callback])
    policy.learn(int(1e6), callback=callback)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', default=12314, type=int)
    args = parser.parse_args()

    train_rl(args.seed)
