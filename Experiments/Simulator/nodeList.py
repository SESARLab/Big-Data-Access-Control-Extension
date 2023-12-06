class NodeList:
    def __init__(self, description=""):
        self.nodes = []
        self.description = description

    def run(self, data, data_logger=None):
        for node in self.nodes:
            node.run(data)
            service = node.getOneService()
            data = service.get_result()
            data_logger.log(nodelist=self.description, service=service)
            #print(f"\t\t{len(data)}")

    def add(self, node):
        self.nodes.append(node)
        return self.nodes[-1]

    def remove(self, node):
        self.nodes.remove(node)
        return node

    def __repr__(self) -> str:
        return "NodeList:\n{}".format(self.nodes)
