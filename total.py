# Define NPV and ROI for each project (values from 1 to 10)
npv_values = {'Project 1': 3, 'Project 2': 8, 'Project 3': 10, 'Project 4': 5}
roi_values = {'Project 1': 3, 'Project 2': 10, 'Project 3': 9, 'Project 4': 6}

# Define criteria weights
weights = {
    'NPV': 0.10,
    'ROI': 0.10,
    'Risk': 0.30,
    'Strategic Plan Alignment': 0.30,
    'Competition': 0.10,
    'Resource Availability': 0.10
}

# Define project-specific criteria values (values from 1 to 10)
risk_values = {'Project 1': 10, 'Project 2': 5, 'Project 3': 5, 'Project 4': 1}
alignment_values = {'Project 1': 10, 'Project 2': 10, 'Project 3': 5, 'Project 4': 5}
competition_values = {'Project 1': 1, 'Project 2': 1, 'Project 3': 10, 'Project 4': 10}
availability_values = {'Project 1': 10, 'Project 2': 10, 'Project 3': 1, 'Project 4': 1}

# Calculate total scores for each project
total_scores = {}

for project in npv_values.keys():
    npv_score = npv_values[project] * weights['NPV']
    roi_score = roi_values[project] * weights['ROI']
    
    # Use array values and normalize to a 0-1 scale
    risk_score = (risk_values[project]) * weights['Risk']
    alignment_score = (alignment_values[project]) * weights['Strategic Plan Alignment']
    competition_score = (competition_values[project]) * weights['Competition']
    availability_score = (availability_values[project]) * weights['Resource Availability']
    
    # Calculate total score
    total_score = npv_score + roi_score + risk_score + alignment_score + competition_score + availability_score
    total_scores[project] = total_score

# Print total scores for each project
for project, score in total_scores.items():
    print(f'{project}: {score:.2f}')
