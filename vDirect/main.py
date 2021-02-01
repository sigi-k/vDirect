import json

from API_requests import vsummary, vsearch, vfetch, vsearch_species, vsearch_protein
import sys
import argparse

"""
This is the implementation of the Argument Parser
"""


def main():
    # ToDo: URL paremeter für base URL. entweder nach den Options...
    parser = argparse.ArgumentParser(description='Welcome to vDirect!', epilog='Thank you for using vDirect!')
    subparsers = parser.add_subparsers(dest='command', help='Subcommands')

    vsearch_parser = subparsers.add_parser('vsearch', help='vsearch subparser help')
    vsummary_parser = subparsers.add_parser('vsummary', help='vsummary subparser help')
    vfetch_parser = subparsers.add_parser('vfetch', help='vfetch subparser help')

    # add subparsers for vSearch:
    vsearch_sps = vsearch_parser.add_subparsers(dest='return_object', help='subparsers for vsearch_parser')
    vog_search_parser = vsearch_sps.add_parser('vog', help='vsearch subparser for vog search')
    species_search_parser = vsearch_sps.add_parser('species', help='vsearch subparser for species search')
    protein_search_parser = vsearch_sps.add_parser('protein', help='vsearch subparser for protein search')

    # add arguments for vog_search_parser:
    vog_search_parser.add_argument('-id', type=str, action='append', nargs='+', dest='id',
                                   help="VOG ID(s)")
    vog_search_parser.add_argument('-pmin', type=int, action='store', nargs='?', dest='pmin',
                                   help="minimum number of proteins in the VOG")
    vog_search_parser.add_argument('-pmax', type=int, action='store', nargs='?', dest='pmax',
                                   help="maximum number of proteins in the VOG")
    vog_search_parser.add_argument('-smin', type=int, action='store', nargs='?', dest='smin',
                                   help="minimum number of species in the VOG")
    vog_search_parser.add_argument('-smax', type=int, action='store', nargs='?', dest='smax',
                                   help="maximum number of species in the VOG")
    vog_search_parser.add_argument('-mingLCA', type=int, action='store', nargs='?', dest='mingLCA',
                                   help="minimum number of genomes in the Last common ancestor")
    vog_search_parser.add_argument('-maxgLCA', type=int, action='store', nargs='?', dest='maxgLCA',
                                   help="maximum number of genomes in the Last common ancestor")
    vog_search_parser.add_argument('-mingGLCA', type=int, action='store', nargs='?', dest='mingGLCA',
                                   help="minimum number of genomes in the Group of the Last common ancestor")
    vog_search_parser.add_argument('-maxgGLCA', type=int, action='store', nargs='?', dest='maxgGLCA',
                                   help="maximum number of genomes in the Group of the Last common ancestor")
    vog_search_parser.add_argument('-fctcat', type=str, action='append', nargs='+', dest='functional_category',
                                   choices=['Xu', 'Xh', 'Xp', 'Xr', 'Xs'],
                                   help="functional category: Xu, Xh, Xp, Xr, Xs. If providing more than one, separate"
                                        " them by a space.")
    vog_search_parser.add_argument('-confct', type=str, action='append', nargs='+', dest='consensus_function',
                                   help="Concensus function")
    vog_search_parser.add_argument('-anc', '-ancestors', type=str, action='append', nargs='+', dest='ancestors',
                                   help="Ancestors")
    vog_search_parser.add_argument('-hs', '-highstringency', type=int, action='store', nargs='?', dest='h_stringency',
                                   choices=[0, 1],
                                   help="High stringency? '1' for True and '0' for False")
    vog_search_parser.add_argument('-ms', '-mediumstringency', type=int, action='store', nargs='?', dest='m_stringency',
                                   choices=[0, 1],
                                   help="Medium stringency? '1' for True and '0' for False")
    vog_search_parser.add_argument('-ls', '-lowstringency', type=int, action='store', nargs='?', dest='l_stringency',
                                   choices=[0, 1],
                                   help="Low stringency? '1' for True and '0' for False")
    vog_search_parser.add_argument('-vs', '-virusspecific', type=int, action='store', nargs='?', dest='virus_specific',
                                   choices=[0, 1],
                                   help="Virus specific? '1' for True and '0' for False")
    vog_search_parser.add_argument('-p', '-phage', type=str, action='store', nargs='?', dest='phages_nonphages',
                                   choices=['mixed', 'phages_only', 'np_only'],
                                   help="specify phages_only, nonphages only or mixed")
    vog_search_parser.add_argument('-prot', '-proteins', type=str, action='append', nargs='+', dest='proteins',
                                   help="Protein IDs")
    vog_search_parser.add_argument('-species', type=str, action='append', nargs='+', dest='species',
                                   help="Species Names, enclose names in quotes")
    vog_search_parser.add_argument('-tid', '-taxonid', type=int, action='append', nargs='+', dest='tax_id',
                                   help="Taxonomy ID(s)")
    vog_search_parser.add_argument('-u', '-union', action='store_true', dest='union',
                                   help="Do you want an (u)nion or an (i)ntersection search when searching VOGs by "
                                        "Species names or Taxonomy IDs? Default = False.")
    vog_search_parser.add_argument('-f', '-format', type=str, action='store', nargs='?', dest='format',
                                   choices=['json', 'df', 'stdout'], default='df',
                                   help="specify a format: 'json' or 'df' or 'stdout'")
    vog_search_parser.add_argument('-sort', type=str, action='store', nargs='?', dest='sort',
                                   help="Parameter sort results by")

    # add arguments for species_search_parser:
    species_search_parser.add_argument('-id', type=int, action='append', nargs='+', dest='ids',
                                       help="species ID(s)")
    species_search_parser.add_argument('-n', '-name', type=str, action='store', nargs='?', dest='name',
                                       help="search for species name or part of a species name")
    species_search_parser.add_argument('-p', '-phage', type=int, action='store', nargs='?', dest='phage',
                                       help="Enter '1' for searching for phages only and '0' when wanting to search "
                                            "for nonphages only")
    species_search_parser.add_argument('-s', '-source', type=str, action='store', nargs='?', dest='source',
                                       help="search for species found in the specified source")
    species_search_parser.add_argument('-v', '-version', type=int, action='store', nargs='?', dest='version',
                                       help="search for species found in the specified version")
    species_search_parser.add_argument('-f', '-format', type=str, action='store', nargs='?', dest='format',
                                       choices=['json', 'df', 'stdout'], default='stdout',
                                       help="specify a format: 'json' or 'df' or 'stdout'")
    species_search_parser.add_argument('-sort', type=str, action='store', nargs='?', dest='sort',
                                       help="Parameter sort results by")

    # add arguments for protein_search_parser:
    protein_search_parser.add_argument('-tid', '-taxonid', type=int, action='append', nargs='+', dest='taxon_id',
                                       help="taxon ID(s) of the species")
    protein_search_parser.add_argument('-n', '-name', type=str, action='append', nargs='+', dest='species_name',
                                       help="search for species name or part of species name")
    protein_search_parser.add_argument('-vid', '-vogid', type=str, action='append', nargs='+', dest='VOG_id',
                                       help="search for VOG IDs")
    protein_search_parser.add_argument('-f', '-format', type=str, action='store', nargs='?', dest='format',
                                       choices=['json', 'df', 'stdout'], default='df',
                                       help="specify a format: 'json', 'df' or 'stdout'")
    protein_search_parser.add_argument('-sort', type=str, action='store', nargs='?', dest='sort',
                                       help="Parameter sort results by")

    # add subparsers for vSummary:
    vsummary_sps = vsummary_parser.add_subparsers(dest='return_object', help='subparsers for vsummary_parser')
    vog_summary_parser = vsummary_sps.add_parser('vog', help='vsummary subparser for vog summary')
    species_summary_parser = vsummary_sps.add_parser('species', help='vsummary subparser for species summary')
    protein_summary_parser = vsummary_sps.add_parser('protein', help='vsummary subparser for protein summary')

    # add arguments for vog_summary_parser:
    vog_summary_parser.add_argument('-id', type=str, nargs='+', dest='id', default=sys.stdin,
                                    help="VOG unique ID(s)")
    vog_summary_parser.add_argument('-f', '-format', type=str, action='store', nargs='?', dest='format',
                                    choices=['json', 'df'], help="specify a format: 'json' or 'df'")
    # vog_summary_parser.add_argument('-sort', type=str, action='store', nargs='?', dest='sort',
    #                                    help="Parameter sort results by")

    # add arguments for protein_summary_parser:
    protein_summary_parser.add_argument('-id', type=str, nargs='+', dest='id', default=sys.stdin,
                                        help="protein ID(s)")
    protein_summary_parser.add_argument('-f', '-format', type=str, action='store', nargs='?', dest='format',
                                        choices=['json', 'df'], help="specify a format: 'json' or 'df'")
    # protein_summary_parser.add_argument('-sort', type=str, action='store', nargs='?', dest='sort',
    #                                    help="Parameter sort results by")

    # add arguments for species_summary_parser:
    species_summary_parser.add_argument('-id', type=int, nargs='+', dest='id', default=sys.stdin,
                                        help="taxon ID(s)")
    species_summary_parser.add_argument('-f', '-format', type=str, action='store', nargs='?', dest='format',
                                        choices=['json', 'df'], help="specify a format: 'json' or 'df'")
    # species_summary_parser.add_argument('-sort', type=str, action='store', nargs='?', dest='sort',
    #                                    help="Parameter sort results by")

    # add subparsers for vFetch:
    vfetch_sps = vfetch_parser.add_subparsers(dest='return_object', help='subparsers for vfetch_parser')
    vog_fetch_parser = vfetch_sps.add_parser('vog', help='vfetch subparser for vog fetch')
    # # species fetch does not exist
    # species_fetch_parser = vfetch_sps.add_parser('species', help='vfetch subparser for species fetch')
    protein_fetch_parser = vfetch_sps.add_parser('protein', help='vfetch subparser for protein fetch')

    # add arguments for vog_fetch_parser:
    vog_fetch_parser.add_argument(type=str, action='store', choices=['hmm', 'msa'],
                                  dest='return_type', help="choose 'hmm' or 'msa'")
    vog_fetch_parser.add_argument('-id', type=str, nargs='+', dest='id', default=sys.stdin,
                                  help="VOG unique identifiers")

    # add arguments for protein_fetch_parser:
    protein_fetch_parser.add_argument(type=str, action='store', choices=['faa', 'fna'],
                                      dest='return_type', help="choose 'faa' or 'fna'")
    protein_fetch_parser.add_argument('-id', type=str, nargs='+', dest='id', default=sys.stdin,
                                      help="Protein identifiers")

    # ToDo Base URL as environment variable?
    parser.add_argument('-base', type=str, action='store', nargs='?', dest='base_url', help="specify the base URL")

    args = parser.parse_args()


    # ToDo: piping when search returns an error -> should recognize it.
    if args.command == 'vfetch':
        if not sys.stdin.isatty():
            id = args.id.read().split()
            # check if dataframe: if yes, get every 2nd value
            if id[1] == '0':
                id = id[2::2]
            # check if json format:
            if id[0][0] == '[':
                raise Exception("The search output cannot be 'json' when piping.")
        else:
            id = args.id

        print(vfetch(return_object=args.return_object, return_type=args.return_type, id=id, base_url=args.base_url),
              file=sys.stdout)


    elif args.command == 'vsummary':
        if args.return_object == 'species':
            if not sys.stdin.isatty():
                input = args.id.read().split()
                try:
                    if input[0][0] == '[':
                        raise KeyError("The search output cannot be in the 'json' format when piping.")
                    # ToDo: better way to check for exception?
                    if input[0] == 'No':
                        raise IndexError("No species match the search criteria.")
                    elif input[0] == 'taxon_id':
                        id = input[2::2]
                    else:
                        id = []
                        for ele in input:
                            id.append(int(ele))
                except KeyError as k:
                    raise Exception(k)
                except IndexError as i:
                    raise Exception(i)
                except Exception:
                    raise Exception("Species search not successful.")
            else:
                id = args.id
            print(vsummary(return_object=args.return_object, format=args.format, taxon_id=id, base_url=args.base_url),
                  file=sys.stdout)

        elif args.return_object == 'protein' or args.return_object == 'vog':
            if not sys.stdin.isatty():
                # ToDo: ????
                # input = args.id.read()
                # print(input)
                inp = json.loads(args.id.read())
                print(inp)
                # id = args.id.read().split()
                # # check if dataframe: if yes, get every 2nd value
                # if id[1] == '0':
                #     id = id[2::2]
                # # check if json format:
                # if id[0][0] == '[':
                #     raise Exception("The search output cannot be in the 'json' format when piping.")
            else:
                id = args.id
            print(vsummary(return_object=args.return_object, format=args.format, id=id, base_url=args.base_url),
                  file=sys.stdout)
        else:
            raise Exception("Unknown return object")



