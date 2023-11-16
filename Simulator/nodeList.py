class NodeList():
  def __init__(self):
    self.nodes = []



  def run(self):
    for node in self.nodes:
      node.run()



  def add(self, node):
    self.nodes.append(node)
    return self.nodes[-1]

  def remove(self, node):
    self.nodes.remove(node)
    return node
