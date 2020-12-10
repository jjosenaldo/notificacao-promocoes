import dash_html_components as html

def createNotification(title, price, description):
	h1_title = html.H1(children=title, title=title)
	h2_price = html.H2(children='R$ '+str(price), className='price')
	h2_descr = html.H2(children='Descrição')
	p_descr = html.P(children=description, title=description)
	return html.Li(children=[h1_title,h2_price,h2_descr,p_descr])