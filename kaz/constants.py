from os.path import dirname, exists, expanduser, join, realpath
import configparser

kaz_home = expanduser(join('~', '.kaz'))

config_path = join(kaz_home, 'config')
script_dir = dirname(dirname(realpath(__file__)))
default_config_path = join(script_dir, 'data', 'default_config')
# Copy default config to user config file if there is no user config
if not exists(config_path):
    with open(default_config_path, 'r') as source, open(config_path, 'w+') as dest:
        dest.write(source.read())

# Read config
config = configparser.ConfigParser()
config.read(config_path)

# Read default config
default_config = configparser.ConfigParser()
default_config.read(default_config_path)

KEY_VALUE_SPACING = int(config['formatting'].get(
    'spacing',
    default_config['formatting']['spacing']))
VERSION='0.4.0'
