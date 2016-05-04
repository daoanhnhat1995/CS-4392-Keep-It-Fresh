import yaml
import pandas as pd
import ujson

class Document(object):
    """
    Contain all datasets parsed to migrate with database models
    """

    def __init__(self,documents):
        self.documents = documents
        self.tables = {}
        self.format_document()

    """ Return whether a document is csv(1) or json(0)
    input: "yelp_academic_dataset_business.csv"

    """
    def get_type(self,document):
        file_type = document.split(".")[1]
        if(str(file_type) == "csv"):
            return 1
        else:
            return 0

    """
    Load all csv and json files into arrays
    So that they can be loaded into PostgreSQL easily

    """

    def format_document(self):
        for key,value in self.documents.iteritems():
            if(self.get_type(value)):
                record = self.load_csv(value)
            else:
                record = self.load_json(value)

            self.tables[key] = record

    """ Return {Array} document
    Load csv file
    """
    def load_csv(self,document):
        return pd.read_csv(document,skiprows=1,header=None)

    """ Return {Array} document
    Load JSON file
    """
    def load_json(self,document):
        f = []
        file = open(document,'r')
        for line in file.readlines():
            line = line.split("\n")[0]
            line = ujson.loads(line)
            f.append(line)
        return f

    """ Return {Array} all tables
    Get all parsed documents ready for migrations
    """
    def get_documents(self):
        return self.tables












