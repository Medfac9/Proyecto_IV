webdriver:
	wget https://github.com/mozilla/geckodriver/releases/download/v0.16.1/geckodriver-v0.16.1-linux64.tar.gz
	sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.16.1-linux64.tar.gz -O > /home/usr/bin/geckodriver'
	sudo chmod +x /home/usr/bin/geckodriver
	rm geckodriver-v0.16.1-linux64.tar.gz

test:
	cd ./bot/ && python3 test.py
