import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import manifold

# datasets
from sklearn import datasets
data = datasets.fetch_openml('mnist_784', version=1, return_X_y=True)
pixel_values, targets = data
targets = targets.astype(int)

# tSNE
tsne = manifold.TSNE(n_components=2, random_state=7)
transformed_data = tsne.fit_transform(pixel_values[:3000, :])

# dataframe
tsne_df = pd.DataFrame(np.column_stack((transformed_data, targets[:3000])), columns=['x', 'y', 'targets'])
tsne_df.loc[:, 'taarget'] = tsne_df.targets.astype(int)

# visualization
grid = sns.FacetGrid(tsne_df, hue='targets', size=8)
grid.map(plt.scatter, 'x', 'y').add_legend()