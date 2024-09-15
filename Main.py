from Model import llm
from GraphState import state
from langgraph.graph import StateGraph, END
from Prompts import (generate_initial_code, performance_analysis, optimize,
                     rating, performance_comparison, determination)
from langchain_core.prompts import ChatPromptTemplate

workflow = StateGraph(state)

#defining the nodes
def analyzer(state):
    history = state.get('history').strip()
    code = state.get('code').strip()
    iterations = state.get('iterations')

    print("Analyzer working...")

    performance = llm(performance_analysis.format(code))

    return {'history': history + "\nANALYZER:\n" + performance, 'performance': performance,
            'iterations': iterations + 1}


def optimizer(state):
    history = state.get('history').strip()
    code = state.get('code').strip()

    print("Optimizing...")
    optimizations = llm(optimize.format(code))
    print(optimizations)

    return {'history': history + "\nOPTIMIZATIONS:\n" + optimizations, 'optimizations': optimizations}


def result(state):
    print("Optimization Done!\n")

    code1 = state.get('actual_code').strip()
    code2 = state.get('code').strip()
    performance_compare = llm(performance_comparison.format(code1, code2))
    print(performance_compare)

    return {'rating': rating, 'performance_compare': performance_compare}


#Adding the Nodes
workflow.add_node("analyzer", analyzer)
workflow.add_node("optimizer", optimizer)
workflow.add_node("result", result)

def optimization_done(state):
    max_iterations = 1 if state.get('iterations') > 2 else 0
    optimized = 1 if 'TRUE' in llm(determination.format(state.get('code'))) else 0
    return "result" if max_iterations or optimized else "optimizer"


workflow.set_entry_point("analyzer")
workflow.add_edge('optimizer', "analyzer")
workflow.add_edge('result', END)

workflow.add_conditional_edges(
    "analyzer",
    optimization_done,
    {
        "result": "result",
        "optimizer": "optimizer"
    }
)


def main():
    # problem = input("Please enter the question: ")
    problem = "Write a function to find the largest subarray sum from a given array. Don't give the driver code."
    code = llm(generate_initial_code.format(problem))
    print("Actual Code: \n" + code + '\n')
    app = workflow.compile()
    app.invoke({'history': code, 'code': code, 'actual_code': code, 'iterations': 0})
    print(app.get_graph().draw_mermaid())

if __name__ == '__main__':
    main()
