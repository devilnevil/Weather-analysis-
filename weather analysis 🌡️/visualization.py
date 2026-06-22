import matplotlib.pyplot as plt

def plot_chart(df):
    plt.figure(figsize=(12,6))

    plt.plot(df['Date'],df['Temperature'],label='Temperature',color='red',linewidth=0.7,linestyle='-')

    plt.plot(df['Date'],df['MA7'],label='7-DAY moving average',color='#ff7f0e',linewidth=2.5)

    plt.title('Weather Analysis vs 7 days moving average',
              fontsize=14,fontweight='bold',pad=15)
    plt.legend(loc='upper left',fontsize=12)

    plt.tight_layout()

    plt.show()

