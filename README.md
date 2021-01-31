# VDirect

VDirect is a user friendly tool to build Requests to retrieve information from the VOGDB-API.


## Installation

```bash
pip install 
```

## Using the VOGDB-API with vDirect
```bash
Below is the search hierarchy: first specify vsearch, vsummary or vfetch, then the subsequent parameters.
'-h' provides a list of the parameters that can be used for filtering.

python vdirect.py vsearch     species   species_search_parameters
                              protein   protein_search_parameters
                              vog       vog_search_parameters
                  vsummary    species   species_ids
                              protein   protein_ids
                              vog       vog_ids
                  vfetch      protein   faa   protein_ids
                                        fna   protein_ids
                              vog       hmm   vog_ids
                                        msa   vog_ids
```

