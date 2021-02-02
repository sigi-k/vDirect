# VDirect

VDirect is a user friendly tool to retrieve information from the VOGDB-API. It is a utility that builds URLs and sends requests to the server.

##Dependencies:
You can install the dependencies with
```bash
pip install argparse
pip install requests
```

## Installation
vDirect can be installed with:
```bash
pip install vDirect
```

## Using the VOGDB-API with vDirect

Below is the search hierarchy: first specify vsearch, vsummary or vfetch, then the subsequent parameters.
'-h' provides a list of the parameters that can be used for filtering.
```bash
    vdirect       vsearch     species   species_search_parameters
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
## Examples
```bash
vdirect vsearch vog -pmin 10 -pmax 20 -fctcat Xu

vdirect vsummary vog -id VOG00001 VOG00033

vdirect vfetch vog msa -id VOG00001 VOG00033 VOG00002

vdirect vfetch protein faa -id VOG00001 VOG00033 VOG00002
```
## Authors

Nikola Vinko*, Sigi Koizar*

*University of Vienna
