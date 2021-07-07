from datetime import date
from numpy import iterable
import pandas as pd
import requests
import xml.etree.ElementTree as ET
import time

# from requests.api import get
# import sys
# sys.path.append("../")
# from ..common.constants import *
# from biomedical_text_mining.common.constants import *
# from ..common.constants import REVEIVED_DAY_XPATH


###################################################
# pubmed_query.py                 PubMed API的使用 #
# 
# 
# Author: zhangjq@tib.cas.cn
# Date: 2021/06/01
#
#
# 一个 API是 esearch 
# 一个 API是 efetch
# 
###################################################

__all__ = [
    "query",
    "fetch_articles",
]

###################################################
# Utils
###################################################
def _batches(iterable: list, size: int=1) -> list:
    """ 打包函数，解决一次装载不了的问题
    
    """
    length = len(iterable) # 总大小

    for index in range(0, length, size): # 每次迭代多少批
        yield iterable[index : min(index+size, length)] # 返回固定大小的batch

    

###################################################
# get pmids using query
###################################################

def query(query, output="json"):
    """ query pubmed
    通过query来得到 pmids（PubMed API的使用，query的使用）

    (It also shows the usage of NCBI PubMed API)

    Args:
        query (str): PubMed query language
            e.g. '("Nature biotechnology"[Journal]) AND (("2020/01/01"[Date - Publication] : "2020/12/31"[Date - Publication]))'

    Returns:
        pmids: a list of pmids
            e.g. ['33483714', '33361824', ... , '33318653']

    Examples:
        >>> query = '("Nature biotechnology"[Journal]) AND (("2020/01/01"[Date - Publication] : "2020/12/31"[Date - Publication]))'
        >>> id_list = query(query) # 424 
        >>> id_list
        ['33483714', '33361824', ... , '33318653'] # 424 # it suggests that NBT 2020 424 publications

    """
    parameters = {
        "tool": "my_tool",
        "email": "m13051995656@163.com", 
        "db": "pubmed",
        "retmode": "json",
        "retmax": 50000,
        "term": query
    }

    BASE_URL = "https://eutils.ncbi.nlm.nih.gov"
    FUNCTION_URL = "/entrez/eutils/esearch.fcgi"

    response = requests.get(BASE_URL + FUNCTION_URL, params=parameters)
    response.raise_for_status() # Check for any errors

    if output == "json":
        return response.json()["esearchresult"]["idlist"] # type(response.json()) 是个 dict
        # 为什么尾巴是 ["esearchresult"]["idlist"] 这两个，是查看JSON得知的
    else:
        return response.text  # type(response.text) 是个 str

###################################################
# fetch article content using pmids
###################################################

def _get_content(article, xpath, default=None, separator="\n"):
    """ 
    """
    info = article.findall(xpath)
    
    if info is None or len(info) == 0:
        return default
    else:
        return separator.join([sub.text for sub in info if sub.text is not None])

