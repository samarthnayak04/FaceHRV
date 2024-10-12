import pandas as pd
import numpy as np

# File path for the original dataset
file_path = 'C:/Users/sam/CODEs/t4/hrv_stress_data.csv'  
data = pd.read_csv(file_path)

# Calculate mean and standard deviation for RMSDD and SDNN
rmsdd_mean = data.iloc[:, 0].mean()
rmsdd_std = data.iloc[:, 0].std()
sdnn_mean = data.iloc[:, 1].mean()
sdnn_std = data.iloc[:, 1].std()

# Count occurrences of labels
label_counts = data.iloc[:, 2].value_counts(normalize=True)

# Print label counts to debug
print("Label Counts:\n", label_counts)

# Directly assign proportions based on the dataset
calm_proportion = label_counts.get(0, 0)  # 0 for calm
stress_proportion = label_counts.get(1, 0)  # 1 for stress

# Calculate total proportion
total_proportion = calm_proportion + stress_proportion

# Check if total_proportion is zero
if total_proportion == 0:
    print("No labels found in the dataset. Cannot generate synthetic data.")
else:
    # Calculate normalized proportions
    normalized_calm_proportion = calm_proportion / total_proportion
    normalized_stress_proportion = stress_proportion / total_proportion

    # Number of synthetic samples to generate
    num_synthetic_samples = 100

    # Generate synthetic RMSDD and SDNN values
    synthetic_rmsdd = np.random.normal(loc=rmsdd_mean, scale=rmsdd_std, size=num_synthetic_samples)
    synthetic_sdnn = np.random.normal(loc=sdnn_mean, scale=sdnn_std, size=num_synthetic_samples)

    # Generate synthetic labels with the specified proportions
    synthetic_labels = np.random.choice([0, 1], size=num_synthetic_samples, 
                                         p=[normalized_calm_proportion, normalized_stress_proportion])

    # Create a DataFrame for synthetic data
    synthetic_data = pd.DataFrame({
        'RMSSD': synthetic_rmsdd,
        'SDNN': synthetic_sdnn,
        'stressMetric': synthetic_labels  # Use binary labels directly
    })

    # Save the synthetic data to CSV
    synthetic_data.to_csv('synthetic_hrv_data.csv', mode='a', index=False)
