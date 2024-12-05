def get_study_prompt(medical_notes):
    """Generate prompt for case study creation"""
    return f"""
    Based on the following de-identified medical notes, create a detailed case study 
    that would be valuable for medical student learning. Include relevant clinical findings,
    test results, and important learning points.
    
    Medical Notes:
    {medical_notes}
    
    Generate a structured case study that includes:
    1. Presenting complaint
    2. History of presenting illness
    3. Relevant examination findings
    4. Key investigations and results
    5. Clinical reasoning points
    6. Learning objectives
    """

def get_question_prompt(medical_notes, current_discussion):
    """Generate prompt for next discussion question"""
    return f"""
    Based on these de-identified medical notes and the current discussion,
    generate the next appropriate question to test the student's understanding
    and guide them toward important learning points.
    
    Medical Notes:
    {medical_notes}
    
    Current Discussion:
    {current_discussion}
    
    Generate a thoughtful question that:
    1. Builds on the current discussion
    2. Tests clinical reasoning
    3. Highlights important medical concepts
    4. Encourages deeper understanding
    """