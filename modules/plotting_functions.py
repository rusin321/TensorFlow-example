import matplotlib.pyplot as plt

def plotTrainHistory(history):
  fig, axes = plt.subplots(1, 2, figsize = (7, 3))

  axes[0].plot(history.history['loss'], label = 'train')
  axes[0].plot(history.history['val_loss'], label = 'validation')
  axes[0].set_xlabel('Epoch')
  axes[0].set_ylabel('Loss function')
  axes[0].legend(loc = 'upper right')

  axes[1].plot(history.history['loss'], label = 'train')
  axes[1].plot(history.history['val_loss'], label = 'validation')
  axes[1].set_xlabel('Epoch')
  axes[1].set_ylabel('Loss function')
  axes[1].set_yscale('log')
  axes[1].legend(loc = 'upper right')

  plt.subplots_adjust(bottom = 0.02, left = 0.02, right = 0.98, wspace = 0.6)