def _fetch_article(batch_ids):
    """retrieves the 

    Args:
        batch_ids (list of pmids): article IDs
    """
    # parameters = self.parameters.copy() # 深拷贝的好处？
    parameters = {
            "tool": "my_tool",
            "email": "m13051995656@163.com",
            "db": "pubmed",
            "retmode": "XML",
            "retmax": 500,
    }
    parameters["id"] = batch_ids

    # response = requests.get(
    #     url="", params=parameters, output="xml"
    # )

    BASE_URL = "https://eutils.ncbi.nlm.nih.gov"
    FUNCTION_URL = "/entrez/eutils/efetch.fcgi"
    response = requests.get(BASE_URL+FUNCTION_URL, params=parameters)
    response.raise_for_status() # Check for any errors


    root = ET.fromstring(response.text)

    # title
    # TITTLE_XPATH = './PubmedArticle/MedlineCitation/Article/ArticleTitle'
    TITTLE_XPATH = ".//ArticleTitle"
    # abstract
    # ABSTRACT_XPATH = './PubmedArticle/MedlineCitation/Article/Abstract/AbstractText'
    ABSTRACT_XPATH = ".//AbstractText"
    # doi
    # DOI_XPATH = './PubmedArticle/MedlineCitation/Article/ELocationID'
    DOI_XPATH = ".//Article/ELocationID"
    # pmid
    # PMID_XPATH = './PubmedArticle/MedlineCitation/'  # 不work
    PMID_XPATH = ".//ArticleId[@IdType='pubmed']"
    # date
    # REVEIVED_DAY_XPATH = './PubmedArticle/PubmedData/History/PubMedPubDate[1]/Day'
    REVEIVED_DAY_XPATH = ".//PubmedData/History/PubMedPubDate[1]/Day"
    # REVEIVED_MONTH_XPATH = './PubmedArticle/PubmedData/History/PubMedPubDate[1]/Month'
    REVEIVED_MONTH_XPATH = ".//PubmedData/History/PubMedPubDate[1]/Month"
    # REVEIVED_YEAR_XPATH = './PubmedArticle/PubmedData/History/PubMedPubDate[1]/Year'
    REVEIVED_YEAR_XPATH = ".//PubmedData/History/PubMedPubDate[1]/Year"
    # ACCEPTED_DAY_XPATH = './PubmedArticle/PubmedData/History/PubMedPubDate[2]/Day'
    ACCEPTED_DAY_XPATH = ".//PubmedData/History/PubMedPubDate[2]/Day"
    # ACCEPTED_MONTH_XPATH = './PubmedArticle/PubmedData/History/PubMedPubDate[2]/Month'
    ACCEPTED_MONTH_XPATH = ".//PubmedData/History/PubMedPubDate[2]/Month"
    # ACCEPTED_YEAR_XPATH = './PubmedArticle/PubmedData/History/PubMedPubDate[2]/Year'
    ACCEPTED_YEAR_XPATH = ".//PubmedData/History/PubMedPubDate[2]/Year"
    # PUBLICATION_DAY_XPATH = './PubmedArticle/PubmedData/History/PubMedPubDate[4]/Day'
    PUBLICATION_DAY_XPATH = ".//PubmedData/History/PubMedPubDate[4]/Day"
    # PUBLICATION_MONTH_XPATH = './PubmedArticle/PubmedData/History/PubMedPubDate[4]/Month'
    PUBLICATION_MONTH_XPATH = ".//PubmedData/History/PubMedPubDate[4]/Month"
    # PUBLICATION_YEAR_XPATH = './PubmedArticle/PubmedData/History/PubMedPubDate[4]/Year'
    PUBLICATION_YEAR_XPATH = ".//PubmedData/History/PubMedPubDate[4]/Year"
    # journal 
    # JOURNAL_XPATH = './PubmedArticle/MedlineCitation/Article/Journal/Title'
    JOURNAL_XPATH = ".//Journal/Title"
    JOURNAL_ABBREVIATION_XPATH = './PubmedArticle/MedlineCitation/Article/Journal/ISOAbbreviation'
    JOURNAL_ABBREVIATION_XPATH = ".//Article/Journal/ISOAbbreviation"

    # publication_type
    PUBLICATION_TYPE_XPATH = './PubmedArticle/MedlineCitation/Article/PublicationTypeList/PublicationType'
    PUBLICATION_TYPE_XPATH = ".//PublicationType"

    # author
    LASTNAME_XPATH = './PubmedArticle/MedlineCitation/Article/AuthorList/Author/LastName'
    LASTNAME_XPATH = ".//AuthorList/Author/LastName"
    INITIALS_XPATH = './PubmedArticle/MedlineCitation/Article/AuthorList/Author/Initials'
    INITIALS_XPATH = ".//AuthorList/Author/Initials"
    FORENAME_XPATH = './PubmedArticle/MedlineCitation/Article/AuthorList/Author/ForeName'
    FORENAME_XPATH = ".//AuthorList/Author/ForeName"
    # affiliation
    AFFILIATION_XPATH = './/Author/AffiliationInfo'

    # country
    COUNTRY_XPATH = './PubmedArticle/MedlineCitation/MedlineJournalInfo/Country'
    COUNTRY_XPATH = ".//MedlineJournalInfo/Country"

    df = pd.DataFrame(columns=["Tittle", "abstract", "publication_type",
                               "publication_year", "publication_month", "publication_day",
                               "accepted_year", "accepted_month", "accepted_day",
                               "received_year", "received_month", "received_day",
                              "journal", "journal_abbreviation", "lastname", "forename", "initials",
                               "affiliation", "country", "doi", "pmid",
                              ])

    for index, article in enumerate(root.iter("PubmedArticle")):
        df.loc[index] = {
            "Tittle": _get_content(article=article, xpath=TITTLE_XPATH),
            "abstract": _get_content(article=article, xpath=ABSTRACT_XPATH),
            "publication_type": _get_content(article=article, xpath=PUBLICATION_TYPE_XPATH),
            "publication_year": _get_content(article=article, xpath=PUBLICATION_YEAR_XPATH),
            "publication_month": _get_content(article=article, xpath=PUBLICATION_MONTH_XPATH),
            "publication_day": _get_content(article=article, xpath=PUBLICATION_DAY_XPATH),
            "accepted_year": _get_content(article=article, xpath=ACCEPTED_YEAR_XPATH),
            "accepted_month": _get_content(article=article, xpath=ACCEPTED_MONTH_XPATH),
            "accepted_day": _get_content(article=article, xpath=ACCEPTED_DAY_XPATH),
            "received_year": _get_content(article=article, xpath=REVEIVED_YEAR_XPATH),
            "received_month": _get_content(article=article, xpath=REVEIVED_MONTH_XPATH),
            "received_day": _get_content(article=article, xpath=REVEIVED_DAY_XPATH),
            "journal": _get_content(article=article, xpath=JOURNAL_XPATH),
            "journal_abbreviation": _get_content(article=article, xpath=JOURNAL_ABBREVIATION_XPATH),
            "lastname": _get_content(article=article, xpath=LASTNAME_XPATH),
            "forename": _get_content(article=article, xpath=FORENAME_XPATH),
            "initials": _get_content(article=article, xpath=INITIALS_XPATH),
            "affiliation": _get_content(article=article, xpath=AFFILIATION_XPATH),
            "country": _get_content(article=article, xpath=COUNTRY_XPATH),
            "doi": _get_content(article=article, xpath=DOI_XPATH),
            "pmid": _get_content(article=article, xpath=PMID_XPATH),
        }
    return df


