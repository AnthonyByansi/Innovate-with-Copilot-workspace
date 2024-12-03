# air_quality_analysis - Starter file for Sustainable-Tech
# air_quality_analysis - Starter file for Sustainable-Tech

import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load air quality data from a CSV file.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    DataFrame: A pandas DataFrame containing the air quality data.
    """
    return pd.read_csv(file_path)

def analyze_data(df):
    """
    Analyze the air quality data.
    
    Parameters:
    df (DataFrame): The air quality data.
    
    Returns:
    dict: A dictionary containing analysis results.
    """
    analysis_results = {
        'mean': df.mean(),
        'median': df.median(),
        'std_dev': df.std()
    }
    return analysis_results

def plot_data(df):
    """
    Plot the air quality data.
    
    Parameters:
    df (DataFrame): The air quality data.
    """
    df.plot()
    plt.title('Air Quality Data')
    plt.xlabel('Time')
    plt.ylabel('Air Quality Index')
    plt.show()

def main():
    # Load the data
    file_path = 'path/to/your/air_quality_data.csv'
    df = load_data(file_path)
    
    # Analyze the data
    analysis_results = analyze_data(df)
    print("Analysis Results:", analysis_results)
    
    # Plot the data
    plot_data(df)

if __name__ == "__main__":
    main()