#Network should predict if a student will pass
#Based on Intelligence, Hours, Difficulty, Grade
#Nodes [1,0] 
#Intelligence  high or low
#Hours Sufficient Insufficient
#Grade A B C
#Pass Yes No Anything below a C will be fail

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 1: Define the structure
model = DiscreteBayesianNetwork([
    ('Intelligence', 'Grade'),
    ('StudyHours', 'Grade'),
    ('Difficulty', 'Grade'),
    ('Grade', 'Pass')
])

# Step 2: Define CPDs

# Intelligence
cpd_intelligence = TabularCPD('Intelligence', 2, [[0.7], [0.3]])  # 0: High, 1: Low

# Study Hours
cpd_study = TabularCPD('StudyHours', 2, [[0.6], [0.4]])  # 0: Sufficient, 1: Insufficient

# Difficulty
cpd_difficulty = TabularCPD('Difficulty', 2, [[0.4], [0.6]])  # 0: Hard, 1: Easy

# Grade | Intelligence, StudyHours, Difficulty
# Format: Grade = A (0), B (1), C (2)
cpd_grade = TabularCPD(
    'Grade', 3,
    [
        [0.9, 0.6, 0.4, 0.8, 0.5, 0.3, 0.7, 0.4],  # A
        [0.08, 0.3, 0.4, 0.15, 0.3, 0.4, 0.2, 0.4],  # B
        [0.02, 0.1, 0.2, 0.05, 0.2, 0.3, 0.1, 0.2],  # C
    ],
    evidence=['Intelligence', 'StudyHours', 'Difficulty'],
    evidence_card=[2, 2, 2]
)

# Pass | Grade
cpd_pass = TabularCPD(
    'Pass', 2,
    [
        [0.05, 0.2, 0.5],  # No
        [0.95, 0.8, 0.5],  # Yes
    ],
    evidence=['Grade'],
    evidence_card=[3]
)

# Step 3: Add CPDs
model.add_cpds(cpd_intelligence, cpd_study, cpd_difficulty, cpd_grade, cpd_pass)

# Step 4: Validate
assert model.check_model(), "Something's wrong in the model!"

# Step 5: Inference
inference = VariableElimination(model)

# Query 1: P(Pass | StudyHours = Sufficient, Difficulty = Hard)
result1 = inference.query(variables=['Pass'], evidence={'StudyHours': 0, 'Difficulty': 0})
print("\nP(Pass | StudyHours=Sufficient, Difficulty=Hard):")
print(result1)

# Query 2: P(Intelligence = High | Pass = Yes)
result2 = inference.query(variables=['Intelligence'], evidence={'Pass': 1})
print("\nP(Intelligence | Pass=Yes):")
print(result2)