#Todo: finish SEARCHES
    elif args.command == 'vsearch':
        if args.return_object == 'species':
            r = vsearch_species(base_url=args.base_url, ids=args.ids, name=args.name, phage=args.phage, source=args.source, version=args.version, sort=args.sort)

        elif args.return_object == 'protein':
            r = vsearch_protein(base_url=args.base_url, species_name=args.species_name, taxon_id=args.taxon_id, VOG_id=args.VOG_id, sort=args.sort)

    #ToDo: Add remaining parameters
        elif args.return_object == 'vog':
            r = vsearch_protein(base_url=args.base_url, ids=args.id, pmin=args.pmin, pmax=args.pmax, smin=args.smin, smax=args.smax,
                                functional_category=args.functional_category, consensus_function=args.consensus_function,
                                mingLCA=args.mingLCA, sort=args.sort, union=args.union)

            # maxgLCA: Optional[int] = None,
            # mingGLCA: Optional[int] = None,
            # maxgGLCA: Optional[int] = None,
            # ancestors: Optional[Set[str]] = Query(None),
            # h_stringency: Optional[bool] = None,
            # m_stringency: Optional[bool] = None,
            # l_stringency: Optional[bool] = None,
            # virus_specific: Optional[bool] = None,
            # phages_nonphages: Optional[str] = None,
            # proteins: Optional[Set[str]] = Query(None),
            # species: Optional[Set[str]] = Query(None),
            # tax_id: Optional[Set[int]] = Query(None),
        else:
            raise ValueError("invalid return object")

        #ToDo: how to print it..?
        if r.status_code == 200:
            for ele in r.json():
                print(ele['taxon_id'], file=sys.stdout)
            print(json.dumps(r.json()), file=sys.stdout)
        else:
            sys.exit(r.json().get('detail'))


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print("EXCEPTION")
        print(ex, file=sys.stdout)
        sys.exit(1)

# ToDo:
"""
When piping: 
if no results -> should return "no matches for the search criteria"
$ python vdirect.py vsearch vog -pmax 10 | python vdirect.py vsummary vog
Now works!
$ python vdirect.py vsearch vog -pmax 10 -pmin 10 | python vdirect.py vsummary vog
works!

python main.py -base http://127.0.0.1:8000/ vsearch vog -pmax 10 -pmin 10
python main.py -base http://127.0.0.1:8000/ vsearch species -n corona
python main.py -base http://127.0.0.1:8000/ vsearch proteins -n corona


Not working:
python vdirect.py vsearch vog -pmax 10 -pmin 33 | python vdirect.py vsummary vog
"""
