import logging
import requests

"""
Here URLs are built and Requests are made.
"""

# set log level for requests module
urllib3_logger = logging.getLogger('urllib3')
urllib3_logger.setLevel(logging.CRITICAL)


def vfetch_vog_msa(base_url, **params):
    url = base_url + 'vfetch/vog/msa/'
    r = requests.get(url=url, params=params)
    return r


def vfetch_vog_hmm(base_url, **params):
    url = base_url + 'vfetch/vog/hmm/'
    r = requests.get(url=url, params=params)
    return r


def vfetch_protein_faa(base_url, **params):
    url = base_url + 'vfetch/protein/faa/'
    r = requests.get(url=url, params=params)
    return r


def vfetch_protein_fna(base_url, **params):
    url = base_url + 'vfetch/protein/fna/'
    r = requests.get(url=url, params=params)
    return r


def vsummary_species(base_url, **params):
    """Yield the response to a species summary of a query."""
    url = base_url + 'vsummary/species/'
    # API GET request
    r = requests.get(url=url, params=params)
    return r


def vsummary_protein(base_url, **params):
    """Yield the response to a protein summary of a query."""
    url = base_url + 'vsummary/protein/'
    # API GET request
    r = requests.get(url=url, params=params)
    return r


def vsummary_vog(base_url, **params):
    """Yield the response to a vog summary of a query."""
    url = base_url + 'vsummary/vog/'
    # API GET request
    r = requests.get(url=url, params=params)
    return r


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


# function to save hmm vFetch response objects (for now just hmm, msa)


#
# def vfetch(return_object="vog", return_type="msa", **params):
#     base_url = params.get('base_url')
#     """Yield the response of a query."""
#     if return_object not in ["vog", "protein"]:
#         # return_object does not compare equal to any enum value:
#         raise ValueError("Invalid return object " + str(return_object))
#
#     url = base_url + 'vfetch/{0}'.format(return_object) + '/{0}?'.format(return_type)
#     if return_object == "vog":
#         if return_type not in ["msa", "hmm"]:
#             # return_type does not compare equal to any enum value:
#             raise ValueError("Invalid return object " + str(return_object))
#
#     elif return_object == "protein":
#         if return_type not in ["faa", "fna"]:
#             # return_type does not compare equal to any enum value:
#             raise ValueError("Invalid return object " + str(return_object))
#
#     # API GET request
#     r = requests.get(url=url, params=params)
#     try:
#         r.raise_for_status()
#     except requests.exceptions.HTTPError as e:
#         raise Exception(e.response.text)
#     response = r.json()
#     return response

def save_object(object, output_path="./test.txt"):
    """Saves the response object to output path"""

    with open(output_path, 'a') as file:
        for document in object:
            file.write(document)