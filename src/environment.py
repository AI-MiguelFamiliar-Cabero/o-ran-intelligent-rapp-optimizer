import numpy as np

class ORANEnvironment:
    \"\"\"
    A simulated 5G O-RAN environment for Radio Resource Management (RRM).
    Agents must optimize spectral efficiency and minimize interference
    by adjusting transmission power and beamforming parameters.
    \"\"\"
    def __init__(self, num_cells=5):
        self.num_cells = num_cells
        self.state_dim = num_cells * 3 # [Load, Interference, Latency]
        self.action_dim = num_cells # Power adjustment [-1, 1]
        self.reset()

    def reset(self):
        # Initial network state
        self.state = np.random.uniform(0.3, 0.7, self.state_dim)
        return self.state

    def step(self, actions):
        # Apply actions to transmission power
        power_adjustments = actions * 0.1
        noise = np.random.normal(0, 0.05, self.state_dim)
        
        # Simulate network response (simplified)
        # Higher power -> more interference for neighbors, lower latency for self
        self.state = np.clip(self.state + noise - power_adjustments.repeat(3), 0, 1)
        
        # Reward: Balanced spectral efficiency vs power consumption
        reward = -np.mean(np.square(self.state - 0.5)) - 0.1 * np.mean(np.square(actions))
        
        return self.state, reward, False, {}