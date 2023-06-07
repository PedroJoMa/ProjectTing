from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    class_queue = PriorityQueue()
    element1 = {"qtd_linhas": 1}
    element2 = {"qtd_linhas": 2}

    class_queue.enqueue(element1)
    class_queue.enqueue(element2)

    assert class_queue.search(0) == element1
    assert class_queue.search(1) == element2
