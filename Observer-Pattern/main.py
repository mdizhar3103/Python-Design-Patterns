from currentKpiObserver import CurrentKPIs
from forecastKpiObserver import ForecastKPIs
from kpisubject import KPIs


kpis = KPIs()
currentKPIs = CurrentKPIs(kpis)
forecastKPIs = ForecastKPIs(kpis)
kpis.set_kpis(25, 10, 5)
kpis.set_kpis(100, 50, 30)
kpis.set_kpis(50, 10, 20)
 
print("\n Detaching the current KPIS observer \n\n")
kpis.detach(currentKPIs)
kpis.set_kpis(150, 110, 120)