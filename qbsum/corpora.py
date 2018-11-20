import os
import pandas as pd
import spacy
from pathlib import Path
from abc import ABC, abstractmethod


class Corpus(ABC):
    """An abstract data loader to define corpus interfaces."""

    @abstractmethod
    def __init__(self, documents_dir, queries_dir, references_dir):
        """
        Constructor.
        :param documents_dir:
        :type documents_dir: Path
        :param queries_dir:
        :type queries_dir: Path
        :param references_dir:
        :type references_dir: Path
        """
        pass

    @abstractmethod
    def document_sets(self):
        """
        Document sets getter.
        :return: list of documents sets (topics); a document is a list of string
        :rtype: list(list(list(str)))
        """
        pass

    @abstractmethod
    def queries(self):
        """
        Queries getter.
        :return: list of queries
        :rtype: list(str)
        """
        pass
    
    @abstractmethod
    def references(self):
        """
        Reference summaries getter.
        :return: list reference summaries by topics; a topic can have multiple summaries;  a summary is a list of string
        :rtype: list(list(list(str)))
        """
        pass
    
    @abstractmethod
    def document_set_names(self):
        """
        Documents sets (topics) names getter.
        :return: list of documents sets (topics) names; indices match document_sets
        :rtype: list(str)
        """
        pass


class DevCorpus(Corpus):
    """A data loader for the development corpus."""

    def __init__(self, documents_dir, queries_dir, references_dir):
        
        nlp = spacy.load('en_core_web_sm')
        
        self.__document_sets = []
        self.__queries = []
        self.__references = []
        self.__document_set_names = []

        for flat_file in sorted(os.listdir(str(documents_dir))):

            # Define the documents set:
            document_set_name = flat_file.replace(".csv", "")
            self.__document_set_names.append(document_set_name)

            # Load documents:
            df = pd.read_csv(documents_dir/flat_file, encoding='utf-8-sig')
            document_set = []
            for i, row in df.iterrows():
                document = [row['TITLE']]
                body = nlp(row['TEXT'])
                for sentence in body.sents:
                    document.append(sentence.text)
                document_set.append(document)
            self.__document_sets.append(document_set)


            # Load queries:
            file_name = document_set_name + ".txt"
            if Path(queries_dir/file_name).is_file:
                # Query is the first line of text from the query file:
                with open(str(queries_dir/file_name), encoding='utf-8-sig') as f:
                    self.__queries.append(f.readline())
            
            # Load topic's reference summary:
            doc_set_references = []
            if Path(references_dir/file_name).is_file:
                with open(str(references_dir/file_name), encoding='utf-8-sig') as f:
                    # Currently, references consists of the first line of text from the reference file:
                    # TODO: add support for multi-sentence references:
                    doc_set_references.append([f.readline()])
                
                self.__references.append(doc_set_references)

    
    def document_sets(self):
        return self.__document_sets.copy()

    def queries(self):
        return self.__queries.copy()
    
    def references(self):
        return self.__references.copy()
    
    def document_set_names(self):
        return self.__document_set_names.copy()



class NewsCorpus(Corpus):
    """A data loader for the development corpus."""

    def __init__(self, documents_dir, queries_dir, references_dir):
        
        nlp = spacy.load('en_core_web_sm')
        
        self.__document_sets = []
        self.__queries = []
        self.__references = []
        self.__document_set_names = []

        for topic in sorted(os.listdir(str(documents_dir))):

            # Define the documents set:
            self.__document_set_names.append(topic)
            
            # Load queries:
            query_file = topic + ".txt"
            if Path(queries_dir/query_file).is_file:
                with open(str(queries_dir/query_file), encoding='utf-8-sig') as f:
                    self.__queries.append(f.readline())
            
            # Load topic's reference summary:
            doc_set_references = []
            for summary_file in os.listdir(str(references_dir/topic)):
                summary = []
                with open(str(references_dir/topic/summary_file), encoding='utf-8-sig') as f:
                    raw_text = nlp(f.read())
                    for sentence in raw_text.sents:
                        summary.append(sentence.text)
                    doc_set_references.append(summary)
                self.__references.append(doc_set_references)

            # Load documents:
            document_set = []
            for doc_file in os.listdir(str(documents_dir/topic)):
                document = []
                with open(str(documents_dir/topic/doc_file), encoding='utf-8-sig') as f:
                    raw_text = nlp(f.read())
                    for sentence in raw_text.sents:
                        document.append(sentence.text)
                document_set.append(document)
                
            self.__document_sets.append(document_set)


    
    def document_sets(self):
        return self.__document_sets.copy()

    def queries(self):
        return self.__queries.copy()
    
    def references(self):
        return self.__references.copy()
    
    def document_set_names(self):
        return self.__document_set_names.copy()

