# G:\Afame Technologies\src\utils.py
import os
import matplotlib.pyplot as plt

def save_plot(fig, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    fig.savefig(filename, bbox_inches='tight')
    plt.close(fig)
    print(f"Plot saved to {filename}")

def save_metrics(rmse, r2, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        f.write(f'RMSE: {rmse:.4f}\nR2 Score: {r2:.4f}')
    print(f"Metrics saved to {filename}")