import matplotlib.pyplot as plt
import numpy as np
import io
import base64

# Generate random data
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure()
plt.plot(x, y)
plt.title('Random Example Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Save plot to a PNG image in memory
buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)
img_base64 = base64.b64encode(buf.read()).decode('utf-8')
