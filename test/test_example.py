from dags.example import add, subtract


class TestExampleDAG:
    def test_add(self, caplog):
        add()
        print(caplog.records)
        assert "2 + 2 = 4" in caplog.text

    def test_subtract(self, caplog):
        subtract()
        assert "2 - 2 = 0" in caplog.text

    def test_task_dependencies(self, dag_bag):
        dag = dag_bag.dags["example"]

        add_task = dag.get_task("add")
        assert add_task.upstream_task_ids == set()
        assert add_task.downstream_task_ids == set(["subtract"])

        subtract_task = dag.get_task("subtract")
        assert subtract_task.upstream_task_ids == set(["add"])
        assert subtract_task.downstream_task_ids == set()
