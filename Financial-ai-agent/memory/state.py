class AgentState:
    def __init__(self, user_query):
        self.user_query = user_query
        self.plan = []
        self.tool_outputs = {}
        self.final_insight = None
