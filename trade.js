function openForm() {
	document.getElementById("tradeform").style.display = "block";
}

function closeForm() {
	document.getElementById("tradeform").style.display = "none";
}

var symbol = document.getElementById("symbol")

/*
function getMarketPrice(symbol) {
	
	hand over symbol to python code, invoke getIndividualQuote(symbol) function in py 
	return "$" + marketPrice
	
	$.ajax({
		type: 'POST',
		url: "../../StockData Retrieve (Python)/YahooFinanceInfoRetrive.py",
		// go 2 directories up
		data: 
	})
	//
}
*/

var shares = document.getElementsByClassName("shares") 
/* declare var called shares containing info about number of shares user wants to buy/sell */

function calculateCost(marketPrice, shares) {
	cost = marketPrice * shares
	return cost /* display cost in html */
}

var symbolSearchButton = document.getElementById('symbol-search')
/*
symbolSearchButton.addEventListener('click', function() {
	getMarketPrice(symbol)
});
*/