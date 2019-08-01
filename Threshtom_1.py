import pylab
from skimage import io
from skimage.filters import threshold_otsu, threshold_adaptive
import glob

# Open and crop images
for image in glob.glob('*.tif'): 
    file_name = str(image)
    image = io.imread(image,as_gray=True)
    pylab.imshow(image)
    pylab.show()
    m,n =image.shape
    print(m ,n)
    m_input = int(input("Crop y value :")) # Crop size usually 50 but depends on size scale-bar
    image_crop = image[0:m-m_input, 0:n]
    m,n =image_crop.shape
    areaimage = m*n
    print("The area of the cropped image is :",  areaimage) 

#Manual global threshold
    pylab.hist(image_crop.ravel(), 256)
    pylab.show()
    thresh_value = int(input("Input threshold value: "))
    image_manual = image_crop > thresh_value
    pylab.imshow(image_manual)
    pylab.show()
    areacatalyst = image_manual.sum()
    coverage_manual = float(areacatalyst) / areaimage * 100
    print("For manual thresh, the coverage is (%): ", "%.2f" % coverage_manual)

#Global Otsu method
    T = threshold_otsu(image_crop)
    image_otsu = image_crop > T
    pylab.imshow(image_otsu, cmap='Blues')
    pylab.savefig('Otsu ' + file_name, format ='tiff', dpi = 400)
    pylab.show()
    areacatalyst = image_otsu.sum()
    coverage_otsu = float(areacatalyst) / areaimage * 100
    print("For Otsu thresh, the coverage is (%): ", "%.2f" % coverage_otsu)

#Adaptive thresholding
    block_size = 39
    image_adaptive = threshold_adaptive(image_crop, block_size, offset=10)
    pylab.imshow(image_adaptive, cmap='Purples')
    pylab.savefig('Adaptive ' + file_name, format ='tiff', dpi = 400)
    pylab.show()
    areacatalyst = image_adaptive.sum()
    coverage_adaptive = float(areacatalyst) / areaimage * 100
    print("For adaptive thresh, the coverage is (%): ", "%.2f" % coverage_adaptive)    

#Plot images
    fig, axes = pylab.plt.subplots(nrows=3, figsize=(7, 8))
    ax0, ax1, ax2 = axes

    ax0.imshow(image_manual)
    ax0.set_title('Manual global thresholding', fontsize=15)
    ax0.text(70, 70, "Coverage= " "%.2f" % coverage_manual, style='italic', color='white',
             fontsize=10, bbox={'facecolor':'black', 'alpha':0.5, 'pad':10})

    ax1.imshow(image_otsu)
    ax1.set_title('Otsu global thresholding')
    ax1.text(70, 70, "Coverage= " "%.2f" % coverage_otsu, style='italic', color='white',
             fontsize=10, bbox={'facecolor':'black', 'alpha':0.5, 'pad':10})

    ax2.imshow(image_adaptive)
    ax2.set_title('Adaptive thresholding')
    ax2.text(70, 70, "Coverage= " "%.2f" % coverage_adaptive, style='italic', color='white',
             fontsize=10, bbox={'facecolor':'black', 'alpha':0.5, 'pad':10})

    for ax in axes:
        ax.axis('off')

    pylab.show()
     

    
