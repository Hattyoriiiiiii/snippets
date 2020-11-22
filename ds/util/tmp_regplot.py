import seaborn as sns
sns.set(style="darkgrid")  #, palette='pastel'
import warnings
warnings.simplefilter('ignore')

plt.rcParams['font.family'] = 'IPAexGothic'

plt.rcParams["figure.figsize"] = [20, 12]
plt.rcParams['font.size'] = 40 
plt.rcParams['xtick.labelsize'] = 10 
plt.rcParams['ytick.labelsize'] = 10


fig, ax = plt.subplots(figsize=(8, 5), linewidth=10, edgecolor='white') #, facecolor='pink'
# ax.plot(x_means, y_means)
ax.set_xlim(0, 32500)
ax.set_ylim(-0.1, 1.2)


sns.scatterplot(y_means, x_means, s=50, palette='black', alpha=1)
# sns.regplot(x, y, order=1, scatter=False, color="green", fit_reg=True, label='data1', ci=95) #, truncate=True
sns.regplot(x, y, order=2, scatter=False, color="green", fit_reg=True, label='data1', ci=95) #, truncate=True

#ax.collections.clear(9

plt.title('図1. 増殖曲線', fontsize=18)
plt.xlabel('細胞数(cells)')
plt.ylabel('吸光度(Abs.)')
#plt.grid()
plt.legend()

# plt.savefig('増殖曲線_mean_scr.png')
plt.show()