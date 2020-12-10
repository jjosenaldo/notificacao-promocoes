import dash_core_components as dcc
import dash_html_components as html

CATEGORIAS = ['limpeza', 'vestuário', 'eletrodomésticos', 'cama, mesa e banho', 'açougue']

def getDropdown(id='dropdown-categorias', categorias=CATEGORIAS):
	options = []
	for categoria in categorias:
		options.append({'label':categoria, 'value':categoria})
	return [dcc.Dropdown(
	        id=id,
	        options=options,
	        value=''
	    ), 
		html.Div(id='hidden-dropdown-div', style={'display':'none'})]