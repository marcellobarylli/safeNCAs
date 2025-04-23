import matplotlib.pyplot as plt
import numpy as np
import sys

def plot_learning_curve(progress_file='out.progress'):
    """Plots the learning curve from a .progress file."""
    try:
        # Load data, skipping lines that might cause errors if columns mismatch
        data = np.loadtxt(progress_file, usecols=(0, 1), comments='#', encoding='utf-8')
        if data.ndim == 1: # Handle case with only one data point
            print(f"Warning: Only one data point found in {progress_file}. Cannot plot curve.")
            return
        if data.shape[0] < 2:
             print(f"Warning: Less than two data points found in {progress_file}. Cannot plot curve.")
             return
             
        evaluations = data[:, 0]
        best_fitness = data[:, 1]

        plt.figure(figsize=(10, 6))
        plt.plot(evaluations, best_fitness, marker='.', linestyle='-')
        plt.title(f'Learning Curve from {progress_file}')
        plt.xlabel('Evaluations')
        plt.ylabel('Best Fitness So Far')
        plt.grid(True)
        plt.tight_layout()
        
        # Save the plot
        plot_filename = progress_file.replace('.progress', '_learning_curve.png')
        plt.savefig(plot_filename)
        print(f"Learning curve saved to {plot_filename}")
        # plt.show() # Uncomment to display the plot interactively

    except FileNotFoundError:
        print(f"Error: Progress file '{progress_file}' not found.")
    except Exception as e:
        print(f"An error occurred while plotting: {e}")

if __name__ == "__main__":
    # Allow specifying a different progress file via command line argument
    file_to_plot = sys.argv[1] if len(sys.argv) > 1 else 'out.progress'
    plot_learning_curve(file_to_plot) 