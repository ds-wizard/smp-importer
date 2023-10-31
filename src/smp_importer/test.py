from pprint import pprint

import fixtures
from importer import process

result = process(fixtures.FIXTURE_1, "application/ld+json")

pprint(result)
print("------------------------------------------------------------------")
print(f'The size of imported replies is {len(result["actions"])}')
