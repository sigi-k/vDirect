from vDirect import API_requests


base_url = "http://127.0.0.1:8000/"

class TestSpeciesSearch:
    def test_vsearch_species_ids(self):
        taxon_id = [11128, 1002724]
        url = API_requests.vsearch_species(base_url, taxon_id, name=None, phage=None, source=None).url
        expected = "http://127.0.0.1:8000/vsearch/species?taxon_id=11128&taxon_id=1002724"
        assert url.lower() == expected.lower()

    def test_vsearch_species_multiple_paras(self):
        taxon_id = [11128, 100272433]
        phage = True
        source = "WrongSource"
        url = API_requests.vsearch_species(base_url, taxon_id, name=None, phage=phage, source=source).url
        expected = "http://127.0.0.1:8000/vsearch/species?taxon_id=11128&taxon_id=100272433&phage=true&source=WrongSource"
        assert url.lower() == expected.lower()

    def test_vsearch_species_name(self):
        name = ["Corona", "Banana"]
        url = API_requests.vsearch_species(base_url, taxon_id=None, name=name, phage=None, source=None).url
        expected = "http://127.0.0.1:8000/vsearch/species?name=Corona&name=Banana"
        assert url.lower() == expected.lower()


class TestProteinSearch:
    def test_vsearch_protein_name(self):
        species_name = ["corona"]
        url = API_requests.vsearch_protein(base_url, species_name=species_name, taxon_id=None, VOG_id=None).url
        expected = "http://127.0.0.1:8000/vsearch/protein?species_name=corona"
        assert url.lower() == expected.lower()

    def test_vsearch_protein_taxID(self):
        taxon_id = [11128, 1002427]
        url = API_requests.vsearch_protein(base_url, species_name=None, taxon_id=taxon_id, VOG_id=None).url
        expected = "http://127.0.0.1:8000/vsearch/protein?taxon_id=11128&taxon_id=1002427"
        assert url.lower() == expected.lower()

    def test_vsearch_protein_taxID_name(self):
        species_name = ["corona"]
        taxon_id = [11128, 1002427]
        url = API_requests.vsearch_protein(base_url, species_name=species_name, taxon_id=taxon_id, VOG_id=None).url
        expected = "http://127.0.0.1:8000/vsearch/protein?species_name=corona&taxon_id=11128&taxon_id=1002427"
        assert url.lower() == expected.lower()

    def test_vsearch_protein_VOG_id(self):
        VOG_id = ["VOG00078", "VOG00001"]
        url = API_requests.vsearch_protein(base_url, species_name=None, taxon_id=None, VOG_id=VOG_id).url
        expected = "http://127.0.0.1:8000/vsearch/protein?VOG_id=VOG00078&VOG_id=VOG00001"
        assert url.lower() == expected.lower()

