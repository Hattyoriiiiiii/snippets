from keras.utils import plot_model
plot_model(model, to_file='model.png', show_shapes=True, show_layer_names=True,
           expand_nested=True, rankdir='TB', dpi=96)