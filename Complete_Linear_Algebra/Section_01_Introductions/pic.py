import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# import picture
pic = Image.open('Einstein_tongue.jpg')

# convert to floating-point precision
pic = np.array(pic)

# SVD (singular value decomposition)

# do the SVD. Note: You'll understand this decomposition by the end of the
# course! Don't worry if it seems mysterious now!
U, S, V = np.linalg.svd(pic)

# plot the spectrum
#plt.plot(S,'s-')
#plt.xlim([0,100])
#plt.xlabel('Component number')
#plt.ylabel('Singular value (\sigma)')
#plt.show()

# reconstruct the image based on some components

# list the components you want to use for the reconstruction
# use only the first 4 largest features
comps = np.arange(0, 5)

# reconstruct the low-rank version of the picture
reconPic = U[:,comps]@np.diag(S[comps])@V[comps,:]

# show the original and reconstructed pictures for comparison
plt.figure(figsize=(5,10))
plt.subplot(1, 2, 1)
plt.imshow(pic, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(reconPic, cmap='gray')
plt.title('Components %s-%s' %(comps[0], comps[-1]))
plt.axis('off')

plt.show()
