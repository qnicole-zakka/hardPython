"""Practice interface for the hardPython project."""

from abc import ABC, abstractmethod, ABCMeta, classmethod


class GeneralParserInterface(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, '__init__') and
                callable(subclass.__init__) and
                hasattr(subclass, 'load_data') and
                callable(subclass.load_data) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text) or
                NotImplemented)

    @abstractmethod
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def load_data(self, file_path) -> str:
        """load data from the file_path, return the content as a string"""
        return ""

    @abstractmethod
    def extract_text(self, raw_data) -> str:
        """extract text from the raw_data, return the text as a string"""
        return ""


class PdfParser(GeneralParserInterface):
    def __init__(self, file_path):
        super().__init__(file_path)

    def load_data(self, file_path) -> str:
        """load data from the file_path, return the content as a string"""
        return ""

    def extract_text(self, raw_data) -> str:
        """extract text from the raw_data, return the text as a string"""
        return ""
        

@GeneralParserInterface.register
class EmailParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self, file_path) -> str:
        """load data from the file_path, return the content as a string"""
        return ""

    def extract_text(self, raw_data) -> str:
        """extract text from the raw_data, return the text as a string"""
        return ""
    