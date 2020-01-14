from datetime import datetime, timedelta
import os
from prettytable import PrettyTable


def date_arithmetic():
    """Function date_arithmetic uses datetime and timedelta modules to find the date the days after a given date and
    the days between two dates """
    three_days_after_02272000 = datetime(2000, 2, 27) + timedelta(days=3)
    three_days_after_02272017 = datetime(2017, 2, 27) + timedelta(days=3)
    days_passed_01012017_10312017 = (datetime(2017, 10, 31) - datetime(2017, 1, 1)).days
    return three_days_after_02272000, three_days_after_02272017, days_passed_01012017_10312017


def file_reading_gen(path, fields, sep=',', header=False):
    """Function file_reading_gen reads a file path, fields, separator and header and returns the values of the fields
    in the file if the fields given is equal to fields number in file """
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"Can't open {path}")
    else:
        with fp:
            for counter, line in enumerate(fp):
                line = line.rstrip('\n')
                tokens = line.split(sep)
                if fields != len(tokens):
                    raise ValueError(f"{os.path.basename(path)} has {len(tokens)} fields on line {counter + 1}"
                                     f" but expected {fields} ")
                elif header and counter == 0:
                    continue
                else:
                    yield tuple(tokens)


class FileAnalyzer:

    def __init__(self, directory):
        """ Function __init__ initializes the directory, files_summary and function analyze_files."""
        self.directory = directory  # NOT mandatory!
        self.files_summary = dict()

        self.analyze_files()  # summerize the python files data

    def analyze_files(self):
        """Function analyze_files reads a directory and returns the total number of characters, functions, classes,
        and lines for each python file in that directory """
        try:
            files = os.listdir(self.directory)
        except FileNotFoundError:
            raise FileNotFoundError(f"Can't open {self.directory}")
        else:
            for doc in files:
                if doc.endswith('.py'):
                    num_lines = 0
                    num_char = 0
                    num_function = 0
                    num_class = 0
                    try:
                        fp = open(os.path.join(self.directory, doc))
                    except FileNotFoundError:
                        raise FileNotFoundError(f"Can't open {doc}")
                    else:
                        for line in fp:
                            num_lines += 1
                            num_char += len(line)
                            line = line.strip()
                            if line.startswith('def '):
                                num_function += 1
                            if line.startswith('class '):
                                num_class += 1
                        self.files_summary[doc] = {'line': num_lines, 'char': num_char, 'function': num_function,
                                                   'class': num_class}

    def pretty_print(self):
        """ Function pretty_print gets the dictionary that saves all the information and prints it as a pretty table"""
        pt = PrettyTable(field_names=['File Name', 'Classes', 'Functions', 'Lines', 'Character'])
        for key, values in self.files_summary.items():
            pt.add_row([key, values['class'], values['function'], values['line'], values['char']])
        return pt



