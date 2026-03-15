# 📶 O-RAN-Intelligent-rApp-Optimizer

[![MLOps Training Pipeline](https://github.com/AI-MiguelFamiliar-Cabero/o-ran-intelligent-rapp-optimizer/actions/workflows/ml-pipeline.yml/badge.svg)](https://github.com/AI-MiguelFamiliar-Cabero/o-ran-intelligent-rapp-optimizer/actions)

A professional blueprint for **AI-driven Network Automation** in Open RAN (O-RAN) architectures. This repository demonstrates a **Deep Reinforcement Learning (DRL)** rApp designed to autonomously optimize 5G radio resources, ensuring spectral efficiency and interference management.

## 🌟 Vision
In the era of 5G and 6G, network complexity exceeds human manual optimization capabilities. This project showcases the **Autonomous Network** vision: replacing static configurations with dynamic, cloud-native AI agents that learn and adapt to real-time traffic conditions.

## 🏗 Key Features
- **O-RAN Environment Simulator:** A high-fidelity simulation (src/environment.py) modeling 5G cell load, interference, and latency.
- **Deep RL Agent:** A PyTorch-based Actor-Critic architecture (src/agent.py) that computes optimal power adjustments for autonomous resource management.
- **MLOps Lifecycle:** Integrated CI/CD via GitHub Actions to automate model training and validation, ensuring repeatable and scalable AI workflows.

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- PyTorch
- NumPy

### Installation
`ash
git clone https://github.com/AI-MiguelFamiliar-Cabero/o-ran-intelligent-rapp-optimizer.git
cd o-ran-intelligent-rapp-optimizer
pip install -r requirements.txt
`

### Running the Optimizer
To observe the AI engine optimizing the 5G environment:
`ash
export PYTHONPATH=pwd/src
python src/train.py
`

## 🛠 Project Structure
- src/environment.py: O-RAN simulation and reward modeling.
- src/agent.py: Deep RL agent architecture.
- src/train.py: Training loop and MLOps-driven simulation controller.
- .github/workflows/: CI/CD configuration for the AI pipeline.

## 🤝 Contributing
This project is an open framework for discussing the future of **Autonomous Operations** and **Cloud-Native AI**. Contributions in the areas of **Intent-based Networking** and **Multi-Agent Systems (MAS)** are welcome.

---
*Developed by **Miguel Familiar-Cabero, PhD**, Core Network AI Director @ Ericsson.*