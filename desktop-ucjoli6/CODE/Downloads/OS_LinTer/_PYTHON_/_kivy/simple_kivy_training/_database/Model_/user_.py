
class User:

  def __init__(self, lastName:str='', firstName:str='',
               age:int = 1, birthDate:str = "dd/MM/yyyy", birthPlace:str='',
               residencePlace:str='', job_:str='', height_:float=1.0, weigth_:float=21.0,
               morphology_:list[str]=[], defauts:list[str]=[], isTerrian_:bool=True,
              ):
    # Nomination
    # self.userID = userID
    self.lastName = lastName
    self.firstName = firstName
    # Temporalz Attributes
    self.age = age
    self.birthDate = birthDate
    self.birthPlace = birthPlace
    self.residencePlace = residencePlace
    self.job_ = job_  # Financialz Attributes
    # Morphologycalz Attributes
    self.height_ = height_
    self.weigth_ = weigth_
    self.morphology_ = morphology_
    self.defects = defauts
    self.isTerrian_ = isTerrian_  # else
  
  def isTerrian(self, ):
    return self.isTerrian_


if __name__ == "__main__":
  user_ = User()

