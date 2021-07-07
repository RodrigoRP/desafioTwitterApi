import re


def clean_tbl_name(filename):
    # rename csv, force lower case, no spaces, no dashes
    clean_tbl_name = filename.lower().replace(" ", "").replace("-", "_").replace(r"/", "_").replace("\\", "_").replace(
        "$", "").replace("%", "")

    tbl_name = '{0}'.format(clean_tbl_name.split('.')[0])

    return tbl_name


def clean_text(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)  # Removed @mentions
    text = re.sub(r'#', '', text)  # Removing the '#' symbol
    text = re.sub(r'RT[\s]+', '', text)  # Removing RT

    return text


def replace_dtype(dataframe):
    replacements = {
        'timedelta64[ns]': 'varchar',
        'object': 'varchar',
        'float64': 'float',
        'int64': 'int',
        'datetime64[ns]': 'date'
    }

    col_str = ", ".join(
        "{} {}".format(n, d) for (n, d) in zip(dataframe.columns, dataframe.dtypes.replace(replacements)))

    return col_str
