import math


def is_zero(val):
  return abs(val) < 0.01


class Graph:
  def __init__(self):
    """Initializes a Graph object."""
    self.rates = dict()

  def create_graph(self, rates):
    """Creates the graph from exchange rates."""
    for base, exchange_rates in rates.items():
      self.rates[base] = exchange_rates

  def update_graph(self, new_rates):
    """Update the exchange rates if differences arise."""
    for base, exchange_rates in new_rates.items():
      if base in self.rates:
        self.rates[base].update(exchange_rates)
      else:
        self.rates[base] = exchange_rates

  def display_exchange_rate(self, from_currency, to_currency):
    """Displays the current exchange rate."""
    if from_currency in self.rates and to_currency in self.rates[from_currency]:
      return self.rates[from_currency][to_currency]
    else:
      return None

  def show_graph(self):
    """Prints the entire graph."""
    for source_currency in self.rates.keys():
      print(f"Exchange rates from {source_currency}:")
      for target_currency, exchange_rate in self.rates[source_currency].items():
        print(f"{source_currency} to {target_currency}: {exchange_rate}")
    print()

  def find_arbitrage_opportunities(self):
    """Finds the price differences through cycles."""
    arbitrage_opportunities = []
    for source in self.rates:
      distance = {node: float('inf') for node in self.rates}
      previous_nodes = {node: None for node in self.rates}
      distance[source] = 0
      for _ in range(len(self.rates) - 1):
        for base, exchange_rates in self.rates.items():
          for target, rate in exchange_rates.items():
            if distance[base] + -math.log(rate) < distance[target]:
              distance[target] = distance[base] + -math.log(rate)
              previous_nodes[target] = base
      for base, exchange_rates in self.rates.items():
        for target, rate in exchange_rates.items():
          if distance[base] + -math.log(rate) < distance[target]:
            arbitrage_path = [target]
            while True:
              target = previous_nodes[target]
              if target not in arbitrage_path:
                arbitrage_path.append(target)
              else:
                arbitrage_path.append(target)
                arbitrage_path = arbitrage_path[arbitrage_path.index(target):]
                break
            arbitrage_path = arbitrage_path[::-1]
            profit = 1
            for i in range(len(arbitrage_path) - 1):
              profit *= self.rates[arbitrage_path[i]][arbitrage_path[i+1]]
            if not is_zero(profit-1):
              arbitrage_opportunities.append((arbitrage_path, profit))
    return arbitrage_opportunities

