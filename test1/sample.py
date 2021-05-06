import os
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base_env =os.environ.get("NOSE_EN", "sample.yaml")

print(base_env)

with open(os.path.join(BASE_DIR, base_env)) as file:
	env = yaml.load(file, Loader=yaml.FullLoader)
print(env)