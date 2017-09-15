import sys
import argparse
import json
from pprint import pprint

def main():
    """ Main entry point for the script."""
    # parse the config file
    parser = argparse.ArgumentParser(description='Entrypoint.')
    parser.add_argument('config_file', nargs=1,
                    help='path to configuration file')

    args = parser.parse_args()
    print "Reading config file: ", args.config_file[0]

    with open(str(args.config_file[0])) as data_file:    
      config = json.load(data_file)
    # pprint(data)    
    
    print "Configuring role: ", config['role'] 
    
    entrypoint.users.setup_users 
 
    pass

if __name__ == '__main__':
    sys.exit(main())
