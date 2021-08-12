import cv2 as cv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
def conversion_image(source_image):
    img=cv.imread(source_image,cv.IMREAD_GRAYSCALE)
    (thresh, im_bw) = cv.threshold(img, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    #0 equivale a espacio abierto, 1 espacio ocupado.

    im_new=np.where(im_bw==255,1.0,0.0)
    np.savetxt('imagennew1.txt',im_new)
    return (im_new)
    
def conversion_image_white(source_image):
    img=cv.imread(source_image,cv.IMREAD_GRAYSCALE)
    
    (thresh, im_bw) = cv.threshold(img, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    #0 equivale a espacio abierto, 1 espacio ocupado.

    im_new=np.where(im_bw==255,0.0,1.0)
    np.savetxt('imagennew1.txt',im_new)
    return (im_new)
def show_results(A,B,C):
    # A = np.loadtxt('imagennew1.txt',dtype=int)
    # B= np.loadtxt('ruta.txt',dtype=int)
    titles = ['Original Image','Ruta Image','Ruta Diagonales']
    images = [A, B,C]
    miArray=np.arange(3)
    for i in miArray:
        plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
    plt.show()

def show_results_two(A,B):
    # A = np.loadtxt('imagennew1.txt',dtype=int)
    # B= np.loadtxt('ruta.txt',dtype=int)
    titles = ['Original Image','Route']
    images = [A, B]
    miArray=np.arange(2)
    for i in miArray:
        plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
    plt.show()
    
def save_individual_image(directory,name,file):
    directory=directory+name
    # np.savetxt(directory,file)
    matplotlib.image.imsave(directory,file)