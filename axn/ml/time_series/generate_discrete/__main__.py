"""
gen dis
"""
# pylint: disable=invalid-name

import argparse
from datetime import datetime, timedelta
import os


def diff_dates(date1, date2):
    """
    check for least in list
    """
    return abs(date2 - date1).days


description = \
    """
VoterLabs Inc.
Master Control
creates all scripts and excecutes them using this process:
  READ FILE_IN_RAW.CSV
  GET COLUMN HEADERS
  FOR EACH COLUMN NOT IN IGNORE LIST :
  GET ALL CATEGORIES = UNIQUE COLUMN VALUES
  GENERATE ONE HOT ENCODING HEADER
  ENCODE EACH ROW WITH 1 or 0 FOR EACH HEADER
  Then split into test and training sets such that:
  Training data set—a subset to train a model.
  Test data set—a subset to test the trained model.
  Test set MUST meet the following two conditions:
  Is large enough to yield statistically meaningful results.
  Is representative of the data set as a whole.
  Don't pick a test set with different characteristics than the training set.
  Then we train models using Supervised learning.
  Supervised learning consists in learning the link between two datasets:
  the observed data X and an external variable y that we are trying to predict, called target
  Y is a 1D array of length n_samples.
  All VL models use a fit(X, y) method to fit the model and a predict(X)
  method that, given unlabeled observations X, returns the predicted targets y.
      """.strip()


def parse_command_line():
    """
    check for least in list
    """
    # pylint: disable=invalid-name

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        '--file_in',
        help='raw csv file input to be predicted. Must be a csv file where first row has column header names. '
             'Must include time series date columns - like MM/DD/YY (7/3/20) ')
    parser.add_argument('--file_out_discrete',
                        help='raw csv file input to be discretized')
    parser.add_argument(
        '--file_out',
        help='raw csv file input to be discretized')
    parser.add_argument(
        '--discrete_file_script_out',
        help='discretized script make for each time series data directory')
    parser.add_argument(
        '--num_bins',
        help='these are the number of bins to make for all disctrization - like 4000')
    parser.add_argument(
        '--start_date_all',
        help='start of time series window - each step is a day each column must be a date in format MM/DD/YY - like 7/3/20')
    parser.add_argument(
        '--end_date_all',
        help='end of time series window - each step is a day each column must be a date in format MM/DD/YY - like 7/22/20 ')
    parser.add_argument(
        '--window_size',
        help='number of time series increments per window - this is an integet like 4. '
             'This is the sliding window method for framing a time series dataset the increments are days')
    parser.add_argument(
        '--parent_dir',
        help='beginning of docker file system - like /app')

    parser.add_argument(
        '--drop_column',
        action='append',
        help='drop column from discreteize process - BUT not from encoding or prediction')

    args = parser.parse_args()
    return args


