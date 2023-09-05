import numpy as np
import scipy.io

# Parameters
n = 128  # number of pixels in each dimension
t_max = 300  # maximum time of flight
t = np.arange(1, t_max+1)  # time vector
r = 5 * np.ones((n, n))  # target intensity/amplitude
b = np.ones((n, n))  # background/dark photon level
g = lambda x: np.exp(-x**2/3**2)  # Gaussian impulse response

# Depth map
depth_map = scipy.io.loadmat('Depth_CameraMan.mat')['CameraMan']  # load Cameraman image
t_ij = depth_map / 255 * t_max  # scale to [0, t_max]

#Question 1
# Generate data cube
s = np.zeros((n, n, t_max))
for i in range(n):
    for j in range(n):
        s[i, j, :] = r[i, j] * g(t - t_ij[i, j]) + b[i, j]
        
        
#Question 2
# Generates noisy data cube
y = np.random.poisson(s)

#Question 3
# Matched filtering to estimate depth map
t_hat = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        y_vec = y[i, j, :]
        xcorr_g_y = np.correlate(g(t), y_vec, mode='same')
        max_idx = np.argmax(xcorr_g_y)
        t_hat[i, j] = t[max_idx]

#Question 4
# Display clean and estimated depth maps
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(depth_map, cmap='gray', vmin=0, vmax=t_max)
plt.title('Clean Depth Map')
plt.colorbar()
plt.subplot(1, 2, 2)
plt.imshow(t_hat, cmap='gray', vmin=0, vmax=t_max)
plt.title('Estimated Depth Map')
plt.colorbar()
plt.show()

#The depth map of the estimated image can be improved by using  a more pratical
#impulse response to model response of the LIDAR system. A deep learning/ 
#machine learning approachcan be used to determine the depth map estimation.

