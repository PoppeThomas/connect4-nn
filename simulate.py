# Run this file to show a simulated game on the screen.
from learning.NNStrategy import NNStrategy
from learning.RandomStrategy import RandomStrategy
from learning import GameSimulator

nn_strategy = NNStrategy()
nn_strategy.load_model()
random_strategy = RandomStrategy()
GameSimulator.simulate_game(nn_strategy, nn_strategy)
