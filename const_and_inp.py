"""
All constants and imported variables were collected in this module.
"""

import configparser


config = configparser.ConfigParser()
config.read('config.ini')
data_file = config['USER']['data_file']


try:
    fov_v = float(config['USER']['fov_v'])
    fov_h = float(config['USER']['fov_h'])
    ra_user = float(config['USER']['ra_user'])
    dec_user = float(config['USER']['dec_user'])
    sorting_direction_mag = int(config['USER']['sorting_direction_mag']) != 0
    sorting_direction_dist = int(config['USER']['sorting_direction_dist']) != 0
    n = int(config['USER']['n'])
except ValueError as e:
    raise Exception('invalid variable '+str(e))

if n < 1:  # condition checks the value of n so that the script does not start working if there is no object to use
    raise Exception('the number of stars must be greater than Zero for the script to work')

INDEX_ID = 7
INDEX_RA = 0
INDEX_DEC = 1
INDEX_MAG = 22
INDEX_FLUX = 20
