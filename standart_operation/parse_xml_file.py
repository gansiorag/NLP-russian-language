"""
This module

data start
data end

Author Gansior Alexandr mail - gansior@gansior.ru tel - +79173383804
"""
import xml.etree.ElementTree as ET


if __name__ == '__main__':
    root_node = ET.parse('/home/al/Projects_My/NLP-russian-language/datasets/annot.opcorpora.xml').getroot()
    print(root_node)