from agent.planner import create_plan
from agent.executor import execute_tools
from agent.reasoner import analyze_market
from memory.state import AgentState
from agent.trade_logic import trade_recommendation


def run_agent(user_query):
    state = AgentState(user_query)

    # Plan
    state.plan = create_plan(user_query)

    # Execute tools
    state.tool_outputs = execute_tools(state.plan)

    # Reason
    insights = {}
    for market, content in state.tool_outputs.items():
        analysis = analyze_market(content["data"])
        trade = trade_recommendation(analysis)

        insights[market] = {
            **analysis,
            **trade
        }

    state.final_insight = insights
    return state
