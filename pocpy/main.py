from poc import *
import cv2
import numpy as np
import os
import glob

def main():

    default_shift = np.array([0,0])
    default_angle = np.array(60)
    sArrFilePath = glob.glob('lena/' + '*lena*.jpg')
    
    # load master image
    sFileName = os.path.basename(sArrFilePath[0])
    sTmpFileName_master, sTmpExt = os.path.splitext(sFileName)
    master = cv2.imread('lena/' + sTmpFileName_master + '.jpg',0)
    master = np.double(master)
    img1 = master[slice(int(master.shape[0]/2-256),int(master.shape[0]/2+256)),slice(int(master.shape[0]/2-256),int(master.shape[0]/2+256))]

    # load slave image
    sFileName = os.path.basename(sArrFilePath[0])
    sTmpFileName_slave, sTmpExt = os.path.splitext(sFileName)
    slave = cv2.imread('lena/' + sTmpFileName_master + '.jpg',0)
    slave = np.double(slave)
    rows,cols = slave.shape

    # randomly shift slave image
    M = np.float32([[1,0,default_shift[0]],[0,1,default_shift[1]]])
    slave = cv2.warpAffine(slave,M,(cols,rows))

    # randomly rotate slave image
    center = tuple(np.array(slave.shape[0:2])/2)
    rotMat = cv2.getRotationMatrix2D(center, default_angle, 1.0)
    slave = cv2.warpAffine(slave, rotMat, slave.shape[0:2], flags=cv2.INTER_LINEAR)
    slave_crop = slave[slice(int(master.shape[0]/2-256),int(master.shape[0]/2+256)),slice(int(master.shape[0]/2-256),int(master.shape[0]/2+256))]
    
    img2 = cv2.imread("lena_x59_y16_7.27deg.jpg", 0)
    a,b,angle,scale = ripoc(img1, img2)

    print(angle,scale)

if __name__ == '__main__':

    main()