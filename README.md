# **Task for exploring the stars**

The work of the script is as follows - The script takes the path of the
.tsv file, view parameters, a specific direction in the sky and the number
of stars, and as a result produces a list of the brightest stars sorted by
distance from a given point.

Variables are imported into the script using the config.ini file where the following variables are present

**data_file** _is the path of the file that contains the database_

**fov_v** _is one of the parameters of the field of view, in the script it is in accordance with the direction of Right ascension_

**fov_h** _is the second of the field of view parameters, in the script it is in accordance with the Declination direction_

**ra_user** _is one of the coordinates of this direction Right ascension_

**dec_user** _is the second coordinate of the given direction Declination_

**n** _is the number of stars we will explore. If n is not enough 1, then the script will not work and throws exceptions_

**sorting_direction_mag** _is the star sorting vector based on brightness. this variable can take 2 values 0 and any other integer. 
0 if you want to sort from large to small and any other integer if you want to sort from small to large._
_**Please be careful the direction for sorting is specified for additional flexibility and an incorrect variable may lead to an incorrect result**_

**sorting_direction_dist** _is the vector to sort the stars based on the distance to the given point. this variable can take 2 values. 
0 and any other integer. 0 if you want to sort from large to small and any other integer if you want to sort from small to large_

for the correct use of the script, please fill in all the values of the variables correctly