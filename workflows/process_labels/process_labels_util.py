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
        
    # TODO perform additional validation of file, if needed

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

def process_sized_snapshot(df, labels='Labels', key='CardURL', required_fields=['Repo']):
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

    required_fields : list
        List of fields required in the DataFrame. Default 'Repo'

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
    
    # dataframe must contain required fields
    for field in required_fields:
        if (field not in df):
            msg = 'Missing required field: {}'.format(field)
            raise KeyError(msg)
    
    # key field must be unique in dataframe
    if (len(df[key].unique()) != len(df)):
        raise KeyError('Key is not unique')
    
    # copy the input dataframe
    ret_df = df.copy(deep=True)

    # create a dict for parsed labels
    # label: Label(name="D: Dataset: large number of files")
    # keyed on parameter: key
    # ex: {'https://github.com/repo/issues/101':[label_1, label_2, label_3]}
    parsed_labels = {}

    # create a dict for required fields
    # keyed on parameter: key
    # ex: {'https://github.com/repo/issues/101':{'field_1':val1, 'field_2':val2, 'field3':val3}
    req_fields = {}

    # process each row
    for row in df.iterrows():
        # get key value 
        key_value = row[1].get(key)
        # get label str 
        label_str = row[1].get(labels)
        # if the row has any labels
        if (label_str):
            val = _parse_labels(label_str)
            parsed_labels[key_value] = val
        # get the required fields and their values
        req_fields[key_value] = {}
        for field in required_fields:
            req_fields[key_value][field] =  row[1].get(field)
    
    # list of records, one dataframe row per record
    records = []
    # transform parsed labels and req_fields into records
    for entry in parsed_labels.keys():
        record = {}
        record[key] = entry
        values = parsed_labels.get(entry)
        for value in values:
            record[value] = 1
        # get additional required fields
        req_values = req_fields[entry]
        # add fields to current record
        record.update(req_values)
        # append record to list of dataframe records
        records.append(record)
    
    # read records as dataframe
    ret_df = pd.DataFrame.from_records(records)
    # fill N/A values with 0
    ret_df = ret_df.fillna(0)
    return ret_df

# end document
