import argparse

import csv

import pandas
import pandas as pd
import numpy

from ohe.encoder import OneHotEncoderBuilder


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_in')
    parser.add_argument('--file_out')
    parser.add_argument(
        '--ignore',
        action='append')
    args = parser.parse_args()
    return args




def main():
    """
  READ FILE_IN_RAW.CSV
  GET COLUMN HEADERS
  FOR EACH COLUMN NOT IN IGNORE LIST :
  GET ALL CATEGORIES = UNIQUE COLUMN VALUES
  GENERATE ONE HOT ENCODING HEADER
  ENCODE EACH ROW WITH 1 or 0 FOR EACH HEADER

      """
    ######################################################################
    #
    # read run commands
    #
    args = parse_command_line()
    file_in_name = args.file_in
    file_out = args.file_out



    ######################################################################

    #
    # OHE
    #
    print("OneHotEncoder --- START ")

    ohe_builder = OneHotEncoderBuilder(file_in_name)
    for ignore in args.ignore:
        ohe_builder.ignore(ignore)
    ohe = ohe_builder.build()
    data_frame, feature_name_list = ohe.one_hot_encode()

    print("data_frame " + str(data_frame))
    print("feature_name_list " + str(feature_name_list))
    ohe.write_ohe_csv(file_out)

    print("OneHotEncoder --- END ")






if __name__ == '__main__':
    main()


