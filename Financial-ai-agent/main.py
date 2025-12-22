from agent.agent import run_agent

if __name__ == "__main__":
    query = "Analyze Indian markets outlook for next 7 days"
    agent_state = run_agent(query)

    print("\n🧠 FINANCIAL AI AGENT OUTPUT\n")
    for market, insight in agent_state.final_insight.items():
        print(f"📈 {market}")
        for k, v in insight.items():
            print(f"  {k}: {v}")
        print()
