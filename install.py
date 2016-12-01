import configparser 
import os
import sys

ver = (sys.argv[1])
#ver = "20"

os.system("tar -xzvf /home/vm164/temp/API_apiServer_v" + ver + ".tgz -C /home/vm164/temp/")

conf = configparser.ConfigParser()
conf.read("/home/vm164/temp/bundle.ini")

temp = conf.get("settings", "dst")
dest = conf.get("settings", "instDst")

os.system("rm -rf /home/vm164/temp/rabbitmqphp_example/.git")
os.system("cp -R " + temp + "rabbitmqphp_example " + dest)
#print(("cp -R " + temp + "rabbitmqphp_example " + dest))

os.system("rm -r /home/vm164/temp/API_apiServer_v" + ver + ".tgz")
os.system("rm -r /home/vm164/temp/bundle.ini")
os.system("rm -r " + temp + "rabbitmqphp_example")

os.system("echo")
os.system("echo Operation completed successfully.")
os.system("exit")
