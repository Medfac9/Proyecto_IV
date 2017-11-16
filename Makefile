test:
	cd ./bot/ && coverage run test.py

coverage:
	cd ./bot/ && codecov
