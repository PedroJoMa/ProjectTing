from ting_file_management.priority_queue import PriorityQueue
# import pytest


def test_basic_priority_queueing():
    class_queue = PriorityQueue()
    element1 = {"qtd_linhas": 3}
    element2 = {"qtd_linhas": 7}
    element3 = {"qtd_linhas": 2}
    length_high_priority = 2
    length_regular_priority = 1
    class_queue.enqueue(element3)
    class_queue.enqueue(element2)
    class_queue.enqueue(element1)

    assert len(class_queue) == length_high_priority + length_regular_priority

    element_removed = class_queue.dequeue()
    assert element_removed == element3

    search_element1 = class_queue.search(0)
    search_element2 = class_queue.search(1)

    assert search_element1 == element1
    assert search_element2 == element2
