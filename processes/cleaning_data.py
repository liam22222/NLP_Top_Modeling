## Imports
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


def load_csv(file_name):
    """
    Parameters
    ----------
    file_name - a prameter that the function gets

    Returns
    -------
    returns a data frame
    """
    df = pd.read_csv(file_name, low_memory=False, encoding='UTF-8', lineterminator='\n', error_bad_lines=False)
    return df


def get_number_of_rows(dataframe):
    """

    Parameters
    ----------
    dataframe - the function gets dataframe

    Returns
    -------
    returns number of rows in the dataframe
    """
    return dataframe.shape[0]


def get_number_of_columns(dataframe):
    """

    Parameters
    ----------
    dataframe - the function gets dataframe

    Returns
    -------
    returns number of columns in the dataframe
    """
    return dataframe.shape[1]


def get_rows_in_range(dataframe, first_row, last_row):
    """

    Parameters
    ----------
    dataframe - the function gets dataframe
    first_row - the functions gets first row
    last_row - the function gets last row

    Returns
    -------
    returns a df with the following indexes
    """
    return dataframe.iloc[first_row:last_row]


def get_columns_in_range(dataframe, first_column, last_column):
    """
    Parameters
    ----------
    dataframe - the function gets dataframe
    first_column - the functions gets first row
    last_column - the function gets last row

    Returns
    -------
    returns a df with the following indexes
    """
    return dataframe.iloc[:, first_column:last_column]


def select_rows_w_vals_in_range(dataframe, col_name, lower_range, higher_range):
    """
    Parameters
    ----------
    dataframe - the function gets dataframe
    col_name - the column we want to filter
    lower_range - low range of the column
    higher_range - high range of the column

    Returns
    -------
    returns rows in a range of one column with specific values
    """
    return dataframe[dataframe[col_name].between(lower_range, higher_range)]


def drop_columns_in_range(dataframe, lower_range, higher_range):
    """
    Parameters
    ----------
    dataframe - the function gets dataframe
    lower_range - low range of the column
    higher_range - high range of the column

    Returns
    -------
    returns filtered dataframe after dropped cols in certain range
    """
    df_copy = dataframe.copy()
    cols = df_copy.iloc[:, lower_range:higher_range]
    df_copy.drop(cols, axis=1, inplace=True)
    print("deleted cols:", cols)
    return df_copy


def update_col_to_bin_vals(dataframe, col, value_1, value_2):
    """
    Parameters
    ----------
    dataframe - the function gets dataframe
    col - the column on which we want to change its values to binary
    value_1 - giving a value to replace
    value_2 - giving a value to replace

    Returns
    -------
    returns df with formated binary column
    """
    df_copy = dataframe.copy()
    df_copy[col] = df_copy[col].replace(to_replace=value_1, value=1)
    df_copy[col] = df_copy[col].replace(to_replace=value_2, value=0)
    print("Col changed to 1/0:", col)
    return df_copy


def dropping_single_value_cols(dataframe):
    """
    Parameters
    ----------
    dataframe - the function gets dataframe

    Returns
    -------
    return df without columns with single value
    """
    df_copy = dataframe.copy()
    df_copy_cols = df_copy.loc[:, df_copy.nunique() == 1].columns
    df_copy.drop(df_copy_cols, axis=1, inplace=True)
    print("Deleted cols:\n", df_copy_cols)
    return df_copy





# n_rows = get_number_of_rows(gram_df)
# print("number of rows is :", n_rows)
#
# n_cols = get_number_of_columns(gram_df)
# print("number of cols is :", n_cols)
# print(gram_df.head())