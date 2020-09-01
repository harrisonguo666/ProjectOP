const	Alpaca = require('@alpacahq/alpaca-trade-api')
const alpaca = new Alpaca()

// submit a market order to buy 1 share of Apple at market price
alpaca.createOrder({ // let user define these properties -- pull from html form submit
	symbo: 'AAPL',
	qty: 1,
	side: 'buy',
	type: 'market',
	time_in_force: 'gtc' //good til cancelled
})

// get a list of existing orders
const closedOrders = alpaca.getOrders({
	stats: 'closed',
	limit: 100,
	nested: true // show nested multi-leg orders(?)
}).then((closedOrders) => {
	// get only closed orders for a particular stock
	const closedAaplOrders = closedOrders.filter(order => order.symbol =='AAPl')
	console.log(closedAaplOrders)
})
