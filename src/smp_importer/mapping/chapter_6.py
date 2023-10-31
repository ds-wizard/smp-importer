from rdflib import Graph

from smp_importer.model import MappingExecutor
from smp_importer.rdf_helper import get_object_by


def process_chapter_6(g: Graph, executor: MappingExecutor, node: str):
    # ******************************************************************************************************************
    # CHAPTER 6: Reproducibility
    # ******************************************************************************************************************
    chapter_uuid = "7426b2df-f9ed-4e65-a978-5995183e4e63"

    # ------------------------------------------------------------------------------------------------------------------
    # QUESTION: Do you provide releases of your software?
    question_uuid = "f55943d2-5c95-49b6-ba8f-a56ba76fc484"
    value = get_object_by(g, node, "schema:softwareVersion")
    if value is not None:
        # ANSWER: Yes
        answer_uuid = '27efa00f-b9d4-4134-9d36-e29f9037f9fb'
        executor.result_set_reply(f'{chapter_uuid}.{question_uuid}', answer_uuid)
        # QUESTION: What is the version of the current release
        question_uuid_2 = "dc7b8ef8-aa1d-4abf-9a12-f3bbf52f59af"
        executor.result_set_reply(f'{chapter_uuid}.{question_uuid}.{answer_uuid}.{question_uuid_2}', value)
    else:
        # ANSWER: No
        answer_uuid = '65a96f96-109a-4f90-883f-843d19d8ac45'
        executor.result_set_reply(f'{chapter_uuid}.{question_uuid}', answer_uuid)
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    # QUESTION: Do you state how to report bugs and/or usability problems by the software user(s)?
    question_uuid = "ccf5634b-6279-409c-8b64-f617ee7f345a"
    value = get_object_by(g, node, "schema:discussionURL")
    if value is not None:
        # ANSWER: Yes
        answer_uuid = '6f85e7b0-c1d1-490c-94d4-7724bd550a4a'
        executor.result_set_reply(f'{chapter_uuid}.{question_uuid}', answer_uuid)
    else:
        # ANSWER: No
        answer_uuid = '550d307b-1620-4b45-8af9-025648d310e9'
        executor.result_set_reply(f'{chapter_uuid}.{question_uuid}', answer_uuid)
    # ------------------------------------------------------------------------------------------------------------------
