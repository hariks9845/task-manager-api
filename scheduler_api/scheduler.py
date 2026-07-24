import heapq

class TaskSchedulerEngine:
    """
    Priority Queue Engine using a Min-Heap data structure.
    Tuples in heap: (priority_score, due_date_timestamp, task_id, task_object)
    """

    def __init__(self):
        self._heap = []

    def add_task(self, task):
        """Pushes a task onto the min-heap in O(log N) time."""
        timestamp = task.due_date.timestamp() if task.due_date else float('inf')
        heap_item = (task.priority, timestamp, task.id, task)
        heapq.heappush(self._heap, heap_item)

    def build_schedule(self, tasks_queryset):
        """Builds heap and extracts prioritized task sequence in O(N log N) time."""
        self._heap = []
        for task in tasks_queryset:
            self.add_task(task)

        ordered_tasks = []
        while self._heap:
            _, _, _, task = heapq.heappop(self._heap)
            ordered_tasks.append(task)

        return ordered_tasks