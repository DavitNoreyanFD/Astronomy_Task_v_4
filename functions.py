"""
This is the module where all the functions that work in the script are concentrated.
"""
from random import randint
import datetime
import const_and_inp
import stars


def open_tsv(data_tsv, fov_ra: float, fov_dec: float, ra_user_input: float, dec_user_input: float) -> list:
    """
    in order not to load memory, the function checks if the star enters the field of view and then adds to array.
    the function generates an error if there is a mismatch in the main database, for example, if it is not possible
    to convert the column value to float, an error appears that indicates the line where the error was found, and the
    function also gives an error if the path to the database is not specified correctly data
    """
    fov_ra_min = ra_user_input - fov_ra / 2
    fov_ra_max = ra_user_input + fov_ra / 2
    fov_dec_min = dec_user_input - fov_dec / 2
    fov_dec_max = dec_user_input + fov_dec / 2
    try:
        with open(data_tsv) as fd:
            list_of_db = []
            index = 0
            row_error = 0
            for row in fd:
                index += 1
                list_row = row.split('\t')
                try:
                    if fov_ra_min < float(list_row[const_and_inp.INDEX_RA]) < fov_ra_max and \
                            fov_dec_min < float(list_row[const_and_inp.INDEX_DEC]) < fov_dec_max:
                        list_of_db.append(
                            stars.Star(
                                int(list_row[const_and_inp.INDEX_ID]),
                                float(list_row[const_and_inp.INDEX_RA]),
                                float(list_row[const_and_inp.INDEX_DEC]),
                                float(list_row[const_and_inp.INDEX_MAG])
                            )
                        )
                except ValueError:
                    row_error += 1
                    if row_error > 2:
                        print(f'there is an incorrectness in the database row. row index : {index}')
    except FileNotFoundError:
        raise Exception(f'the specified path to the database is not correct: {data_tsv}')

    return list_of_db


def quicksort(array: list, key, reverse: bool) -> list:
    """
a quicksort sorting algorithm that takes an array, key, and sort direction and returns a sorted array
    """
    if len(array) < 2:
        return array
    left = []
    same = []
    right = []
    delimiter = key(array[randint(0, len(array) - 1)])

    for item in array:
        value = key(item)
        if value > delimiter:
            if reverse is False:
                left.append(item)
            else:
                right.append(item)
        elif value == delimiter:
            same.append(item)
        elif value < delimiter:
            if reverse is False:
                right.append(item)
            else:
                left.append(item)
    sorted_array = quicksort(left, key, reverse) + same + quicksort(right, key, reverse)

    return sorted_array


def n_high_mag(array: list, num: int) -> list:
    """
functions strips out num elements from array
    """
    return array[:num]


def my_key_mag(item):
    return item.mag


def my_key_dist(item):
    return item.distance


def create_result(star_array: list):
    """
the function is designed to create the final output as a .csv file,
the file name is the date and time of the current time
    """
    with open(f'{datetime.datetime.now()}.csv', 'w') as csv_temp:
        head = 'ID'.center(20) + ',' + \
               'RA'.center(20) + ',' + \
               'DEC'.center(20) + ',' + \
               'MAG'.center(20) + ',' + \
               'DISTANCE'.center(20) + '\n'
        csv_temp.write(head)
        for star in star_array:
            row = f'{star.id}'.center(20) + ',' + \
                  f'{star.ra}'.center(20) + ',' + \
                  f'{star.dec}'.center(20) + ',' + \
                  f'{star.mag}'.center(20) + ',' + \
                  f'{star.distance}'.center(20) + '\n'
            csv_temp.write(row)
