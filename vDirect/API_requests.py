import logging
import requests

"""
Here URLs are built and Requests are made.
"""

# set log level for requests module
urllib3_logger = logging.getLogger('urllib3')
urllib3_logger.setLevel(logging.CRITICAL)


# GET REQUESTS FOR VFETCH
def get_vfetch_vog_msa(base_url, id):
    url = base_url + 'vfetch/vog/msa'
    params = {
        "id": id
    }
    return requests.get(url, params)


def get_vfetch_vog_hmm(base_url, id):
    url = base_url + 'vfetch/vog/hmm'
    params = {
        "id": id
    }
    return requests.get(url, params)


def get_vfetch_protein_faa(base_url, id):
    url = base_url + 'vfetch/protein/faa'
    params = {
        "id": id
    }
    return requests.get(url, params)


def get_vfetch_protein_fna(base_url, id):
    url = base_url + 'vfetch/protein/fna'
    params = {
        "id": id
    }
    return requests.get(url, params)


# POST REQUESTS FOR VFETCH
def post_vfetch_vog_msa(base_url, input):
    url = base_url + 'vfetch/vog/msa'
    return requests.post(url, input)


def post_vfetch_vog_hmm(base_url, input):
    url = base_url + 'vfetch/vog/hmm'
    return requests.post(url, input)


def post_vfetch_protein_faa(base_url, input):
    url = base_url + 'vfetch/protein/faa'
    return requests.post(url, input)


def post_vfetch_protein_fna(base_url, input):
    url = base_url + 'vfetch/protein/fna'
    return requests.post(url, input)



# GET REQUESTS FOR VSUMMARY
def get_vsummary_species(base_url, taxon_id):
    """Yield the response to a species summary of a query."""
    url = base_url + 'vsummary/species'
    params = {
        "taxon_id": taxon_id
    }
    return requests.get(url, params)


def get_vsummary_protein(base_url, id):
    """Yield the response to a protein summary of a query."""
    url = base_url + 'vsummary/protein'
    params = {
        "id": id
    }
    return requests.get(url, params)


def get_vsummary_vog(base_url, id):
    """Yield the response to a vog summary of a query."""
    url = base_url + 'vsummary/vog'
    params = {
        "id": id
    }
    return requests.get(url, params)


# POST REQUESTS FOR VSUMMARY
def post_vsummary_species(base_url, input):
    """Yield the response to a species summary of a query."""
    url = base_url + 'vsummary/species'
    return requests.post(url, input)


def post_vsummary_protein(base_url, input):
    """Yield the response to a protein summary of a query."""
    url = base_url + 'vsummary/protein'
    return requests.post(url, input)


def post_vsummary_vog(base_url, input):
    """Yield the response to a vog summary of a query."""
    url = base_url + 'vsummary/vog'
    return requests.post(url, input)



# GET REQUESTS FOR VSEARCH
def vsearch_protein(base_url, species_name, taxon_id, VOG_id, sort):
    url = base_url + 'vsearch/protein'

    params = {
        "species_name": species_name,
        "taxon_id": taxon_id,
        "VOG_id": VOG_id,
        "sort": sort
    }
    return requests.get(url, params)


def vsearch_vog(base_url, id, pmin, pmax, smin, smax, functional_category, consensus_function, mingLCA, maxgLCA, mingGLCA,
                maxgGLCA, ancestors, h_stringency, m_stringency, l_stringency, virus_specific, phages_nonphages,
                proteins, species, tax_id, sort, union=False):
    url = base_url + 'vsearch/vog'

    for number in pmin, pmax, smin, smax:
        if number:
            assert number >= 0, f'number {number} cannot be smaller than 0.'

    params = {
        "id": id,
        "pmin": pmin,
        "pmax": pmax,
        "smin": smin,
        "smax": smax,
        "functional_category": functional_category,
        "consensus_function": consensus_function,
        "mingLCA": mingLCA,
        "maxgLCA": maxgLCA,
        "mingGLCA": mingGLCA,
        "maxgGLCA": maxgGLCA,
        "ancestors": ancestors,
        "h_stringency": h_stringency,
        "m_stringency": m_stringency,
        "l_stringency": l_stringency,
        "virus_specific": virus_specific,
        "phages_nonphages": phages_nonphages,
        "proteins": proteins,
        "species": species,
        "tax_id": tax_id,
        "sort": sort,
        "union": union
    }
    return requests.get(url, params)


def vsearch_species(base_url, ids, name, phage, source, version, sort):
    url = base_url + 'vsearch/species'
    params = {
        "ids": ids,
        "name": name,
        "phage": phage,
        "source": source,
        "version": version,
        "sort": sort
    }
    return requests.get(url, params)




# function to save hmm vFetch response objects (for now just hmm, msa)
def save_object(object, output_path="./test.txt"):
    """Saves the response object to output path"""

    with open(output_path, 'a') as file:
        for document in object:
            file.write(document)