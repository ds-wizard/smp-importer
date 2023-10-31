from rdflib import Graph

from smp_importer.model import MappingExecutor
from smp_importer.rdf_helper import get_object_by


def process_chapter_7(g: Graph, executor: MappingExecutor, node: str):
    # ******************************************************************************************************************
    # CHAPTER 7: Recognition
    # ******************************************************************************************************************
    chapter_uuid = "87f6b5db-1f0e-4ba9-a7cb-82ec050bb4cf"

    # ------------------------------------------------------------------------------------------------------------------
    # QUESTION: Do you include citation information (i.e. how to cite your software in the form of citation.cff, codemeta.json or bibtex)?
    question_uuid = "ac635be0-839d-4bb2-aa90-6eb2e80c2ed6"
    value = get_object_by(g, node, "schema:citation")
    if value is not None:
        # ANSWER: Yes
        answer_uuid = '463c3b6e-cf96-43e5-a189-f840f7ea93db'
        executor.result_set_reply(f'{chapter_uuid}.{question_uuid}', answer_uuid)
    else:
        # ANSWER: No
        answer_uuid = 'b62bb0f8-d9b2-4f8a-a13e-7e8572ba94a7'
        executor.result_set_reply(f'{chapter_uuid}.{question_uuid}', answer_uuid)
    # ------------------------------------------------------------------------------------------------------------------
