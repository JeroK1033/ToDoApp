class Todo:
    def __init__(self, code_id, title, description):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: (list[str]) = []
    
    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        self.tags.append(tag)

    def __str__(self) -> str:
        return f"{self.code_id} - {self.title}"

class TodoBook:
    def __init__(self):
        self.todos: int = {}
    
    def add_todo(self, title: str, description:str) -> int:
        id = len(self.todos) + 1
        new_todo = Todo(code_id=id, title=title, description=description)
        self.todos[id] = new_todo
        return id
    
    def pending_todos(self)->list[Todo]:
        return [todo for todo in self.todos.values() if not todo.completed]
    
    def completed_todos(self)->list[Todo]:
        return [todo for todo in self.todos.values() if todo.completed]
    
    def tags_todo_count(self)-> dict[str,int]:
        tag_count = {}
        for todo in self.todos.values():
            for tag in todo.tags:
                if tag in tag_count:
                    tag_count[tag] += 1
                else:
                    tag_count[tag] = 1
        return tag_count
    