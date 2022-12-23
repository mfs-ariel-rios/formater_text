import csv
import json


def read_csv_file(path, filename, column: int = 1):
    items = []
    filePathNameWExt = './' + path + '/' + filename
    with open(filePathNameWExt, 'r', encoding='utf-8') as f:
        file_reader = csv.reader(f, delimiter=',')
        items = get_items_column(file_reader, column)
    return items


def conver_object(countries: list):
    return [{'id': countries.index(country) + 1, 'value': country.lower(),
             'label': country} for country in countries]


def write_to_JSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w', encoding='utf-8') as fp:
        json.dump(data, fp, indent=4, ensure_ascii=False)


def get_items_column(csv, column: int):
    items: list = []
    for index, row in enumerate(csv):
        if (row[column] == '' or index == 0):
            continue
        items.append(row[column])
    return items


def main() -> None:
    countries_raw = read_csv_file('./', 'formulario-csv.csv')
    countries_map: list = conver_object(countries_raw)
    write_to_JSONFile('./', 'countries_map_form', countries_map)
    print('Archivo generado')


main()
