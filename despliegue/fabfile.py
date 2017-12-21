from fabric.api import *

def instalarProyecto():
	run('git clone https://github.com/Medfac9/Proyecto_IV')
	run('cd ./Proyecto_IV && sudo pip3 install -r requirements.txt')

def subirApi():
    run('nohup sudo -E python3 home/ubuntu/Proyecto_IV/flask_api.py', pty=False)

def borrarApi():
	run('sudo rm -rf ./Proyecto_IV')

def MatarApi():
    run('sudo pkill python3')