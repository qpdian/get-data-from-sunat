def formatText(text = ''):
    return text.replace('\n', ' ').replace('\t', ' ').replace('\r', ' ').replace('\xa0', '')

def to_csv_file(data, path_file):
    with open(path_file, "a") as my_file:
        my_file.write(','.join(data) + '\n')

