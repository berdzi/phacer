
# create folders nofaces,selfies,group in teh same folder as photos 

import argparse
import sys
import os
import shutil

import numpy as np
import cv2 as cv

def countFaces(fname,detector):
	img_file = fname
	img1 = cv.imread(cv.samples.findFile(img_file))
	img1Width = int(img1.shape[1]*scale_factor)
	img1Height = int(img1.shape[0]*scale_factor)

	img1 = cv.resize(img1, (img1Width, img1Height))

	detector.setInputSize((img1Width, img1Height))

	faces = detector.detect(img1)
		
	if faces[1] is None:
		faces_number = 0
	else:	
		faces_number = len(faces[1])

	return faces_number

def getFilesList(directory):
	files = []
	for root, dirs, filenames in os.walk(directory):
		for filename in filenames:
			if not filename.endswith(".jpg"):
				continue
			files.append(os.path.join(root, filename))

	return files

if __name__ == '__main__':

	fdmodel = "face_detection_yunet_2023mar.onnx"
	scale_factor=0.25
	score_threshold=0.9
	nms_threshold=0.3
	top_k=5000
	

	## [initialize_FaceDetectorYN]
	detector = cv.FaceDetectorYN.create(
	
	fdmodel,
	"",
	(320, 320),
	score_threshold,
	nms_threshold,
	top_k
	)
	
	files = getFilesList(sys.argv[1])
	for f in files:	
		bf = os.path.basename(f)	
		print(bf)
		if os.path.exists("selfies/"+bf):
			continue
		if os.path.exists("nofaces/"+bf):
			continue
		if os.path.exists("group/"+bf):	
			continue
		c = countFaces(f,detector)
		
		if c==0:			
			shutil.copy(f, "nofaces/"+bf)
		elif c>=1 and c<=2:
			shutil.copy(f, "selfies/"+bf)
		else:
			shutil.copy(f, "group/"+bf)
