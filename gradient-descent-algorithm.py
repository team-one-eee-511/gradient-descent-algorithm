
class RegressionSolver:
  def __init__(self):
    self.alpha = 1

  # set the the learning rate
  def set_alpha(self, alpha):
    self.alpha = alpha
    
  # dataset must be an array of (x,y) tuples, with length m
  def set_data(self, dataset):
    # validate argument
    assert isinstance(dataset, (tuple, list)), "Invalid type: data must be an array"
    assert len(dataset) > 0, "Invalid param: data must have a non-zero length"
    assert isinstance(dataset[0], (tuple, list)), "Invalid param: data must be an array of (x,y) tuples"
    assert len(dataset[0]) == 2, "Invalid param: data must be an array of (x,y) tuples"

    self.dataset = dataset
    self.m = len(dataset)

  def solve(self):
    theta0 = 0
    delta0 = -1
    theta1 = 1
    delta1 = -1

    while delta-


    mylist = [self.func(x) for x in range(self.m)]
    return mylist

  # calculate  h(x) = theta0 + theta1*x
  def hx(self, x, theta0, theta1):
    return theta0 + theta1 * x

  # get ith x value in dataset
  def __xi(self, i):
    return dataset[i][0]

  # get ith y value in dataset
  def __yi(self, i):
    return dataset[i][1]

  # calculate delta term to change theta0
  def __theta0_delta(self, theta0, theta1):
    sum_term = 0

    for i in range(self.m):
      sum_term += self.__hx(self.__xi(i)) - self.__yi(i)

    return self.alpha * 1/m * sum_term

  # calculate delta term to change theta0
  def __theta1_delta(self, theta0, theta1):
    sum_term = 0

    for i in range(self.m):
      x = self.__xi(i)
      sum_term += ( self.__hx(self.__xi(i)) - self.__yi(i) ) * self.__xi()

    return self.alpha * 1/m * sum_term


  