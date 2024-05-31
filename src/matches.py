import json

DC_TERMS = "http://purl.org/dc/terms/"
DC_ELEMENTS = "http://purl.org/dc/elements/1.1/"

def llm_matches(keys, llm_matches_path, correspondences):

    with open(llm_matches_path, "r") as fout:
        matches = json.load(fout)

    llm_matches =  matches["matching"]

    for key in keys:
        if not key.startswith("@"):
            for element in llm_matches.keys():
                if key.split(":")[1] == element:
                    correspondences[key] = llm_matches[element].split(":")[-1]
        
    return correspondences

def get_dc_terms(keys, terms):
    for key in keys:
        if not key.startswith("@"):
            terms[key] = key.split(":")[1]

    return terms


def get_matches(data, llm_matches_path, elements_path, terms_path):
    correspondence = {}

    if DC_ELEMENTS in data.values():
        correspondence = llm_matches(data.keys(), llm_matches_path, correspondence)
        
    
    if DC_TERMS in data.values():
        correspondence = get_dc_terms(data.keys(), correspondence)
    return correspondence
