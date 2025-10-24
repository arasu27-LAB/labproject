from datetime import date
class Date:
    def calculate_age(self,dtob):
        today = date.today()
        return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))
d=Date()
print(d.calculate_age(date(2006,5,30)))
print(d.calculate_age(date(1989,1,12)))

