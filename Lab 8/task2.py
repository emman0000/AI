# Import necessary libraries
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 1: Define the structure of the Bayesian Network
model = DiscreteBayesianNetwork([
    ('Burglary', 'Alarm'),
    ('Earthquake', 'Alarm'),
    ('Alarm', 'JohnCalls'),
    ('Alarm', 'MaryCalls')
])

# Step 2: Define the Conditional Probability Distributions (CPDs)

# P(Burglary)
cpd_burglary = TabularCPD(variable='Burglary', variable_card=2,
                          values=[[0.999], [0.001]])

# P(Earthquake)
cpd_earthquake = TabularCPD(variable='Earthquake', variable_card=2,
                            values=[[0.998], [0.002]])

# P(Alarm | Burglary, Earthquake)
cpd_alarm = TabularCPD(variable='Alarm', variable_card=2,
                       values=[[0.999, 0.71, 0.06, 0.05],  # Alarm = False
                               [0.001, 0.29, 0.94, 0.95]],  # Alarm = True
                       evidence=['Burglary', 'Earthquake'],
                       evidence_card=[2, 2])

# P(JohnCalls | Alarm)
cpd_john = TabularCPD(variable='JohnCalls', variable_card=2,
                      values=[[0.3, 0.9],  # JohnCalls = False
                              [0.7, 0.1]],  # JohnCalls = True
                      evidence=['Alarm'],
                      evidence_card=[2])

# P(MaryCalls | Alarm)
cpd_mary = TabularCPD(variable='MaryCalls', variable_card=2,
                      values=[[0.2, 0.99],  # MaryCalls = False
                              [0.8, 0.01]],  # MaryCalls = True
                      evidence=['Alarm'],
                      evidence_card=[2])

# Step 3: Add CPDs to the model
model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_john, cpd_mary)

# Step 4: Validate the model
assert model.check_model(), "Model is incorrect"

# Step 5: Perform inference
inference = VariableElimination(model)

# Example Query 1: What is the probability of a Burglary given John and Mary both called?
result1 = inference.query(variables=['Burglary'], evidence={'JohnCalls': 1, 'MaryCalls': 1})
print("P(Burglary | JohnCalls = Yes, MaryCalls = Yes):")
print(result1)

# Example Query 2: What is the probability of Alarm being True?
result2 = inference.query(variables=['Alarm'])
print("\nP(Alarm):")
print(result2)

# Example Query 3: What is the probability of Earthquake given Alarm = True?
result3 = inference.query(variables=['Earthquake'], evidence={'Alarm': 1})
print("\nP(Earthquake | Alarm = Yes):")
print(result3)
