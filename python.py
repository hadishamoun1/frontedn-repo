import yaml

with open('config.yaml', 'r') as stream:
    config = yaml.safe_load(stream)

if config['run_localhost']:
    print("Running in localhost mode.")
else:
    print("Not running in localhost mode.")
