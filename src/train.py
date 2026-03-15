import numpy as np
from environment import ORANEnvironment
from agent import DRLAgent

def train_rapp():
    env = ORANEnvironment()
    agent = DRLAgent(env.state_dim, env.action_dim)
    
    print("Starting Training for O-RAN Intelligent rApp Optimizer...")
    for epoch in range(20):
        state = env.reset()
        epoch_reward = 0
        
        for step in range(50):
            action = agent.select_action(state)
            next_state, reward, done, _ = env.step(action)
            agent.update(state, action, reward)
            
            state = next_state
            epoch_reward += reward
        
        print(f"Epoch {epoch+1}/20 | Average Reward: {epoch_reward/50:.4f}")

if __name__ == "__main__":
    train_rapp()