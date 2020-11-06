import itertools
class Jugada():
  """docstring for ClassName"""
  def __init__(self,live,plf,jlf):
    
    self.jigglypuff_vida =int(live)
    self.pikachu_vida = int(live)
    self.turno=1
    self.pikachuPower= int(plf)
    self.jigglypuffPower= int(jlf)
  #funcion k valora los turnos de cada pokemon restando al la vida el poder de cada pokemos contrario
  
  def vs(self):
    pikachu_vida=self.pikachu_vida
    jigglypuff_vida=self.jigglypuff_vida
    while pikachu_vida>0 and jigglypuff_vida>0:
      
      if self.turno==0:
        jigglypuff_vida=jigglypuff_vida-self.pikachuPower

        self.turno=1
      else:
        pikachu_vida=pikachu_vida-self.jigglypuffPower
        self.turno=0
    if pikachu_vida<=0:
      win="jigglypuff"
    else:
      win="pikachu"
      
      
    vida_p=pikachu_vida
    vida_j=jigglypuff_vida
    return(win,vida_p,vida_j)
