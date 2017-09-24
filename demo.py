import py_kernel_pca
import sklearn.decomposition
from time import time
import numpy as np


gpu_pca = py_kernel_pca.KernelPCA(4)

cpu_pca = sklearn.decomposition.KernelPCA(n_components=4)


print "PCA for 2000x100 matrix. Computing 4 principal components\n\n"

X = np.random.rand(2000,100)

X_f = np.copy(X).astype(np.float32) # make  copy of X, otherwise T1 and T2 share the same reference. Additionally, the gpu pca currently only takes float32 type.i

t0 = time()
T1 = gpu_pca.fit_transform(X_f)
print "GPU PCA compute time = ", (time() - t0)


t1 = time()
T2 = cpu_pca.fit_transform(X)
print "CPU PCA compute time = " , (time() - t1)


print "\n\nOrthogonality Test. All dot products of the resulting principal components should be ~ 0."
print "This is tested by dotting the first and second largest eigenvectors (principal components) of the output for the sklearn's pca and this library's pca."

print "\n\nThis library's GPU PCA: T0 . T1 = ", np.dot(T1[:,0], T1[:,1])
print "sklearns's CPU PCA: T0 . T1 = ", np.dot(T2[:,0], T2[:,1])



