import calendar

from datetime import datetime, timedelta, date
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
		my_day = my_days.filter(date__day=day).first()

		day_string = f'{self.year}-{self.month}-{day}'
		# create day for existing days
		if day != 0 and not my_day:
			
			my_day = Day.objects.create(date=day_string)
			my_day.save()
			my_day = Day.objects.get(date=day_string)

		entry_list = ''
		for entry in entries:
			entry_list += f'<span class="badge badge-secondary m-1"> {entry.element.group} </span>'

		if day != 0:
			balance_day = int(round(my_day.balance_day.total_seconds() / 3600, 0))
			if balance_day > 0:
				balance = f'<span class="balance-pos"><i class="fas fa-caret-square-up fa-fw mr-1"></i>{balance_day}</span>'
			elif balance_day < 0:
				balance = f'<span class="balance-neg"><i class="fas fa-caret-square-down fa-fw mr-1"></i>{balance_day}</span>'
			else:
				balance = f'<span class="balance"></span>'
			

		if day != 0:
			if my_day.is_weekend:
				return f"""<td><div class="card"><a href="/entry/day/{day_string}"><div class="card-header header-small btn-blue-light">{balance}{day}</div></a>{entry_list}</ul></div></td>"""
			elif my_day.is_public_holiday:
				return f'<td><div class="card"><a href="/entry/day/{day_string}"><div class="card-header header-small btn-soft-red">{balance}{day}</div></a>{entry_list}</ul></div></td>'
			elif my_day.is_vacation:
				return f'<td><div class="card"><a href="/entry/day/{day_string}"><div class="card-header header-small btn-siemens-yellow-dark">{balance}{day}</div></a>{entry_list}</ul></div></td>'
			else:
				return f'<td><div class="card"><a href="/entry/day/{day_string}"><div class="card-header header-small btn-light">{balance}{day}</div></a>{entry_list}</ul></div></td>'

		return '<td></td>'


	def formatweek(self, theweek, entries, my_days):
		'''format days into weeks'''
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, entries, my_days)
		return f'<tr> {week} </tr>'

	def formatweekview(self, withyear=True):
		'''format header and add single week'''
		entries = Entry.objects.filter(date__date__year=self.year, date__date__month=self.month)
		my_days = Day.objects.filter(date__date__year=self.year, date__date__month=self.month)

		cal = f'<table class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'

	def formatmonthview(self, withyear=True):
		'''format header and adds weeks as rows'''
		entries = Entry.objects.filter(date__date__year=self.year, date__date__month=self.month)
		my_days = Day.objects.filter(date__year=self.year, date__month=self.month)

		cal = f'<table class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, entries, my_days)}\n'
		return cal

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
