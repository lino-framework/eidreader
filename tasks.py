from atelier.invlib import setup_from_tasks

ns = setup_from_tasks(
    globals(),
    blogref_url="https://luc.lino-framework.org",
    revision_control_system='git',
    # tolerate_sphinx_warnings=True,
    doc_trees=['docs'],
    intersphinx_urls=dict(docs="https://eidreader.lino-framework.org"))

# srcref_url='https://github.com/lino-framework/eidreader/blob/master/%s'
