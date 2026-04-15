import calendar
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # Split and convert to integers
        syear, smonth, sday = map(int, date1.split("-"))
        eyear, emonth, eday = map(int, date2.split("-"))

        # Dictionaries
        leap_year_days = {
            1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        non_leap_year_days = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }

        # Helper: convert a date to "days since year 0"
        def days_from_start(year, month, day):
            # Count full years
            days = 0
            for y in range(year):
                days += 366 if calendar.isleap(y) else 365
            
            # Count full months in current year
            if calendar.isleap(year):
                mdays = leap_year_days
            else:
                mdays = non_leap_year_days
            
            for m in range(1, month):
                days += mdays[m]
            
            # Add days in current month
            days += day
            return days

        # Convert both dates to absolute day counts
        d1 = days_from_start(syear, smonth, sday)
        d2 = days_from_start(eyear, emonth, eday) 
        return abs(d1-d2)
