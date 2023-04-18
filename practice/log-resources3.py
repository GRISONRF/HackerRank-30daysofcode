""" Follow Up Question 3 -Follow Up Question 3 -
Write a function that takes the logs as input, builds the transition graph and returns it as an adjacency list with probabilities. Add START and END states.Write a function that takes the logs as input, builds the transition graph and returns it as an adjacency list with probabilities. Add START and END states.
Specifically, for each resource, we want to compute a list of every possible next step taken by any user, together with the corresponding probabilities. The list of resources should include START but not END, since by definition END is a terminal state.Specifically, for each resource, we want to compute a list of every possible next step taken by any user, together with the corresponding probabilities. The list of resources should include START but not END, since by definition END is a terminal state.
Expected output for logs1:Expected output for logs1:


transition_graph(logs1) # =>transition_graph(logs1) # =>
{{
'START': {'resource_1': 0.25, 'resource_2': 0.125, 'resource_3': 0.5, 'resource_6': 0.125},'START': {'resource_1': 0.25, 'resource_2': 0.125, 'resource_3': 0.5, 'resource_6': 0.125},
'resource_1': {'resource_6': 0.333, 'END': 0.667},'resource_1': {'resource_6': 0.333, 'END': 0.667},
'resource_2': {'END': 1.0},'resource_2': {'END': 1.0},
'resource_3': {'END': 0.4, 'resource_1': 0.2, 'resource_2': 0.2, 'resource_3': 0.2},'resource_3': {'END': 0.4, 'resource_1': 0.2, 'resource_2': 0.2, 'resource_3': 0.2},
'resource_4': {'END': 1.0},'resource_4': {'END': 1.0},
'resource_5': {'resource_4': 1.0},'resource_5': {'resource_4': 1.0},
'resource_6': {'END': 0.5, 'resource_5': 0.5}'resource_6': {'END': 0.5, 'resource_5': 0.5}
}}


For example, of 8 total users, 4 users have resource_3 as a first visit (user_1, user_2, user_3, user_5), 2 users have resource_1 as a first visit (user_6, user_22), 1 user has resource_2 as a first visit (user_7), and 1 user has resource_6 (user_8) so the possible next steps for START are resource_3 with probability 4/8, resource_1 with probability 2/8, and resource_2 and resource_6 with probability 1/8.For example, of 8 total users, 4 users have resource_3 as a first visit (user_1, user_2, user_3, user_5), 2 users have resource_1 as a first visit (user_6, user_22), 1 user has resource_2 as a first visit (user_7), and 1 user has resource_6 (user_8) so the possible next steps for START are resource_3 with probability 4/8, resource_1 with probability 2/8, and resource_2 and resource_6 with probability 1/8.
These are the resource paths per user for the first logs example, ordered by access time:These are the resource paths per user for the first logs example, ordered by access time:


{{
'user_1': ['resource_3', 'resource_3', 'resource_1'],'user_1': ['resource_3', 'resource_3', 'resource_1'],
'user_2': ['resource_3', 'resource_2'],'user_2': ['resource_3', 'resource_2'],
'user_3': ['resource_3'],'user_3': ['resource_3'],
'user_5': ['resource_3'],'user_5': ['resource_3'],
'user_6': ['resource_1', 'resource_6', 'resource_5', 'resource_4'],'user_6': ['resource_1', 'resource_6', 'resource_5', 'resource_4'],
'user_7': ['resource_2'],'user_7': ['resource_2'],
'user_8': ['resource_6'],'user_8': ['resource_6'],
'user_22': ['resource_1'],'user_22': ['resource_1'],
}}

Expected output for logs2:Expected output for logs2:
transition_graph(logs2) # =>

transition_graph(logs2) # =>
{{'START': {'resource_3': 1.0},'START': {'resource_3': 1.0},
'resource_3': {'resource_3: 0.857, 'END': 0.143}'resource_3': {'resource_3: 0.857, 'END': 0.143}
}  """