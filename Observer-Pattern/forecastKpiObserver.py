from absobserver import AbsObserver


class ForecastKPIs(AbsObserver):
    open_tickets = -1 
    closed_tickets = -1
    new_tickets = -1
 
    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)
 
    def update(self):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets
        self.display()
 
    def display(self):
        print('Forecast open tickets: {}'.format(self.open_tickets))
        print('New Tickets expected in next hour: {}'.format(self.new_tickets))
        print('Tickets expected to be closed in next hour: {}'.format(self.closed_tickets))
        print("\n**************************************************")
