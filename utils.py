import csv
import locale

def write_to_csv(items, filename):
    keys = items[0].keys()
    with open(filename, 'w', encoding=locale.getpreferredencoding()) as output_file:
        dict_writer = csv.DictWriter(output_file, keys, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
        dict_writer.writeheader()
        dict_writer.writerows(items)