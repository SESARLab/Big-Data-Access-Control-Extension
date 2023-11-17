class Service():
  def __init__(self,policy,data):
    self.policy = policy
    self.data = data

  def run(self):
    print("Service {} running".format(self.data))

