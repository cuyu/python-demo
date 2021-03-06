import csv
import os
import tempfile
import random


def operate_csv(row_operate_method):
    """
    A decorator of the row operate method.
    The input method should only operate on self._operate_row (e.g. delete a specific column).
    """

    def wrap(*args):
        self = args[0]
        # The file generated by mkstemp() will not be removed automatically.
        fd, tmp_path = tempfile.mkstemp()
        with open(tmp_path, "wb") as tmp:
            with open(self.file_path, "rb") as source:
                rdr = csv.reader(source)
                wtr = csv.writer(tmp)
                for r in rdr:
                    if r:
                        self._operate_row = r
                        row_operate_method(*args)
                    wtr.writerow(r)
        # Copy the content back.
        with open(tmp_path, "rb") as tmp:
            with open(self.file_path, "wb") as target:
                rdr = csv.reader(tmp)
                wtr = csv.writer(target)
                for r in rdr:
                    wtr.writerow(r)
        os.remove(tmp_path)

    return wrap


class CSVModifier(object):
    def __init__(self, csv_file_path):
        self.file_path = csv_file_path
        self._operate_row = []

    @operate_csv
    def delete_csv_column(self, column_num):
        """
        Delete specific column.
        :param column_num: the column number you want to delete, the first column is 0.
        :return: None
        """
        del self._operate_row[column_num]

    @operate_csv
    def replace_csv_column_by_column(self, source_column_num, target_column_num):
        """
        Replace the column content by another column content.
        :param source_column_num: The column to be replaced.
        :param target_column_num: The column that is used as replace content.
        :return: None
        """
        self._operate_row[source_column_num] = self._operate_row[target_column_num]

    @operate_csv
    def replace_csv_column_by_content(self, source_column_num, content):
        self._operate_row[source_column_num] = content

    @operate_csv
    def replace_csv_column_by_random_content(self, source_column_num, content_list):
        content = random.choice(content_list)
        self._operate_row[source_column_num] = content

    @operate_csv
    def replace_csv_column_by_add_quota(self, source_column_num):
        self._operate_row[source_column_num] = "'" + self._operate_row[source_column_num] + "'"


if __name__ == "__main__":
    modifier = CSVModifier('/Users/CYu/Code/Python/eventgen-retails/replace_files/product_info.csv')
    modifier.replace_csv_column_by_random_content(20,
                                                  ['Ace', 'Bull', 'Coda', 'Hammer', 'EarlyBird', 'Fallout', 'Gatlin',
                                                   'Mircohard', 'Dami', 'Oldbalance'])
    # for (dirpath, dirnames, filenames) in os.walk('/Users/CYu/qa/new_test/resources/apps/oidemo/samples/'):
    #     for filename in filenames:
    #         if filename.endswith('.vmstat'):
    #             file_path = os.path.join(dirpath, filename)
    #             modifier = CSVModifier(file_path)
    #             modifier.replace_csv_column_by_column(0, 3)
