import os
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, "sample.yaml")) as file
	env = yaml.load(file, Loader=yaml.FullLoader)
print(env)