class NodeLinkList:
    def __init__(self, value:int | float | str, next = None):
        self.value = value
        self.next = next
        self.previous = None
    def __repr__(self):
        return f"{self.value}->{self.next}"


class LinkList:
  def __init__(self, value = None):
  


  def check_type(self,value):
    if isinstance(value, (int,float,str):
        pass
    elif isinstance(value,(iterable)):


