import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,4))

ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(np.log10(amount_ng), te(colony_1), color='g', label='LB+Amp')
ax1.plot(np.log10(amount_ng), te(colony_4), color='r', label='LB+Amp+Ara')
ax1.set_title("形質転換効率")
ax1.set_xlabel("$log_{10}$(プラスミド量(ng))")
ax1.set_ylabel("TE")
ax1.grid(True)
ax1.legend()


ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(np.log10(amount_ng), tf(colony_1, colony_3 * 1e5), color='g', label='LB+Amp')
ax2.plot(np.log10(amount_ng), tf(colony_1, colony_4 * 1e5), color='r', label='LB+Amp+Ara')
ax2.set_title("形質転換頻度")
ax2.set_xlabel("$log_{10}$(プラスミド量(ng))")
ax2.set_ylabel("TF")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
# fig.savefig('')
plt.show()