# poker

Project goal: Build an automated poker player which learns via machine learning and is capable of playing on websites


	Steps:
  	1. Build automated poker player for a single site without ML
    		- This will use python and selenium to perform actions on the site
    		- Understanding the current context (e.g. what cards you have) will be done via reading the 
				HTML Canvas element as an image file, then performing OCR on it
				- Decision engine will just be hardcoded, no ML at this point
  	2. Change decision engine from hardcoded rules to ML
				- TensorFlow will be used. Further details TBD.
