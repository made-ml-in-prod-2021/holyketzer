import yaml

CONFIG_FILE = "configs/config.yaml"

def load_config():
    with open(CONFIG_FILE) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        return yaml.load(file, Loader=yaml.FullLoader)

config = load_config()
