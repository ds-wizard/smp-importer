from smp_importer.mapping.chapter_1 import process_chapter_1
from smp_importer.mapping.chapter_6 import process_chapter_6
from smp_importer.mapping.chapter_7 import process_chapter_7

from smp_importer.model import MappingExecutor
from smp_importer.rdf_helper import create_rdf_graph, get_root_subject


def process(content: str, content_type: str) -> dict:
    root_subject = get_root_subject(content)
    g = create_rdf_graph(content, content_type)
    executor = MappingExecutor()

    process_chapter_1(g, executor, root_subject)
    process_chapter_6(g, executor, root_subject)
    process_chapter_7(g, executor, root_subject)

    g.close()
    return executor.get_result_dict()
