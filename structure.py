class NodeLinkList:
    def __init__(self, value:int | float | str, next = None):
        self.value = value
        self.next = next
        self.previous = None
    def __repr__(self):
        return f"{self.value}->{self.next}"


class LinkList:
    
    def __init__(self, value = None):
        if value is None:
            pass
        else:
            self.data = self.last = NodeListLink(value)
    
    def append(self, value):      
        if hasattr(self,'data'):
            self.last.next = NodeLinkList(value)
            self.last.previous = self.last
            self.last = self.last.next
        else:
            self.data = self.last  = NodeListLink(value)
    
    def get(self):
        return self.last.value

    def reverse(self):
        if self.data:
            self._reverse(self.data.next)
            self.new_data = self.new_last = NodeListLink(self.data.value)
            
    def _reverse(self,node):
        if node:
            self._reverse(node.next)
            self.new_last.next = NodeListLink(node.value)
            self.new_Last = self.new_last.next
        else:
            self.new_data = self.new_last = NodeListLink(self.data.value)
