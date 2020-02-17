from os.path import exists

from tensorflow_core.python.keras import Sequential
from tensorflow_core.python.keras.layers import Conv2D, Flatten, Dense
from tensorflow_core.python.keras.models import load_model
from game.Constants import NB_COLUMNS, NB_ROWS, COMPUTER

MODEL_FILE_NAME = 'connect4-nn.h5'


# My first attempt at letting a Convolutional Neural Network learn from playing games against itself.
class NNStrategy:

    def __init__(self):
        self.model = None

    # Load the previously saved model from disk, or create a new model if the saved model cannot be found.
    def load_model(self):
        if exists(MODEL_FILE_NAME):
            self.model = load_model(MODEL_FILE_NAME)
        else:
            print("Model does not exist yet - creating a new one")
            self.__create_model()

    # Saves the updated model to disk.
    def save_model(self):
        self.model.save(MODEL_FILE_NAME)

    def __create_model(self):
        new_model = Sequential()
        new_model.add(Conv2D(32, kernel_size=7, padding='same', activation='relu', input_shape=(NB_ROWS, NB_COLUMNS, 1)))
        new_model.add(Conv2D(64, kernel_size=4, padding='valid', activation='relu'))
        # new_model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        new_model.add(Flatten())
        new_model.add(Dense(30, activation='relu'))
        new_model.add(Dense(1, activation='tanh'))
        new_model.compile(optimizer='adam', loss='mean_squared_error')
        self.model = new_model

    # Given the n x 43 dimensional training data (n board states of 42 positions + a score), updates
    # the internal neural network to learn from the examples.
    def learn_from(self, train_data):
        X_train = train_data[:, 0:NB_COLUMNS * NB_ROWS].reshape(train_data.shape[0], NB_ROWS, NB_COLUMNS, 1)
        y_train = train_data[:, NB_COLUMNS * NB_ROWS: NB_COLUMNS * NB_ROWS + 1]
        # Initially, I'm trying 1 epoch to not over-train on badly played games, but since generating
        # games is currently a lot slower than learning from them, I might want to experiment with this setting
        self.model.fit(X_train, y_train, epochs=1)

    # Predict the score for the given board state (for which the given player made the last move).
    def __predict_value(self, player, board):
        if player == COMPUTER:
            # The computer just played, so we're looking at the board state from the right perspective
            return self.model.predict(board.state.reshape(1, NB_ROWS, NB_COLUMNS, 1))
        else:
            # The computer simulated the human turn, so we need to inverse the board before estimating the value
            adapted_board_state = -1 * board.state.copy().reshape(1, NB_ROWS, NB_COLUMNS, 1)
            return self.model.predict(adapted_board_state)

    # Given that it's the given player's turn, return the column in which this strategy thinks it needs
    # to play to maximize the next board state's value.
    def next_move(self, player, board):
        legal_moves = board.get_legal_moves()
        max_value = float('-inf')
        best_col = -1
        for col in legal_moves:
            board.play(player, col)
            value = self.__predict_value(player, board)
            board.undo(col)
            if value > max_value:
                max_value = value
                best_col = col
        return best_col

