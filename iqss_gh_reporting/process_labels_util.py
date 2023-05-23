"""
Functions to read and process the labels in the sized snapshot 
output of the `create_iq_snapshot` process  
"""

# required modules
import re
import os
import pandas as pd

def read_sized_snapshot(filename, sep='\t'):
    """
    Read sized output of the `create_iq_snapshot`

    Parameters
    ----------
    filename : str
        Path of snapshot output to read

    sep : str
        Type of file separator. Default: tab (\t)

    Raise
    -----
    KeyError
    FileNotFoundError
    TypeError (resource is not a file)

    Return
    -------
    DataFrame
    """
    # if path doesn't exist
    if (not(os.path.exists(filename))):
        msg = '{} not found'.format(filename)
        raise FileNotFoundError(msg)

    # if resource is not a file 
    if (not(os.path.isfile(filename))):
        msg = '{} is not a file'.format(filename)
        raise TypeError(msg)
        
    # TODO perform additional file validation, if needed

    return pd.read_csv(filename, sep=sep)

def _parse_labels(labels):
    """
    Parse a string containing labels.
    Local function, do not call externally.

    Parameter
    ---------
    labels : str
        String containing list of comma-separated labels of form:
            Label(name="D: Dataset: large number of files")
    
    Return
    ------
    list
    """
    label_list = labels.split(',')
    names = []
    for label in label_list:
        l = label.strip()
        name_list = re.findall('"(.*?)"', l)
        if (name_list and (len(name_list) > 0)):
            names.append(name_list[0])
    return names

def process_sized_snapshot(df, labels='Labels', key='CardURL'):
    """
    Process a DataFrame derived from a sized sprint snapshot

    Parameters
    ----------
    df : DataFrame
        Output of `read_sized_snapshot`

    labels : str
        Name of the label field in input DataFrame. Default: 'Labels'

    key : str
        Field in DataFrame to use as key. Must be unique in snapshot. 
        Default: ['CardURL]

    Raise
    -----
    ValueError
        DataFrame is empty
    KeyError
        DataFrame is missing the label field or key field
    
    Return
    ------
    DataFrame
    """

    # dataframe cannot be empty
    if (df.empty == True):
        raise ValueError('Empty input DataFrame')
    
    # dataframe must contain labels field
    if (labels not in df):
        msg = 'Missing field: {}'.format(labels)
        raise KeyError(msg)
    
    # dataframe must contain key field
    if (key not in df):
        msg = 'Missing key field: {}'.format(key)
        raise KeyError(msg)
    
    # key field must be unique in dataframe
    if (len(df[key].unique()) != len(df)):
        raise KeyError('Key is not unique')
    
    # get a dict representation of dataframe
    df_dict = df.to_dict('records')

    # create a dict for parsed labels
    # label: Label(name="D: Dataset: large number of files")
    # keyed on parameter: key
    # ex: {'https://github.com/repo/issues/101':[label_1, label_2, label_3]}
    parsed_labels = {}

    # list of records, one dataframe row per record
    records = []

    # process each row in the copied dataframe
    for count, row in df.iterrows():
        # get key value 
        key_value = row.get(key)
        # get label str 
        label_str = row.get(labels)
        # if the row has any labels
        if (label_str):
            val = _parse_labels(label_str)
            parsed_labels[key_value] = val
        # create the record for this row
        record = {}
        record[key] = key_value
        # get values of parsed labels 
        values = parsed_labels.get(key_value)
        # update value of each parsed label
        for value in values:
                # add element to record dictionary
                record[value] = 1
        # get the column/values for this row
        row_dict = df_dict[count]
        # add current row fields to current record
        record.update(row_dict)
        # append record to list of dataframe records
        records.append(record)
    
    # read records as dataframe
    ret_df = pd.DataFrame.from_records(records)
    # fill N/A values with 0
    ret_df = ret_df.fillna(0)
    return ret_df

def summarize_processed_sized_snapshot(df, filter={}):
    """
    Summarize a processed and sized snapshot given a set of filters

    Parameters
    ----------
    df : DataFrame 
        Output of `process_sized_snapshot`
    filter : dict
        Column name and list of values
        Example: {column: [val1, val2]}
        Default = {}

    Raise
    -----
    ValueError
        DataFrame is empty
    KeyError
        DataFrame is missing the column

    Return
    ------
    df : DataFrame    
    """
    # return dataframe
    ret_df = df.copy(deep=True)

    # dataframe cannot be empty
    if (df.empty == True):
        raise ValueError('Empty input DataFrame')
    
    # dataframe must contain column if filter is specified
    if (bool(filter)):
        # can only have one key
        if (len(list(filter.keys())) > 1):
            raise ValueError('Only one column in filter allowed')
        # if has one key, must be valide
        column = list(filter.keys())[0]
        if (not column in list(df.columns)):
            msg = 'Column not found: {}'.format(column)
            raise KeyError(msg)
        # if the filter is valid
        # get values
        values = filter[column]
        print('Values: {}'.format(values))
        # apply filter
        ret_df = df.loc[df[column].isin(values)]

    # summarize the dataframe
    ret_df = pd.DataFrame(ret_df.sum(numeric_only=True)).transpose()
    return ret_df

def create_sprint_filter(column, column_values, substrs):
    """
    Create the list of column values to filter on. Useful for column 
    labels and values that contain unprintable utf-8 characters.

    Parameters
    ----------
    column : str
        Name of column
    column_values : list
        List of actual column values
    substrs : list
        List of substrings to find in list of column values

    Raise
    -----
    ValueError
        column, column_values, or substrings are empty

    Return
    ------
    dict
        Dictionary of form: {column : [val1, val2...val_n]}
    """
    if ((not(column)) or
        (len(column_values)<1) or
        (len(substrs) <1)):
        raise ValueError('Invalid parameter value')
    
    # eliminate duplicates in list
    column_vals = set(column_values)
    # create list of full-string filtered labels (substring matches)
    filtered = []
    # for each substring
    for substr in substrs:
        for val in column_vals:
            if substr in val:
                filtered.append(val)

    return {column : filtered}

# end document