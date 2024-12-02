import matplotlib.pyplot as plt
import numpy as np
import io
import base64

def generate_plot(agents, density):
    # Simulate some data based on inputs
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * int(agents) * float(density)

    # Create the plot
    plt.figure()
    plt.plot(x, y, label=f"Agents: {agents}, Density: {density}")
    plt.title("Agent Simulation")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()

    # Save plot to a PNG image in memory
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")

