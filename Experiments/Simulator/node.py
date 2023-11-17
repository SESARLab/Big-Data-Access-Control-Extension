class Node (object):
  def __init__(self, policy):
      self.policy = policy
      self.services = []

  def match(self, service):
    for key in self.policy:
      if key in service.policy:
        if service.policy[key] == self.policy[key]:
          self.services.append(service)
          return True
      else:
        return False

