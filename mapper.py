import json
def get_nested_value(data, keys):
    """
    Retrieve a nested value from a dictionary given a list of keys.
    If any key is missing in the path, return None.
    """
    for key in keys:
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return None
    return data


def map_llm_response(mapping_json, llm_response_json):
    """
    Map the LLM response JSON to a new structure based on the mapping JSON.
    If a path in the mapping JSON does not exist in the LLM response JSON, return None.
    """
    response = {}

    for map_key, path in mapping_json.items():
        # Split the path into individual keys
        keys = path.split('.')
        
        # Retrieve the value from the LLM response JSON based on the key path
        value = get_nested_value(llm_response_json, keys)
        
        # Add the mapped value (or None if not found) to the response dictionary
        response[map_key] = value

    return response


# Example usage:
mapping_json = {
    "photosynthesis_summary": "summary",
    "detailed_explanation_intro": "detailed_explanation.introduction",
    "light_reaction_location": "detailed_explanation.stages.0.location",
    "calvin_cycle_steps": "detailed_explanation.stages.1.steps",
    "photosynthesis_equation": "detailed_explanation.equation.text"
}

llm_response_json = {
    "summary": "Photosynthesis is a biological process by which plants, algae, and some bacteria convert light energy into chemical energy, stored in glucose.",
    "detailed_explanation": {
        "introduction": {
            "definition": "Photosynthesis is the process of converting light energy into chemical energy in the form of glucose, primarily in chloroplasts of plant cells.",
            "importance": "It provides the primary source of energy for nearly all life forms on Earth and is crucial for maintaining atmospheric oxygen levels."
        },
        "stages": [
            {
                "stage": "Light-dependent reactions",
                "location": "Thylakoid membrane",
                "steps": [
                    "Photons from sunlight are absorbed by chlorophyll molecules.",
                    "Water molecules are split (photolysis), producing oxygen as a byproduct.",
                    "Electrons are excited to a higher energy state and travel through the electron transport chain.",
                    "Energy generated from electron transport is used to pump protons into the thylakoid lumen, creating a proton gradient.",
                    "ATP and NADPH are generated for the Calvin cycle."
                ]
            },
            {
                "stage": "Calvin Cycle (Light-independent reactions)",
                "location": "Stroma of chloroplasts",
                "steps": [
                    "CO2 is fixed by the enzyme RuBisCO.",
                    "The fixed carbon undergoes a series of reactions, resulting in the production of G3P (glyceraldehyde-3-phosphate).",
                    "G3P can be used to form glucose and other carbohydrates.",
                    "Regeneration of RuBP (Ribulose bisphosphate) to continue the cycle."
                ]
            }
        ],
        "equation": {
            "text": "6 CO2 + 6 H2O + light → C6H12O6 + 6 O2",
            "molecules": [
                { "reactant": "CO2", "amount": "6 molecules" },
                { "reactant": "H2O", "amount": "6 molecules" },
                { "product": "C6H12O6", "amount": "1 molecule" },
                { "product": "O2", "amount": "6 molecules" }
            ]
        }
    }
}

# Generate the mapped response
mapped_response = map_llm_response(mapping_json, llm_response_json)

# Write the output JSON to a file
output_file = 'mapped_response.json'
with open(output_file, 'w') as f:
    json.dump(mapped_response, f, indent=4)

print(f"Mapped response saved to {output_file}")
