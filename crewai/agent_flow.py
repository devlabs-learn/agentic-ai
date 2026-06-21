from crewai.flow.flow import Flow, start, listen, router
from crewai import Agent, Task, Crew

from typing import Any, Optional
from pydantic import BaseModel

class StockTradingState(BaseModel):
    stock: Optional[str] = "APPL"
    summary: Optional[str] = None
    advise: Optional[str] = None
    transaction: Any = None


class StockAnalysisFlow(Flow[StockTradingState]):
    @start()
    def analyse_stock(self):
        agent = Agent(
            role = "Stock Trading Analyst",
            goal = "Analyse the stock - {stock} and return a summary of your analysis",
            backstory = "You are an expert stock analyst, good at anlysing stock fundamentals, technical analysis and market sentiment"
        )

        task = Task(
            description="Analyse stock {stock}",
            expected_output="Summarize your analysis and return a list of important points",
            agent=agent
        )

        crew = Crew(agents=[agent], tasks=[task])
        result = crew.kickoff(inputs={"stock": self.state.stock })

        # Store result from agent as summary
        self.state.summary = result.raw

        return result.raw

    
    @listen(analyse_stock)
    def advise_action(self, summary):
        agent = Agent(
            role = "Stock Adviser",
            goal = "Advise based on research summary to BUY, SELL or HOLD",
            backstory = "You are a stock adviser good at providing recommendations on taking market actions BUY, SELL, HOLD"
        )

        task = Task(
            description="Provide recommendation to BUY, SELL or HOLD based on stock analysis summary: {summary}",
            expected_output="Return only SELL, BUY or HOLD",
            agent=agent
        )

        crew = Crew(agents=[agent], tasks=[task])
        result = crew.kickoff(inputs={"summary": summary })

        # Store result from agent as advise
        self.state.advise = result.raw
        
        return result.raw
    

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
        print(f"BUY - {self.state.stock}")

        self.state.transaction = {
            "ID": 1,
            "QTY": 10,
            "TOTAL": 1000
        }

        return "DONE"

    @listen("sell_stock")
    def sell_stock_action(self):
        # call API to sell stock
        print(f"SELL - {self.state.stock}")
        
        self.state.transaction = {
            "ID": 1,
            "QTY": 10,
            "TOTAL": 1000
        }

        return "DONE"

    @listen("hold_stock")
    def hold_stock_action(self):
        # call API to HOLD stock
        print(f"HOLD - {self.state.stock}")

        return "DONE"


flow = StockAnalysisFlow(state = StockTradingState(stock="APPL"))
# flow.plot()

result = flow.kickoff()

print(result)
print(flow.state)


