import matplotlib.pyplot as plt

def outliers_iqr(data):
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return list(data[(data < lower_bound) | (data > upper_bound)])

def laps_boxplot(laps_df, title):
    # Prepare data for boxplot: group lap durations by driver_number
    lap_data = [[dn, laps_df[laps_df['driver_number'] == dn]['lap_duration'].values] for dn in sorted(laps_df['driver_number'].unique())]

    sorted_boxplot_data = sorted(lap_data, key=lambda x: x[1].min())
    driver_numbers = [x[0] for x in sorted_boxplot_data]
    boxplot_data = [x[1] for x in sorted_boxplot_data]

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)

    ax.boxplot(boxplot_data, tick_labels=driver_numbers, zorder=3, patch_artist=True)
    ax.set_xlabel('Driver Number')
    ax.set_ylabel('Lap Duration (s)')
    ax.set_title(title)

    plt.show()