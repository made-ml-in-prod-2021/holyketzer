from src.config import config

def test_config():
    assert isinstance(config, dict)