def main():
    """
    check for least in list
    """
    # pylint: disable=too-many-locals
    # pylint: disable=invalid-name
    # pylint: disable=too-many-statements
    # pylint: disable=consider-using-sys-exit
    # pylint: disable=invalid-name

    args = parse_command_line()
    file_in = args.file_in
    file_out_discrete = args.file_out_discrete
    file_out = args.file_out

    discrete_file_script_out = args.discrete_file_script_out
    start_date_all = args.start_date_all
    end_date_all = args.end_date_all
    num_bins = args.num_bins
    window_size = args.window_size
    drop_column = args.drop_column

    parent_dir = args.parent_dir
    if parent_dir is None:
        quit()

    start_date_all_window_f = datetime.strptime(start_date_all, "%m/%d/%Y")
    end_date_all_window_f = datetime.strptime(end_date_all, "%m/%d/%Y")

    start_window_date_next = start_date_all_window_f
    end_window_date_next = start_date_all_window_f + \
        timedelta(days=int(window_size))

    while end_window_date_next < end_date_all_window_f:

        start_window_date = start_window_date_next
        end_window_date = end_window_date_next
        time_series = start_window_date.strftime(
            "%m-%d-%Y") + "_" + end_window_date.strftime("%m-%d-%Y")

        directory = time_series

        # Path
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)

        drops = []
        for drop in drop_column:
            drops.append(drop)

        dropsforme = "\\\n".join(f"  --drop_column  {d}" for d in drops)
        start_date_all_f = datetime.strptime(start_date_all, "%m/%d/%Y")
        end_date_all_f = datetime.strptime(end_date_all, "%m/%d/%Y")
        date_drops = []

        while start_window_date > start_date_all_f:
            date_drops.append(start_date_all_f)
            start_date_all_f = start_date_all_f + timedelta(days=1)

        end_date_w_f = end_window_date + timedelta(days=1)
        while end_date_all_f >= end_date_w_f:
            date_drops.append(end_date_w_f)
            end_date_w_f = end_date_w_f + timedelta(days=1)

        dropsdatesforme = "\\\n".join(
            f"  --drop_column  {d.strftime('%m/%d/%Y')}" for d in date_drops)
        dropsdatesforme2 = dropsdatesforme.replace("2020", "20")
        dropsdatesforme3 = dropsdatesforme2.replace("03", "3")
        dropsdatesforme4 = dropsdatesforme3.replace("04", "4")
        dropsdatesforme5 = dropsdatesforme4.replace("05", "5")
        dropsdatesforme6 = dropsdatesforme5.replace("06", "6")
        dropsdatesforme7 = dropsdatesforme6.replace("07", "7")
        dropsdatesforme8 = dropsdatesforme7.replace("01", "1")
        dropsdatesforme9 = dropsdatesforme8.replace("02", "2")
        dropsdatesforme10 = dropsdatesforme9.replace("08", "8")
        dropsdatesforme11 = dropsdatesforme10.replace("09", "9")

        start_date_window_f = start_window_date
        end_date_window_f = end_window_date

        dates = []
        while end_date_window_f >= start_date_window_f:
            dates.append(start_date_window_f)
            start_date_window_f = start_date_window_f + timedelta(days=1)

        options = "\\\n".join(
            f"  --dicretize uniform {num_bins} {d.strftime('%m/%d/%Y')} " for d in dates)
        no = options.replace("/", r"\/")
        no2 = no.replace("2020", "20")
        no3 = no2.replace("03", "3")
        no4 = no3.replace("04", "4")
        no5 = no4.replace("05", "5")
        no6 = no5.replace("06", "6")
        no7 = no6.replace("07", "7")
        no8 = no7.replace("01", "1")
        no9 = no8.replace("02", "2")
        no10 = no9.replace("08", "8")
        no11 = no10.replace("09", "9")

        tscsv = "_" + time_series + ".csv"
        file_out_discrete_ts = file_out_discrete.replace(".csv", tscsv)
        file_out_ts = file_out.replace(".csv", tscsv)

        file_out_discrete_ts_path = path + "/" + file_out_discrete_ts
        file_out_ts_path = path + "/" + file_out_ts

        template = f"""
        #!/usr/bin/env bash
        python -m discrete  \\
          --file_in {file_in} \\
        {dropsforme} \\
            {dropsdatesforme11} \\
          {no11} \\
          --file_out_discrete {file_out_discrete_ts_path} \\
          --file_out {file_out_ts_path}

        """.strip()

        tssh = "_" + time_series + ".sh"
        discrete_file_script_out_ts = discrete_file_script_out.replace(
            ".sh", tssh)
        discrete_file_script_out_ts_path = path + "/" + discrete_file_script_out_ts

        print("discrete_file_script_out_ts ")
        print(discrete_file_script_out_ts_path)
        print(template)
        discrete_text_file = open(discrete_file_script_out_ts_path, "w")
        discrete_text_file.write(template)

        start_window_date_next = start_window_date_next + timedelta(days=1)
        end_window_date_next = start_window_date_next + \
            timedelta(days=int(window_size))
        print("start_window_date_next ")
        print(start_window_date_next)
        print("end_window_date_next ")
        print(end_window_date_next)


if __name__ == '__main__':
    main()
