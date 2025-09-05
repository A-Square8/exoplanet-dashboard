import streamlit as st
from modules.data_loader import load_exoplanet_data
from modules.data_cleaner import clean_data
from modules.feature_engineer import engineer_features
from modules.analyzer import compute_metrics, get_habitable_planets
from modules.visualizer import (create_discovery_line_chart, create_method_bar_chart, create_scatter_plot,
                                create_habitable_scatter, create_3d_star_map, create_corr_heatmap, create_box_plot)

@st.cache_data
def process_data():
    raw_df = load_exoplanet_data()
    cleaned_df = clean_data(raw_df)
    engineered_df = engineer_features(cleaned_df)
    return engineered_df

df = process_data()

st.sidebar.title('Filters')
years = sorted(df['disc_year'].unique())
selected_years = st.sidebar.multiselect('Select Years', years, default=years[-5:])
methods = sorted(df['discoverymethod'].unique())
selected_methods = st.sidebar.multiselect('Select Discovery Methods', methods, default=methods)
types = sorted(df['planet_type'].unique())
selected_types = st.sidebar.multiselect('Select Planet Types', types, default=types)
hz_classes = sorted(df['hz_class'].unique())
selected_hz = st.sidebar.multiselect('Select Habitable Zone Classes', hz_classes, default=hz_classes)

filtered_df = df[
    (df['disc_year'].isin(selected_years)) &
    (df['discoverymethod'].isin(selected_methods)) &
    (df['planet_type'].isin(selected_types)) &
    (df['hz_class'].isin(selected_hz))
]

st.title('Modular Astronomy Insights Dashboard')
st.write(f'Filtered to {len(filtered_df)} planets.')

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Step 1: Ingestion", "Step 2: Cleaning", "Step 3: Engineering", "Step 4: Analysis", "Step 5: Visualization"])

with tab1:
    st.header('Step 1: Data Ingestion')
    st.write('Raw data preview:')
    st.dataframe(df.head(5))

with tab2:
    st.header('Step 2: Data Cleaning')
    st.write('Cleaned data stats (e.g., shape, nulls):')
    st.write(f"Shape: {df.shape}, Nulls in key cols: 0")

with tab3:
    st.header('Step 3: Feature Engineering')
    st.write('Engineered features preview (e.g., planet_type, hz_class):')
    st.dataframe(filtered_df[['pl_rade', 'planet_type', 'hz_class', 'hz_inner', 'hz_outer']].head())

with tab4:
    st.header('Step 4: Analysis')
    metrics = compute_metrics(filtered_df)
    habitable = get_habitable_planets(filtered_df)
    st.write(f"Average host star brightness (vmag): {metrics['avg_brightness']:.2f}")
    st.write(metrics['anova_result'])
    st.write('Correlation Matrix:')
    st.dataframe(metrics['corr_matrix'])
    st.write(f'Found {len(habitable)} habitable planets.')

with tab5:
    st.header('Step 5: Visualization')
    st.plotly_chart(create_discovery_line_chart(metrics['discovery_counts']))
    st.plotly_chart(create_method_bar_chart(metrics['method_counts']))
    st.plotly_chart(create_scatter_plot(filtered_df))
    st.plotly_chart(create_habitable_scatter(habitable))
    st.plotly_chart(create_3d_star_map(filtered_df))
    st.plotly_chart(create_corr_heatmap(metrics['corr_matrix']))
    st.plotly_chart(create_box_plot(filtered_df))

st.download_button('Download Filtered Data', filtered_df.to_csv(index=False), file_name='filtered_exoplanets.csv')
