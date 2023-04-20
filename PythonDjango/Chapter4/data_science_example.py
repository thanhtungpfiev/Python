# Created by Admin at 5/14/2022
def fetch_data(data_source):
    pass


def parse_data(data):
    pass


def filter_data(parsed_data):
    pass


def polish_data(filtered_data):
    pass


def analyse(polished_data):
    pass


class Report:
    pass


def do_report(data_source):
    # fetch and prepare data
    data = fetch_data(data_source)
    parsed_data = parse_data(data)
    filtered_data = filter_data(parsed_data)
    polished_data = polish_data(filtered_data)
    # run algorithms on data
    final_data = analyse(polished_data)
    # create and return report
    report = Report(final_data)
    return report
