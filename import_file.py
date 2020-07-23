# -*- coding: utf-8 -*-
"""Import file module"""


def import_page_object():
    """Import page object file

        Returns:
            page_object_content(list): a list containing
            each input data of 'page_object.txt'
    """
    page_object_content = []
    with open("./page_object.txt", "r+") as page_object_file:
        for input_page_object in page_object_file:
            input_page_object = input_page_object.strip()
            page_object_content.append(input_page_object)
    return page_object_content


def import_configuration():
    """Import configuration file

        Returns:
            config_content(list): a list containing
            each input data of 'configuration.txt'
    """
    config_content = []
    with open("./configuration.txt", "r+") as config_file:
        for input_config in config_file:
            input_config = input_config.strip()
            config_content.append(input_config)
    return config_content
