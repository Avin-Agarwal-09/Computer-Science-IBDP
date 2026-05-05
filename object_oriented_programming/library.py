class LibraryItem:
    def __init__(self,title,itemID,author,runTime):
        self.title = title
        self.itemID = itemID
        self.author = author
        self.runTime = runTime

    def get_title(self):
        return self.title
    
class Book(LibraryItem):
    def __init__(self,title,itemID,author,runTime,pages):
        super().__init__(title,itemID,author,runTime)
        self.pages = pages
    
    def set_author(self,new_author):
        self.author = new_author