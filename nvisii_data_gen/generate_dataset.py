#!/usr/bin/env python3
import random 
import subprocess
import os

relative_path = os.path.join("nvisii_data_gen", "single_video_pybullet.py")
num_frames_per_hdri = 10



for i in range(0, 4000):
	to_call = [
		"C:/dope_venv/Scripts/python.exe",relative_path,
		'--spp','10',
		'--nb_frames', str(i * num_frames_per_hdri + num_frames_per_hdri),
		'--nb_objects', '1',#str(int(random.uniform(50,75))),
		'--scale', '0.01',
		'--outf',f"dataset",
		'--initial_index', str(i*num_frames_per_hdri),
		'--hdri_number', str(i),
		'--nb_distractors', str(random.randint(0, 10)),	
	]
	subprocess.call(to_call)