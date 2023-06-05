"""
Module: rename_files.py
Description: This module is used to rename the files in the directory.

Functions: rename_file(directory_path, source_extension, destination_extension)

Author: Sinku Kumar
Date: 4th June 2023
Version: 0.1
"""

import os

#directory = 'C:\\Users\\Sinkukumar\\PycharmProjects\\IntegrationServicesAutomation\\Files'


def rename_file(directory_path, source_extension, destination_extension):
    """
    This function is used to rename the files in the directory.

    Usage:
    rename_file(directory_path, source_extension, destination_extension)

    :param str directory_path:
    :param str source_extension:
    :param str destination_extension:
    :return:
    """
    for file in os.listdir(directory_path):
        if file.endswith(source_extension):
            try:
                os.rename(f'{directory_path}\\{file}', f'{directory_path}\\{file[:-4]}{destination_extension}')
                print(f"Renamed file: {file}")
            except FileExistsError:
                print(f"File already exists: {file}, don't rename it again and again!")
    return 1
