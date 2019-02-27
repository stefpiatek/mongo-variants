import json
import pymongo

from pymongo import MongoClient

client = MongoClient('localhost', 27017)


variants = 'input/all_vep_variants.json'

db = client.variant_database

collection = db.variants


variant_checker = {}

with open(variants, 'r') as variants:
    for variant in variants:
        variant_dict = {}
        variant_key = ""
        v = json.loads(variant)
        collection.insert_one(v)

        '''
        for key, value in v.items():
            if key == 'mappings':
                for anno_name, anno_value in value[0].items():
                    if anno_name == "location" or anno_name == "allele_string":
                        variant_key += anno_value
            elif key == "name":
                v[key] = [value]
        if variant_key not in variant_checker.keys():
            variant_checker[variant_key] = v
        elif variant_checker[variant_key] != v:
            tmp_original = dict(variant_checker[variant_key])
            tmp_current = dict(v)
            for field in ["evidence", "synonyms", "name"]:
                merged = dict(tmp_original)
                merged[field] = tmp_original.pop(field)
                merged[field] += tmp_current.pop(field)
            if tmp_original != tmp_current:
                print(tmp_original)
                print(tmp_current)
                print("---")
        '''



