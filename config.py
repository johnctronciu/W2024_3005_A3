#File to read configuration settings, Boilerplate code

from configparser import ConfigParser

def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser() #Class to read and write to .ini files
    parser.read(filename) #Read configs (user, host, password, DB Name...)

    # get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section) # Get all parameters
        for param in params: #iterate over
            config[param[0]] = param[1] #Set key to value i.e. 'password = [YOUR PASSWORD]'
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config

if __name__ == '__main__':
    config = load_config()
    print(config)