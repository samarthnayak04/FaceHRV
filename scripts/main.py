from video_capture import capture_ppg_signal
from hrv_analysis import calculate_hrv_metrics
from feedback_system import provide_feedback
from preprocessing import preprocess_signal
import pandas as pd

if __name__ == "__main__":
    ppg_signal = capture_ppg_signal(duration=30)
    filtered_ppg_signal = preprocess_signal(ppg_signal)
    rmssd, sdnn = calculate_hrv_metrics(filtered_ppg_signal)
    print(f"RMSSD: {rmssd:.4f}, SDNN: {sdnn:.4f}")
    condition = provide_feedback(rmssd)
    if condition=="stress":
        stressMetric=1
    else:
        stressMetric=0    


    data = {
        'RMSSD ': [rmssd*100],
        'SDNN ': [sdnn*100],
        'condition':[stressMetric],
        
    }

    df = pd.DataFrame(data)
    #add your custom csv file to store your rmssd data in it 
    df.to_csv('.csv', mode='a', header=False, index=False)  # Append to the CSV file

    print(df)
