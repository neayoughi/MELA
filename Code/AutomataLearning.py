import ast
from aalpy.learning_algs import run_RPNI


# Load your trace data from a file
def load_traces_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read the entire file content
        file_content = file.read()
        # Convert the string representation to a list of tuples
        traces = ast.literal_eval(file_content)
        return traces

# Path to your trace file
trace_file_path = 'Trace_DDoS.txt'

# Load the traces
traces = load_traces_from_file(trace_file_path)

# Run RPNI algorithm
learned_model = run_RPNI(traces, automaton_type='moore', input_completeness=None, print_info=True)
# learned_model = run_RPNI(traces, automaton_type='moore', print_info=True)
# learned_model.make_input_complete('sink_state')
print(learned_model.is_input_complete())
print(learned_model.get_input_alphabet())


# save or print the learned model
print(learned_model)
learned_model.visualize(file_type='dot', path='LearnedModel_DDoS.dot')
learned_model.visualize(file_type='pdf', path='LearnedModel_DDoS.pdf')
learned_model.save()
