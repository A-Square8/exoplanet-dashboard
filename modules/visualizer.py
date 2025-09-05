import plotly.express as px

def create_discovery_line_chart(discovery_counts):
    return px.line(discovery_counts, x='disc_year', y='counts', title='Discovery Rates Over Years')

def create_method_bar_chart(method_counts):
    return px.bar(method_counts, x='discoverymethod', y='count', title='Counts by Discovery Method')

def create_scatter_plot(filtered_df):
    return px.scatter(filtered_df, x='pl_orbper', y='pl_rade', color='planet_type', trendline='ols',
                      title='Orbital Period vs. Planet Radius (with Trendline)',
                      labels={'pl_orbper': 'Orbital Period (days)', 'pl_rade': 'Planet Radius (Earth)'})

def create_habitable_scatter(habitable):
    return px.scatter(habitable, x='pl_rade', y='pl_insol', color='discoverymethod',
                      title='Habitable Zone Planets (Radius vs. Insolation Flux)')

def create_3d_star_map(filtered_df):
    return px.scatter_3d(filtered_df, x='ra', y='dec', z='sy_dist', color='planet_type',
                         title='3D Distribution of Exoplanet Systems',
                         labels={'ra': 'Right Ascension', 'dec': 'Declination', 'sy_dist': 'Distance (parsecs)'})

# Complex additions
def create_corr_heatmap(corr_matrix):
    return px.imshow(corr_matrix, text_auto=True, aspect='auto', title='Correlation Heatmap')

def create_box_plot(filtered_df):
    return px.box(filtered_df, x='discoverymethod', y='pl_rade', title='Planet Radius by Discovery Method (for ANOVA)')