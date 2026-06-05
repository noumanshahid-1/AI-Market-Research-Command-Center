"""
async_runner.py
---------------
Runs selected agents concurrently.

Purpose:
- Improve response speed
- Execute independent agents in parallel
- Keep architecture simple and stable
"""

from concurrent.futures import ThreadPoolExecutor, as_completed


class AsyncAgentRunner:
    """
    Runs agent classes concurrently using threads.
    """

    @staticmethod
    def run(agent_plan: list, agent_map: dict, query: str) -> list:
        """
        Execute agents concurrently and return their results.
        """

        results = []

        with ThreadPoolExecutor(max_workers=4) as executor:

            future_to_agent = {}

            for agent_name in agent_plan:
                agent_class = agent_map.get(agent_name)

                if not agent_class:
                    continue

                agent_instance = agent_class(query)

                future = executor.submit(
                    agent_instance.process
                )

                future_to_agent[future] = agent_name

            for future in as_completed(future_to_agent):

                agent_name = future_to_agent[future]

                try:
                    result = future.result()
                    results.append(result)

                except Exception as error:
                    results.append(
                        {
                            "agent": agent_name,
                            "status": "error",
                            "message": str(error)
                        }
                    )

        return results