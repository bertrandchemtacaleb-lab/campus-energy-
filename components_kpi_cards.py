"""Composant réutilisable : cartes d'indicateurs clés (KPI)."""
import streamlit as st


def render_kpi_row(kpis: dict[str, str]) -> None:
    """`kpis` : dict {libellé: valeur affichée}. Affiche une ligne de cartes st.metric."""
    columns = st.columns(len(kpis))
    for col, (label, value) in zip(columns, kpis.items()):
        with col:
            st.metric(label, value)
