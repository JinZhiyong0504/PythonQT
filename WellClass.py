import pandas as pd

class WellClass(object):

    Wellinfo = pd.DataFrame([],columns=['WellID','WellName','GeoFormation','Xcoord_surf','Ycoord_surf','Xcoord_bot','Ycoord_bot',
                                        'CompName','SpudDate','Status','AccumProd_Oil','AccumProd_Gas','AccumProd_Wat','AccumInj_Wat','AccumInj_Gas'])
    
    WellProd_Day = pd.DataFrame([],columns=['Date','Oil_Prod','Wat_Prod','Gas_Prod','Bottom_Presure','AccumProd_Gas',
                                            'AccumProd_Oil','AccumProd_Wat','MonthlyOrDaily'])

    WellLog = pd.DataFrame([],columns=['Depth','AcousticLog','Gammar','Resistivity','Spontanous'])

    WellDev = pd.DataFrame([],columns=['Depth','','',])

    WellData_Indicator = pd.DataFrame([],columes=['Wellinf','Product','log','Dev'])

    ##WellEfficiency = pd.DataFrame([],)

    
    def InformaitonInit(self,buf):
        a=1

    def ProdInit(self,buf):
        a=1

    def WellLogInit(self,buf):
        a=1

    def WellDevInit(self,buf):
        a=1
