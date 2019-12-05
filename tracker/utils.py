from datetime import datetime, timedelta
from calendar import HTMLCalendar

from tracker.models import Entry, Day


class Calendar(HTMLCalendar):
	

	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	def formatday(self, day, entries, my_days):
		'''format day brackets'''
		entries = entries.filter(date__date__day=day)
		my_day = my_days.filter(date__day=day)
		entry_list = ''
		for entry in entries:
			entry_list += f'<li class="list-group-item card-list-small"> {entry.element.group} </li>'

		if day != 0:
			return f'<td><div class="card"><div class="card-header header-small">{day}</div><ul class="list-group list-group-flush">{entry_list}</ul></div></td>'
		return '<td></td>'


	def formatweek(self, theweek, entries, my_days):
		'''format days into weeks'''
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, entries, my_days)
		return f'<tr> {week} </tr>'


	def formatmonth(self, withyear=True):
		'''format header and adds weeks as rows'''
		entries = Entry.objects.filter(date__date__year=self.year, date__date__month=self.month)
		my_days = Day.objects.filter(date__year=self.year, date__month=self.month)

		cal = f'<table class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, entries, my_days)}\n'
		return cal