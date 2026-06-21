from crewai.flow.flow import Flow, start, listen, router


class StockAnalysisFlow(Flow):
    @start()
    def analyse_stock(self):
        self.state["stock"] = "APPL"
        self.state["summary"] = "Apple has demonstrated consistent revenue and earnings growth over the past several years"
        # LLM Call

        return self.state["summary"]
    
    @listen(analyse_stock)
    def advise_action(self, summary):
        self.state["recommendation"] = "SELL" # LLM Call
        
        return self.state["recommendation"]
    

    @router(advise_action)
    def take_action(self, recommendation):
        if recommendation == "BUY":
            return "buy_stock"
        
        if recommendation == "SELL":
            return "sell_stock"
        
        if recommendation == "HOLD":
            return "hold_stock"
        
    @listen("buy_stock")
    def buy_stock_action(self):
        # call API to buy stock
        print(f"BUY - {self.state['stock']}")
        self.state["transaction"] = {
            "ID": 1,
            "QTY": 10,
            "TOTAL": 1000
        }

        return "DONE"

    @listen("sell_stock")
    def sell_stock_action(self):
        # call API to sell stock
        print(f"SELL - {self.state['stock']}")

        self.state["transaction"] = {
            "ID": 1,
            "QTY": 10,
            "TOTAL": 1000
        }

        return "DONE"

    @listen("hold_stock")
    def hold_stock_action(self):
        # call API to HOLD stock
        print(f"HOLD - {self.state['stock']}")

        return "DONE"


flow = StockAnalysisFlow()
result = flow.kickoff()

print(result)
print(flow.state)


