import json

from rdflib import URIRef, Literal, Graph, BNode


def create_rdf_graph(content: str, content_type: str) -> Graph:
    context = {
        "@context": {
            "schema": "https://schema.org/",
        }
    }
    rdf_format = None
    if content_type == "application/ld+json":
        rdf_format = 'json-ld'
    else:
        rdf_format = 'json-ld'

    g = Graph()
    g.parse(data=content, format=rdf_format, context=context)
    return g


def get_root_subject(content: str) -> str:
    json_data = json.loads(content)
    return json_data.get("@id", json_data.get("id", None))


def build_term(g, uri):
    if uri is not None:
        # Blank Node
        if isinstance(uri, BNode):
            return uri

        # URI: ':name'
        if uri.startswith(":"):
            return URIRef(g.namespace_manager.store.namespace('') + uri[1:])

        # URI: 'schema:name'
        splitted = uri.split(":")
        if len(splitted) == 2 and splitted[1][0] != "/":
            return URIRef(g.namespace_manager.store.namespace(splitted[0]) + splitted[1])

        # URI: 'http://schema.org/person#name'
        if "://" in uri:
            return URIRef(uri)

        # Literal
        return Literal(uri)


def shorten_uri(g, uri):
    return uri


def get_subjects_by(g, predicate, object):
    return g.subjects(build_term(g, predicate), build_term(g, object))


def get_objects_by(g, subject, predicate):
    return g.objects(build_term(g, subject), build_term(g, predicate))


def get_sparql(g, query, init_bindings):
    return list(g.query(query, initBindings=init_bindings))


def get_subject_by(g, predicate, object):
    return next(get_subjects_by(g, predicate, object), None)


def get_object_by(g, subject, predicate):
    return next(get_objects_by(g, subject, predicate), None)


def get_sparql_one(g, query):
    return list(g.query(query))[0]
