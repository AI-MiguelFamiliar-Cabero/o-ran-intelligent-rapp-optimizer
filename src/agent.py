import torch
import torch.nn as nn
import torch.optim as optim

class DRLAgent(nn.Module):
    \"\"\"
    Deep Reinforcement Learning agent (Actor-Critic inspired) for 
    autonomous resource optimization in O-RAN rApps.
    \"\"\"
    def __init__(self, state_dim, action_dim):
        super(DRLAgent, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, action_dim),
            nn.Tanh() # Normalized action output
        )
        self.optimizer = optim.Adam(self.parameters(), lr=1e-3)

    def select_action(self, state):
        state_tensor = torch.FloatTensor(state)
        with torch.no_grad():
            return self.network(state_tensor).numpy()

    def update(self, state, action, reward):
        state_tensor = torch.FloatTensor(state)
        action_tensor = torch.FloatTensor(action)
        reward_tensor = torch.FloatTensor([reward])
        
        # Simplified policy gradient update
        pred_action = self.network(state_tensor)
        loss = nn.MSELoss()(pred_action, action_tensor) * (-reward_tensor)
        
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        return loss.item()