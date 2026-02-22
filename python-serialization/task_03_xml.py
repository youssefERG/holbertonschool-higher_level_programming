#!/usr/bin/python3
"""Module for serializing and deserializing Python dictionaries using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file."""
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file into a Python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        text = child.text
        if text.isdigit():
            result[child.tag] = int(text)
        elif text.replace('.', '', 1).isdigit() and text.count('.') == 1:
            result[child.tag] = float(text)
        elif text.lower() == 'true':
            result[child.tag] = True
        elif text.lower() == 'false':
            result[child.tag] = False
        else:
            result[child.tag] = text
    return result