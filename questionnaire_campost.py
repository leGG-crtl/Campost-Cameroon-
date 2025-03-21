 
import streamlit as st
import pandas as pd

st.title("📦 Questionnaire CAMPOST - Gestion des Colis et Satisfaction Client")

st.header("📌 Partie 1 : Informations Générales")
age = st.radio("1️⃣ Âge :", ["Moins de 18 ans", "18 - 30 ans", "31 - 45 ans", "Plus de 45 ans"])
genre = st.radio("2️⃣ Genre :", ["Homme", "Femme", "Autre"])
frequence = st.selectbox("3️⃣ Fréquence d’utilisation :", ["Moins d’une fois par mois", "1 à 3 fois par mois", "Plus de 3 fois par mois"])
type_envoi = st.selectbox("4️⃣ Type d’envoi le plus fréquent :", ["Documents", "Petits colis (-5kg)", "Colis volumineux (+5kg)"])

st.header("📌 Partie 2 : Expérience Client")
probleme = st.radio("5️⃣ Avez-vous rencontré des problèmes avec CAMPOST ?", ["Oui", "Non"])
details_probleme = st.multiselect("6️⃣ Quels types de problèmes ?", ["Retard de livraison", "Perte de colis", "Colis endommagé", "Mauvaise communication"]) if probleme == "Oui" else []
frequence_pb = st.radio("7️⃣ Fréquence des problèmes ?", ["Rarement", "Occasionnellement", "Souvent"])
solution_campos = st.radio("8️⃣ CAMPOST a-t-il résolu le problème ?", ["Oui, efficace", "Oui, mais insuffisant", "Non, problème non résolu"])

st.header("📌 Partie 3 : Satisfaction Client")
satisfaction_criteria = ["Rapidité", "Fiabilité du suivi", "Service client"]
satisfaction = {critère: st.slider(f"🔹 {critère}", 1, 5, 3) for critère in satisfaction_criteria}

st.header("📌 Partie 4 : Suggestions d’Amélioration")
amelioration = st.multiselect("🔧 Améliorations souhaitées ?", ["Suivi en temps réel", "Livraison plus rapide", "Service client amélioré", "Meilleure gestion des réclamations"])
appli = st.radio("📱 Voulez-vous une application mobile CAMPOST ?", ["Oui", "Non"])

st.header("📊 Récapitulatif")
resultats = {
    "Âge": age, "Genre": genre, "Fréquence": frequence, "Type d’envoi": type_envoi,
    "Problèmes": ", ".join(details_probleme) if probleme == "Oui" else "Aucun",
    "Fréquence des problèmes": frequence_pb, "Solution CAMPOST": solution_campos,
    "Satisfaction": satisfaction, "Améliorations demandées": amelioration, "Application mobile": appli
}
st.write(resultats)

df = pd.DataFrame([resultats])
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("📩 Télécharger en CSV", data=csv, file_name="questionnaire_campost.csv", mime="text/csv")

if st.button("✅ Soumettre"):
    st.success("Merci pour votre participation ! 🚀")