class TestVOGSearch:
    params = {
        "id": ["VOG00078", "VOG00001"],
        "pmin": 100,
        "pmax": 100,
        "smin": 54,
        "smax": 78,
        "functional_category": "Xu",
        "consensus_function": "transferase",
        "mingLCA": 66,
        "maxgLCA": 34,
        "mingGLCA": 10,
        "maxgGLCA": 200,
        "ancestors": ["Viruses", "Coronaviridae"],
        "h_stringency": True,
        "m_stringency": True,
        "l_stringency": True,
        "virus_specific": False,
        "phages_nonphages": "phages_only",
        "proteins": ["11128.NP_150077.1"],
        "species": ["Bovine coronavirus"],
        "tax_id": [11128, 11118],
        "union": True
    }
    def test_vsearch_vog_id_single(self):
        url = API_requests.vsearch_vog(base_url, id=["VOG00067"], pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?id=VOG00067"
        assert url.lower() == expected.lower()

    def test_vsearch_vog_ids(self):
        url = API_requests.vsearch_vog(base_url, id=self.params.get("id"), pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?id=VOG00078&id=VOG00001"
        assert url.lower() == expected.lower()

    def test_vsearch_concensus_function(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=self.params.get("consensus_function"), mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?consensus_function=transferase"
        assert url.lower() == expected.lower()

    def test_vsearch_ancestors_single(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=["Coronaviridae"], h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?ancestors=coronaviridae"
        assert url.lower() == expected.lower()

    def test_vsearch_ancestors(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=self.params.get("ancestors"), h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?ancestors=viruses&ancestors=coronaviridae"
        assert url.lower() == expected.lower()

    def test_vsearch_phages_nonphages(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=self.params.get("phages_nonphages"),
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?phages_nonphages=phages_only"
        assert url.lower() == expected.lower()

    def test_vsearch_virus_specific(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=self.params.get("virus_specific"), phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?virus_specific=false"
        assert url.lower() == expected.lower()

    def test_vsearch_species(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None,
                                       smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None,
                                       phages_nonphages=None,
                                       proteins=None, species=self.params.get("species"), tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?species=Bovine%20coronavirus"
        # encode space in the url as '%20' instead of '+'
        url = url.replace('+', "%20")
        assert url.lower() == expected.lower()

    def test_vsearch_high_stringency(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=self.params.get("h_stringency"), m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?h_stringency=true"
        assert url.lower() == expected.lower()

    def test_vsearch_medium_stringency(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=self.params.get("m_stringency"),
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?m_stringency=true"
        assert url.lower() == expected.lower()

    def test_vsearch_low_stringency(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=self.params.get("l_stringency"), virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?l_stringency=true"
        assert url.lower() == expected.lower()

    def test_vsearch_pmin(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=self.params.get("pmin"), pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?pmin=100"
        assert url.lower() == expected.lower()

    def test_vsearch_pmax(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=self.params.get("pmax"), smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?pmax=100"
        assert url.lower() == expected.lower()

    def test_vsearch_smin(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=self.params.get("smin"),
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?smin=54"
        assert url.lower() == expected.lower()

    def test_vsearch_smax(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=None,
                                       smax=self.params.get("smax"), functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?smax=78"
        assert url.lower() == expected.lower()

    def test_vsearch_mingLCA(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=self.params.get("mingLCA"),
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?mingLCA=66"
        assert url.lower() == expected.lower()

    def test_vsearch_maxgLCA(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=self.params.get("maxgLCA"), mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?maxgLCA=34"

        assert url.lower() == expected.lower()

    def test_vsearch_mingGLCA(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=self.params.get("mingGLCA"),
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?mingGLCA=10"
        assert url.lower() == expected.lower()

    def test_vsearch_maxgGLCA(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=self.params.get("maxgGLCA"), ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?maxgGLCA=200"
        assert url.lower() == expected.lower()

    def test_vsearch_functional_category(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=self.params.get("functional_category"), consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?functional_category=Xu"
        assert url.lower() == expected.lower()

    def test_vsearch_functional_category_2(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=["Xu", "Xr"], consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?functional_category=Xu&functional_category=Xr"
        assert url.lower() == expected.lower()

    def test_vsearch_proteins(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=self.params.get("proteins"), species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?proteins=11128.NP_150077.1"
        assert url.lower() == expected.lower()

    def test_vsearch_tax_id(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=self.params.get("tax_id"), union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?tax_id=11128&tax_id=11118"
        assert url.lower() == expected.lower()

    def test_vsearch_tax_id_union_true(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=self.params.get("tax_id"), union=True).url
        expected = "http://127.0.0.1:8000/vsearch/vog?tax_id=11128&tax_id=11118&union=true"
        assert url.lower() == expected.lower()

    def test_vsearch_tax_id_union_false(self):
        url = API_requests.vsearch_vog(base_url, id=None, pmin=None, pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=self.params.get("tax_id"), union=False).url
        expected = "http://127.0.0.1:8000/vsearch/vog?tax_id=11128&tax_id=11118&union=false"
        assert url.lower() == expected.lower()

    # Multiple parameters:
    def test_vsearch_vog_id_pmin(self):
        url = API_requests.vsearch_vog(base_url, id=self.params.get("id"), pmin=self.params.get("pmin"), pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=None, h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?id=VOG00078&id=VOG00001&pmin=100"
        assert url.lower() == expected.lower()

    def test_vsearch_vog_id_pmin_ancestors(self):
        url = API_requests.vsearch_vog(base_url, id=self.params.get("id"), pmin=self.params.get("pmin"), pmax=None, smin=None,
                                       smax=None, functional_category=None, consensus_function=None, mingLCA=None,
                                       maxgLCA=None, mingGLCA=None,
                                       maxgGLCA=None, ancestors=self.params.get("ancestors"), h_stringency=None, m_stringency=None,
                                       l_stringency=None, virus_specific=None, phages_nonphages=None,
                                       proteins=None, species=None, tax_id=None, union=None).url
        expected = "http://127.0.0.1:8000/vsearch/vog?id=VOG00078&id=VOG00001&pmin=100&ancestors=Viruses&ancestors=coronaviridae"
        assert url.lower() == expected.lower()


class TestSummary:
    def test_vsummary_species_single(self):
        url = API_requests.get_vsummary_species(base_url, taxon_id=[11128]).url
        expected = "http://127.0.0.1:8000/vsummary/species?taxon_id=11128"
        assert url.lower() == expected.lower()

    def test_vsummary_species_multiple(self):
        url = API_requests.get_vsummary_species(base_url, taxon_id=[11128, 101570]).url
        expected = "http://127.0.0.1:8000/vsummary/species?taxon_id=11128&taxon_id=101570"
        assert url.lower() == expected.lower()

    def test_vsummary_protein_single(self):
        url = API_requests.get_vsummary_protein(base_url, id=["1034149.YP_009198699.1"]).url
        expected = "http://127.0.0.1:8000/vsummary/protein?id=1034149.YP_009198699.1"
        assert url.lower() == expected.lower()

    def test_vsummary_protein_multiple(self):
        url = API_requests.get_vsummary_protein(base_url, id=["1034149.YP_009198699.1", "101570.YP_224152.1"]).url
        expected = "http://127.0.0.1:8000/vsummary/protein?id=1034149.YP_009198699.1&id=101570.YP_224152.1"
        assert url.lower() == expected.lower()

    def test_vsummary_vog_single(self):
        url = API_requests.get_vsummary_vog(base_url, id=["VOG00099"]).url
        expected = "http://127.0.0.1:8000/vsummary/vog?id=VOG00099"
        assert url.lower() == expected.lower()

    def test_vsummary_vog_multiple(self):
        url = API_requests.get_vsummary_vog(base_url, id=["VOG00099", "VOG01293"]).url
        expected = "http://127.0.0.1:8000/vsummary/vog?id=VOG00099&id=VOG01293"
        assert url.lower() == expected.lower()


class TestFetch:
    def test_vfetch_protein_faa_single(self):
        url = API_requests.get_vfetch_protein_faa(base_url, id=["1034149.YP_009198699.1"]).url
        expected = "http://127.0.0.1:8000/vfetch/protein/faa?id=1034149.YP_009198699.1"
        assert url.lower() == expected.lower()

    def test_vfetch_protein_faa_multiple(self):
        url = API_requests.get_vfetch_protein_faa(base_url, id=["1034149.YP_009198699.1", "101570.YP_224152.1"]).url
        expected = "http://127.0.0.1:8000/vfetch/protein/faa?id=1034149.YP_009198699.1&id=101570.YP_224152.1"
        assert url.lower() == expected.lower()

    def test_vfetch_protein_fna_single(self):
        url = API_requests.get_vfetch_protein_fna(base_url, id=["1034149.YP_009198699.1"]).url
        expected = "http://127.0.0.1:8000/vfetch/protein/fna?id=1034149.YP_009198699.1"
        assert url.lower() == expected.lower()

    def test_vfetch_protein_fna_multiple(self):
        url = API_requests.get_vfetch_protein_fna(base_url, id=["1034149.YP_009198699.1", "101570.YP_224152.1"]).url
        expected = "http://127.0.0.1:8000/vfetch/protein/fna?id=1034149.YP_009198699.1&id=101570.YP_224152.1"
        assert url.lower() == expected.lower()

    def test_vfetch_vog_msa_sinlge(self):
        url = API_requests.get_vfetch_vog_msa(base_url, id=["VOG00099"]).url
        expected = "http://127.0.0.1:8000/vfetch/vog/msa?id=VOG00099"
        assert url.lower() == expected.lower()

    def test_vfetch_vog_msa_multiple(self):
        url = API_requests.get_vfetch_vog_msa(base_url, id=["VOG00099", "VOG01293"]).url
        expected = "http://127.0.0.1:8000/vfetch/vog/msa?id=VOG00099&id=VOG01293"
        assert url.lower() == expected.lower()

    def test_vfetch_vog_hmm_sinlge(self):
        url = API_requests.get_vfetch_vog_hmm(base_url, id=["VOG00099"]).url
        expected = "http://127.0.0.1:8000/vfetch/vog/hmm?id=VOG00099"
        assert url.lower() == expected.lower()

    def test_vfetch_vog_hmm_multiple(self):
        url = API_requests.get_vfetch_vog_hmm(base_url, id=["VOG00099", "VOG01293"]).url
        expected = "http://127.0.0.1:8000/vfetch/vog/hmm?id=VOG00099&id=VOG01293"
        assert url.lower() == expected.lower()
