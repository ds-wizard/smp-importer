from rdflib import Graph

from smp_importer.model import MappingExecutor
from smp_importer.rdf_helper import get_object_by, get_objects_by


def process_chapter_1(g: Graph, executor: MappingExecutor, node: str):
    # ******************************************************************************************************************
    # CHAPTER 1: Accessibility & License
    # ******************************************************************************************************************
    chapter_uuid = "6230f637-cf55-4055-b2e7-6cde6711aa51"

    # ------------------------------------------------------------------------------------------------------------------
    # QUESTION: What is the name of the software?
    question_uuid = "56adb0ca-3e80-45fa-8fbe-1f3508d6032b"
    value = str(get_object_by(g, node, "schema:name"))
    executor.result_set_reply(f'{chapter_uuid}.{question_uuid}', value)
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    # QUESTION: How can the software be accessed by third parties?
    question_uuid = "d86ca238-e2fc-41cf-b4ea-13dd903c0453"
    is_accessible_for_free = str(get_object_by(g, node, "schema:isAccessibleForFree"))
    conditions_of_access = str(get_object_by(g, node, "schema:conditionsOfAccess"))
    if is_accessible_for_free:
        # ANSWER: Publicly available (e.g. GitHub, via URL, etc.)
        answer_uuid = 'b58c3e29-f373-4121-bfe1-7878b53aa656'
        executor.result_set_reply(f'{chapter_uuid}.{question_uuid}', answer_uuid)
        code_repository = str(get_object_by(g, node, "schema:codeRepository"))
        if code_repository is not None:
            question_uuid_2 = '843c467a-de1c-475c-9b01-aec90a318716'
            executor.result_set_reply(f'{chapter_uuid}.{question_uuid}.{answer_uuid}.{question_uuid_2}',
                                      code_repository)
    elif conditions_of_access is not None:
        # ANSWER: Other
        answer_uuid = '3100dfe6-ef85-4206-9d3e-11e8c32f7637'
        executor.result_set_reply(f'{chapter_uuid}.{question_uuid}', answer_uuid)
        code_repository = str(get_object_by(g, node, "schema:codeRepository"))
        if code_repository is not None:
            question_uuid_2 = '4a56b2d9-151e-479b-93a3-dfe45d599f3b'
            executor.result_set_reply(f'{chapter_uuid}.{question_uuid}.{answer_uuid}.{question_uuid_2}',
                                      code_repository)
    else:
        # ANSWER: Not relevant/applicable to me
        answer_uuid = 'fb09e051-afb5-44fa-98e6-8a772e7e4562'
        executor.result_set_reply(f'{chapter_uuid}.{question_uuid}', answer_uuid)
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    # QUESTION: Does your software have a license?
    question_uuid = "22c70672-edd2-46cd-a422-bb857bc46def"
    licenses = list(get_objects_by(g, node, "schema:license"))
    if len(licenses) > 0:
        # ANSWER: Yes
        answer_uuid = "d488fe17-df1a-4583-8829-fc0d0f02aeec"
        executor.result_set_reply(f'{chapter_uuid}.{question_uuid}', answer_uuid)
        # QUESTION: What is the license of your software?
        question_uuid_2 = "327b65c4-3782-4b93-adb0-6db7b9f19e84"
        license_names = ','.join([str(get_object_by(g, license, "schema:name")) for license in licenses])
        executor.result_set_reply(f'{chapter_uuid}.{question_uuid}.{answer_uuid}.{question_uuid_2}', license_names)
    else:
        # ANSWER: No
        answer_uuid = "fbe41b6b-d976-46b6-a686-5df9023e08b4"
        executor.result_set_reply(f'{chapter_uuid}.{question_uuid}', answer_uuid)
    # ------------------------------------------------------------------------------------------------------------------
