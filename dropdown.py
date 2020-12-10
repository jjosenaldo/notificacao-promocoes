import dash_core_components as dcc

CATEGORIAS = ['limpeza', 'vestuário', 'eletrodomésticos', 'cama, mesa e banho', 'açougue']

def getDropdown(id='dropdown-categorias', categorias=CATEGORIAS):
	options = []

	for categoria in categorias:
		options.append({'label':categoria,'value':categoria})

	return dcc.Dropdown(
        id=id,
        options=options,
        value=categorias[0]
    )