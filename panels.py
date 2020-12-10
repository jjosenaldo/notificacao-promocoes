import dash_html_components as html
import dash_core_components as dcc
from dropdown import getDropdown
from map import getMap
from notifications import createNotification

def createLeftPanel():
	return html.Div(children=getMap(), id='left')

def createRightTopPanel():
	title = html.H2(children='Escolha uma categoria:')
	dropdown = getDropdown()
	# This * is needed because the dropdown consists of two components
	# (the dropdown itself and a invisible div)
	return html.Div(children=[title,*dropdown], id='right-top')

def createRightCenterPanel(idNotifications='notifications'):
	hr_1 = html.Hr()
	h1 = html.H1(children='Notificações')
	hr_2 = html.Hr()
	ul = html.Ul(children=[], id=idNotifications)
	return html.Div(children=[hr_1,h1,hr_2,ul], id='right-center')

def createRightPanel():
	return html.Div(children=[createRightTopPanel(),createRightCenterPanel()], id='right')

def createMainPanel():
	left = createLeftPanel()
	right = createRightPanel()
	interval = dcc.Interval(
		id='interval-component',
		interval=1*1000, # in milliseconds
		n_intervals=0
	)
	return html.Div(children=[left,right,interval], id='main')