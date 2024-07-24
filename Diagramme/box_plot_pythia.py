# Box Plot von Pythia Modell mit der Daten
import pandas as pd
import matplotlib.pyplot as plt

# Daten für BLEU
BLEU = {
'0%': [0.60592, 0.61779, 0.60759, 0.61455, 0.61549, 0.60019, 0.61673, 0.62018, 0.60921, 0.63235],
'10%': [0.29553, 0.29975, 0.29987, 0.28749, 0.28485, 0.28057, 0.29563, 0.29988, 0.30177, 0.28749],
"20%": [0.22381, 0.22267, 0.22364, 0.26366, 0.26426, 0.25908, 0.26032, 0.26375, 0.25951, 0.26366],
'50%': [0.09874, 0.09917, 0.09852, 0.09818, 0.09847, 0.09864, 0.09877, 0.09861, 0.09836, 0.09856],
'100%': [0.05341, 0.05337, 0.05344, 0.05357, 0.05341, 0.0534, 0.05339, 0.05338, 0.05358, 0.05341]
}

# Daten für Perplexität
PPL = {
'0%': [299.7, 309.19, 302.8, 307.66, 304.47, 305.79, 300.51, 303.39, 297.94, 305.95],
'10%': [401.97, 401.97, 401.97, 401.97, 401.97, 401.97, 401.97, 401.97, 401.97, 401.97],
"20%": [401.97, 401.97, 401.97, 401.97, 401.97, 401.97, 401.97, 401.97, 401.97, 401.97],
'50%': [401.97, 401.97, 401.97, 401.97, 401.97, 401.97, 401.97, 401.97, 401.97, 401.97],
'100%': [401.97, 401.97, 401.97, 401.97, 401.97, 401.97, 401.97, 401.97, 401.97, 401.97]
}

# Daten für ROUGE
ROUGE_1 = {
'0%': [0.77353, 0.76242, 0.76242, 0.76242, 0.76658, 0.76242, 0.77151, 0.77353, 0.77353, 0.76242],
'10%': [0.787, 0.787, 0.79155, 0.787, 0.78701, 0.78701, 0.787, 0.787, 0.79155, 0.787],
"20%": [0.7197, 0.7197, 0.7197, 0.78701, 0.78701, 0.78701, 0.78701, 0.78701, 0.78701, 0.78701],
'50%': [0.79155, 0.79155, 0.79155, 0.79155, 0.79155, 0.79155, 0.79155, 0.79155, 0.79155, 0.79155],
'100%': [0.80266, 0.80266, 0.80266, 0.80266, 0.80266, 0.80266, 0.80266, 0.80266, 0.80266, 0.80266]
}
ROUGE_2 = {
'0%': [0.7567, 0.7567, 0.7567, 0.7567, 0.7567, 0.7567, 0.76125, 0.7567, 0.7567, 0.7567],
'10%': [0.7567, 0.7567, 0.7567, 0.7567, 0.75671, 0.75671, 0.7567, 0.7567, 0.7567, 0.7567],
"20%": [0.68797, 0.68798, 0.68798, 0.75671, 0.75671, 0.75671, 0.75671, 0.75671, 0.75671, 0.75671],
'50%': [0.7567, 0.7567, 0.7567, 0.7567, 0.7567, 0.7567, 0.7567, 0.7567, 0.7567, 0.7567],
'100%': [0.7692, 0.7692, 0.7692, 0.7692, 0.7692, 0.7692, 0.7692, 0.7692, 0.7692, 0.7692]
}
ROUGE_L = {
'0%': [0.77353, 0.76242, 0.76242, 0.76242, 0.76658, 0.76242, 0.77151, 0.77353, 0.77353, 0.76242],
'10%': [0.787, 0.787, 0.79155, 0.787, 0.787, 0.787, 0.787, 0.787, 0.79155, 0.787],
"20%": [0.7197, 0.7197, 0.7197, 0.787, 0.787, 0.787, 0.787, 0.787, 0.787, 0.787],
'50%': [0.787, 0.79155, 0.79155, 0.79155, 0.787, 0.78755, 0.79155, 0.791, 0.79155, 0.787],
'100%': [0.80266, 0.80266, 0.80266, 0.80266, 0.80266, 0.80266, 0.80266, 0.80266, 0.80266, 0.80266]
}

# Daten für WMD
WMD = {
'0%': [0.152, 0.151, 0.164, 0.146, 0.149, 0.153, 0.158, 0.146, 0.154, 0.16],
'10%': [0.229, 0.232, 0.225, 0.246, 0.248, 0.248, 0.229, 0.232, 0.225, 0.245],
"20%": [0.239, 0.244, 0.242, 0.243, 0.245, 0.245, 0.245, 0.244, 0.253, 0.243],
'50%': [0.269, 0.266, 0.268, 0.267, 0.267, 0.269, 0.267, 0.268, 0.267, 0.267],
'100%': [0.271, 0.27, 0.27, 0.27, 0.271, 0.27, 0.27, 0.27, 0.271, 0.271]
}
df = pd.DataFrame(ROUGE_2)
df.plot.box(title="ROUGE_2 - Pythia_7B")
plt.grid(linestyle="--", alpha=0.3)
plt.show()

