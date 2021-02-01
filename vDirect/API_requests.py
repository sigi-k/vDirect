import logging
import pandas as pd
import requests
import json

# base_url = 'http://127.0.0.1:8000/'
# ToDo: change base URL to new server URL muss ein Paremeter von Vdirect sein
# entweder über command line parameter. oder über environment variable

# set log level for requests module

urllib3_logger = logging.getLogger('urllib3')
urllib3_logger.setLevel(logging.CRITICAL)


def vfetch(return_object="vog", return_type="msa", **params):
    base_url = params.get('base_url')
    """Yield the response of a query."""
    if return_object not in ["vog", "protein"]:
        # return_object does not compare equal to any enum value:
        raise ValueError("Invalid return object " + str(return_object))

    url = base_url + 'vfetch/{0}'.format(return_object) + '/{0}?'.format(return_type)
    if return_object == "vog":
        if return_type not in ["msa", "hmm"]:
            # return_type does not compare equal to any enum value:
            raise ValueError("Invalid return object " + str(return_object))

    elif return_object == "protein":
        if return_type not in ["faa", "fna"]:
            # return_type does not compare equal to any enum value:
            raise ValueError("Invalid return object " + str(return_object))

    # API GET request
    r = requests.get(url=url, params=params)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise Exception(e.response.text)
    response = r.json()
    return response


def vsummary(return_object="vog", format="json", **params):
    """Yield the response (vog/species/protein summary of a query."""
    base_url = params.get('base_url')
    # First make some basic checks.
    if return_object not in ["vog", "species", "protein"]:
        # return_object does not compare equal to any enum value:
        raise ValueError("Invalid return object " + str(return_object))

    # _valid_formats = ["json", "df"]

    url = base_url + 'vsummary/{0}?'.format(return_object)

    # API GET request
    r = requests.get(url=url, params=params)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if e.response.text:
            raise Exception(e.response.text)
        else:
            # ToDo: better exception needed??
            raise Exception("Undefined error.")
    response = r.json()

    # # formatting
    # if format == "df":
    #     response = pd.DataFrame.from_dict(response)
    # elif format == "csv":
    #     df = pd.DataFrame.from_dict(response)
    #     response = df.to_csv()
    return response


# def vsearch_species(base_url, ids, name, format, phage, source, version, sort):
# def vsearch_species(base_url, **params):
#     url = base_url + 'vsearch/species/'
#     # params = {
#     #     "ids": ids,
#     #     "name": name,
#     #     "format": format,
#     #     "phage": phage,
#     #     "source": source,
#     #     "version": version,
#     #     "sort": sort
#     # }
#     print(params)
#     # API GET request
#     r = requests.get(url=url, params=params)
#     return r


def vsearch(return_object="vog", format="json", **params):
    """Yield the response (vog/species/protein summary of a query."""
    base_url = params.get('base_url')

    # First make some basic checks.
    if return_object not in ["vog", "species", "protein"]:
        # return_object does not compare equal to any enum value:
        raise ValueError("Invalid return object " + str(return_object))

    # _valid_formats = ["json", "df", "stdout"]

    url = base_url + 'vsearch/{0}?'.format(return_object)

    # API GET request
    # ToDo: 200 oder nicht 200
    r = requests.get(url=url, params=params)
    return r

    # response = r.json()
    #
    # # check if no matches were found
    # if not len(response):
    #     raise Exception("No matches for the search criteria.")
    #
    # # formatting
    # if format == "df":
    #     response = pd.DataFrame.from_dict(response)
    # elif format == "csv":
    #     df = pd.DataFrame.from_dict(response)
    #     response = df.to_csv()
    # elif format == "stdout":
    #     response = pd.DataFrame.from_dict(response)
    #
    #     if return_object == "vog":
    #         response = response["id"].tolist()
    #
    #     if return_object == "protein":
    #         response = response["id"].tolist()
    #
    #     if return_object == "species":
    #         response = response["taxon_id"].tolist()
    #
    #     try:
    #         response = ' '.join(response)
    #     except TypeError:
    #         response = ' '.join(str(i) for i in response)
    # return response


def vsearch_species(base_url, **params):
    url = base_url + 'vsearch/species/'
    r = requests.get(url=url, params=params)
    return r


def vsearch_protein(base_url, **params):
    url = base_url + 'vsearch/protein/'
    r = requests.get(url=url, params=params)
    return r


def vsearch_vog(base_url, **params):
    url = base_url + 'vsearch/vog/'
    r = requests.get(url=url, params=params)
    return r


# function to save hmm vFetch response objects (for now just hmm, msa)
def save_object(object, output_path="./test.txt"):
    """Saves the response object to output path"""

    with open(output_path, 'a') as file:
        for document in object:
            file.write(document)
