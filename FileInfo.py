import pandas as pd
from tkinter.filedialog import *

'''
Ask the user if they want to print the output to a file as well.
If No, quit the application. 
If Yes, then ask for the location to place the file. Use a default file title.
'''


def retrieve_file_csv():
    file = askopenfilename()
    file_data = pd.read_csv(file)
    return file_data


def retrieve_metrics(file_data):
    print('\n')
    print('Info Function:\n', file_data.info(), '\n')
    print('Describe Function:\n', file_data.describe(), '\n')
    print('First 15 lines:\n', file_data.head(10), '\n')
    print('Last 15 lines:\n', file_data.tail(10), '\n')
    print("First Valid Index: ", file_data.first_valid_index(), '\n')
    print("Last Valid Index: ", file_data.last_valid_index(), '\n')
    print("Correlation:\n", file_data.corr(), '\n')
    print("Covariance:\n", file_data.cov(), '\n')
    print("Mode:\n", file_data.mode(axis='columns',
          numeric_only=True, dropna=True), '\n')

    print(DF := pd.DataFrame({'Variance': file_data.var(), 'Median': file_data.median(
    ), 'Std Err of Mean': file_data.sem(), 'Kurtosis': file_data.kurt(), 'Skew': file_data.skew(), 'MAD': file_data.mad(), "Memory Usage": file_data.memory_usage(index=False)}))
    print()

    print('Number of Unique values for each column')
    print(file_data.nunique())


def main():
    file_data = retrieve_file_csv()
    retrieve_metrics(file_data)


if __name__ == '__main__':
    main()
    quit()
