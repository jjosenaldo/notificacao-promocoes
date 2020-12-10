import dash_core_components as dcc
import dash_html_components as html

CATEGORIAS = ['limpeza', 'vestuário', 'eletrodomésticos', 'cama, mesa e banho', 'açougue']

def getDropdown(id='dropdown-categorias', categorias=CATEGORIAS):
	options = []
	for categoria in categorias:
		options.append(html.Option(label=categoria, value=categoria))
	return html.Select(
		children=options,
		id=id
	)