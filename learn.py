# Run this file to generate a lot of games and learn from their outcomes.
from learning.RandomStrategy import RandomStrategy
from learning import GameGenerator, GameSimulator
from learning.NNStrategy import NNStrategy

learning_strategy = NNStrategy()
learning_strategy.load_model()
random_strategy = RandomStrategy()
playing_strategy = random_strategy
# while True:
for i in range(10000):
    # print("Measuring performance of learning strategy...")
    # nb_wins_vs_random = GameSimulator.match_strategies(learning_strategy, random_strategy)
    # print("Learning strategy wins " + str(nb_wins_vs_random) + "% of the games against the random strategy")
    print("Learning...")
    GameGenerator.generate(1000, 1000, learning_strategy, playing_strategy, playing_strategy)
    print("Saving model...")
    learning_strategy.save_model()
