# bmi_calculator - Starter file for Healthcare-Innovation

def calculate_bmi(weight, height, unit):
    """
    Calculate BMI using weight and height.

    Parameters:
    weight (float): Weight of the individual.
    height (float): Height of the individual.
    unit (str): Unit system - "metric" or "imperial".

    Returns:
    float: Calculated BMI.
    """
    if unit == "metric":
        return weight / (height ** 2)
    elif unit == "imperial":
        return 703 * weight / (height ** 2)
    else:
        raise ValueError("Invalid unit. Use 'metric' or 'imperial'.")

if __name__ == "__main__":
    # Test the calculate_bmi function with sample inputs
    weight_metric = 70  # kg
    height_metric = 1.75  # meters
    weight_imperial = 154  # lbs
    height_imperial = 69  # inches

    bmi_metric = calculate_bmi(weight_metric, height_metric, "metric")
    bmi_imperial = calculate_bmi(weight_imperial, height_imperial, "imperial")

    print(f"BMI (Metric): {bmi_metric:.2f}")
    print(f"BMI (Imperial): {bmi_imperial:.2f}")
