from data_extraction import get_rates_simul
from forex_graph import Graph


def display_arbitrage(arbitrage_opportunities):
  """Prints the arbitrage opportunities."""
  if len(arbitrage_opportunities) > 0:
    for opportunity, profit in arbitrage_opportunities:
      print("Arbitrage Opportunity:", " -> ".join(opportunity))
      print("Profit:", profit)
      print()
  else:
    print("No arbitrage opportunities found.")


def print_out(G: Graph):
  """Prints the graph data onto a file."""
  with open('data/rates.txt', 'w') as f:
    f.write(str(G.rates))


if __name__ == '__main__':
  """Runs the program."""

  # Setting up rates.
  currencies = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD", "MXN", "SGD", "HKD", "NOK", "KRW", "TRY", "RUB", "INR", "BRL", "ZAR"]
  rates_data = get_rates_simul(currencies)

  # Creating a graph.
  exchange_rate_graph = Graph()
  exchange_rate_graph.create_graph(rates_data)

  # Displaying the graph.
  exchange_rate_graph.show_graph()
  print_out(exchange_rate_graph)

  # Find and display arbitrage opportunities
  opportunities = exchange_rate_graph.find_arbitrage_opportunities()
  display_arbitrage(opportunities)

