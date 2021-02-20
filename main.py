import os,sys
from subprocess import Popen
from json import load,dumps

with open('./config.json','r',encoding='utf-8') as f:
	bots_config = load(f)

p_list = []
for config in bots_config['bots']:
	config_str = dumps(config,ensure_ascii=False)
	p_list.append(Popen([bots_config['python-script'],'runner.py',config_str]))

input()

for process in p_list:
	process.terminate()
	while not process.poll():
		pass