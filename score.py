# Define NPV and ROI for each project
npv_values = [11116.30, 66577.29, 108458.09, 54906.38]
roi_values = [9.42, 92.35, 81.46, 51.70]

# Define criteria weights
weights = {
    'NPV': 0.25,
    'ROI': 0.15,
    'Risk': 0.15,
    'Strategic Plan Alignment': 0.20,
    'Competition': 0.15,
    'Resource Availability': 0.10
}

# Define project-specific criteria values
risk_values = {'Project 1': 'Very High', 'Project 2': 'Medium', 'Project 3': 'Medium', 'Project 4': 'Low'}
alignment_values = {'Project 1': 'High', 'Project 2': 'High', 'Project 3': 'Medium', 'Project 4': 'Medium'}
competition_values = {'Project 1': 'Low', 'Project 2': 'Low', 'Project 3': 'High', 'Project 4': 'Very High'}
availability_values = {'Project 1': 'Good', 'Project 2': 'Good', 'Project 3': 'Poor', 'Project 4': 'Poor'}

# Calculate total scores for each project
total_scores = {}

for i in range(len(npv_values)):
    project = f'Project {i + 1}'
    npv_score = npv_values[i] * weights['NPV']
    roi_score = roi_values[i] * weights['ROI']
    
    # Assign scores based on criteria values
    risk_score = {'Very High': 0.15, 'High': 0.10, 'Medium': 0.05, 'Low': 0.00}[risk_values[project]]
    alignment_score = {'High': 0.10, 'Medium': 0.05, 'Low': 0.00}[alignment_values[project]]
    competition_score = {'Very High': 0.15, 'High': 0.10, 'Low': 0.05, 'Low': 0.00}[competition_values[project]]
    availability_score = {'Good': 0.10, 'Poor': 0.00}[availability_values[project]]
    
    # Calculate total score
    total_score = npv_score + roi_score + risk_score + alignment_score + competition_score + availability_score
    total_scores[project] = total_score

# Print total scores for each project
for project, score in total_scores.items():
    print(f'{project}: {score:.2f}')
