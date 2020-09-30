def test_import_dags(dag_bag):
    assert len(dag_bag.import_errors) == 0
    assert dag_bag.size() == 1


def test_valid_dags(dag_bag):
    for dag in dag_bag.dags.values():
        assert len(dag.tasks) > 0