def fetch_articles(article_ids, xml_saved=False, xml_path="../_data_/", csv_saved=False, csv_path="../data/"):
    """fetch scientific paper basic information with pmids. basic information inclus:
    1. Title
    2. Abstract
    3. 

    Args:
        article_ids (list): ['33483714', '33361824', ... , '33318653']
        xml_saved (bool, optional): whether save raw xml file. Defaults to False.
        xml_path (str, optional): [description]. Defaults to "../_data_/".
        csv_saved (bool, optional): [description]. Defaults to True.
        csv_path (str, optional): whether save parsed csv file. Defaults to "../data/".

    Returns:
        df

    Examples:
        >>> 

    
    """
    articles = pd.DataFrame()
    for batch in _batches(article_ids, 250):
        articles = articles.append(_fetch_article(batch)) # 每次增加一部分article信息
    
    if csv_saved:
        SAVE_PATH = "./" + time.strftime("papers_%Y_%m_%d_%H:%M:%S".format(time.localtime()))  + ".csv"
        articles.to_csv(SAVE_PATH, index=0)
    return articles

###################################################
# Test
###################################################
def test_01():
    query = '("Nature biotechnology"[Journal]) AND (("2020/01/01"[Date - Publication] : "2020/12/31"[Date - Publication]))'
    id_list = query(query)

    df = fetch_articles(id_list[:5])
    print(df)

def test_02():
    query_language = '("Nucleic acids research"[Journal]) AND (("2021/07/02"[Date - Publication] : "2021/07/03"[Date - Publication]))'
    id_lists = query(query_language) # 95
    print("Successfully query...")
    df = fetch_articles(id_lists)
    print(df)
    print("Successfully...")

if __name__ == "__main__":
    test_02()
    # from ..common.constants import * 
    # print(REVEIVED_DAY_XPATH)
