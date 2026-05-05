class TextEditor:
    def __init__(self):
        self.text = ""
        self.stacks = []

    def write(self, new_text):
        self.stacks.append(self.text)
        self.text = self.text + new_text

    def undo(self):
        self.text = self.stacks.pop()

    def get_text(self):
        return self.text
    
editor = TextEditor()

editor.write("Hello")
editor.write(" World")

print(editor.get_text())   # Hello World

editor.undo()
print(editor.get_text())   # Hello

editor.undo()
print(editor.get_text())   # (empty string)