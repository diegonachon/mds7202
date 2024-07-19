import gradio as gr
import pandas as pd
import joblib
import io

pipeline_brf_t3 = joblib.load('brf_best_pipeline.pkl')


columns_names = ['DaysSinceJob', 'CreditCap', 'JobStatus', 'Speed24h', 'AliveSession',
                'BankSpots8w', 'HustleMinutes', 'RiskScore', 'AliasMatch',
                'DeviceEmails8w', 'CribStatus', 'LootMethod', 'InfoSource',
                'HustleMonth', 'ZipHustle', 'Speed4w', 'DeviceOS', 'income', 'FreeMail',
                'HomePhoneCheck', 'BankMonths', 'DOBEmails4w', 'ForeignHustle',
                'DeviceScams', 'OldHoodMonths', 'intended_balcon_amount',
                'NewCribMonths', 'Speed6h', 'CellPhoneCheck', 'customer_age',
                'ExtraPlastic']

def predict(file, text):
    if file is not None:
        file = file.decode('utf-8').strip()
        df = pd.read_csv(io.StringIO(file))
        predictions = pipeline_brf_t3.predict(df)
        return predictions.tolist()
    
    elif text is not None:
        values = eval(text)
        df = pd.DataFrame([values], columns=columns_names)
        predictions = pipeline_brf_t3.predict(df)
        return predictions.tolist()
    
    return "No input provided."

inputs = [
    gr.components.File(label="Adjunta un archivo csv", type="binary"),  
    gr.components.Textbox(label="Ingresa una lista con los datos del cliente.", placeholder="Ejemplo: [0.0067353870811739, 1500.0, 'CB', 7850.955007125409, 1, 5, 16.224843433978073, 163, 0.986506310633034, 1, 'BC', 'AA', 'INTERNET', 0, 1059, 6742.080561007602, 'linux', 0.3, 1, 0, 9, 5, 0, 0, -1, 102.45371092469456, 25, 13096.035018400871, 1, 40, 0]")
]
outputs = gr.components.Textbox()  

interface = gr.Interface(
    fn=predict,
    inputs=inputs,
    outputs=outputs,
    title='Predictions API ',
    analytics_enabled=True
)

if __name__ == "__main__":
    interface.launch(server_name="0.0.0.0", server_port=7860, share=True)