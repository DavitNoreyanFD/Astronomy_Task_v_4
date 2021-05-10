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
