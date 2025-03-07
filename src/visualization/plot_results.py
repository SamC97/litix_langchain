import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_detailed_results(detailed_csv, output_dir="plots"):
    """
    Load detailed comparison results from CSV and generate plots.
    
    For textual fields (Title, Author):
        - Generate heatmaps showing metrics (WER, CER and Levenshtein distance)
          for each document.
    
    For non-textual fields (Publication Year, Groundwater level mentioned):
        - Generate grouped bar plots where the x-axis represents documents and each metric 
          (Precision, Recall, F1) is displayed as a separate bar.
          
    Parameters:
        detailed_csv (str): Path to the CSV file containing detailed per-field results.
        output_dir (str): Directory where the plots will be saved.
    """
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(detailed_csv)

    # Convert numeric columns (non-numeric cells become NaN)
    metric_cols = ["WER", "CER", "Levenshtein", "Precision", "Recall", "F1", "Found"]
    for col in metric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Define field groups and associated metrics
    textual_fields = {
        "Title": ["WER", "CER", "Levenshtein"],
        "Author": ["WER", "CER", "Levenshtein"]
    }

    # --- Plot heatmaps for textual fields ---
    for field, metrics in textual_fields.items():
        df_field = df[df["Field"] == field]
        # Pivot: rows = Filename, columns = metrics
        df_pivot = df_field.set_index("Filename")[metrics]
        plt.figure(figsize=(10, max(4, 0.5 * len(df_pivot) + 1)))
        ax = sns.heatmap(df_pivot, annot=True, fmt=".2f", cmap="viridis", cbar_kws={'label': 'Metric Value'})
        plt.title(f"{field} Metrics (Textual)")
        plt.xlabel("Metric")
        plt.ylabel("Document")
        plt.tight_layout()
        save_path = os.path.join(output_dir, f"heatmap_{field.lower().replace(' ', '_')}_textual.png")
        plt.savefig(save_path, bbox_inches="tight")
        plt.close()
        print(f"Saved heatmap for {field} to {save_path}")

    # --- Plot checkmark table with average accuracy row ---
    # Create a pivot table from the "Found" column
    df_pivot = df.pivot(index="Filename", columns="Field", values="Found")
    # Compute average accuracy for each field (numeric, between 0 and 1)
    avg_series = df_pivot.mean().round(2)
    avg_series.name = "AVERAGE"
    # Append the average row to the pivot table
    df_pivot_with_avg = pd.concat([df_pivot, avg_series.to_frame().T])
    
     # Convert the DataFrame to object dtype to allow string replacement
    df_pivot_with_avg = df_pivot_with_avg.astype(object)
    
    # Create a display DataFrame:
    # For rows not "AVERAGE", replace 0 with "✗" and 1 with "✓"
    df_display = df_pivot_with_avg.copy()
    mask = df_display.index != "AVERAGE"
    df_display.loc[mask] = df_display.loc[mask].map(lambda x: "✗" if x == 0 else ("✓" if x == 1 else x))
    # For the "AVERAGE" row, format as a percentage string
    df_display.loc["AVERAGE"] = df_display.loc["AVERAGE"].apply(lambda x: f"{x*100:.0f}%")
    
    # Create a mapping for long field names to shorter labels
    rename_map = {
        "Title": "Title",
        "Author": "Author",
        "Publication Year": "Pub. Year",
        "Groundwater level mentioned": "GW Mentioned"
    }
    df_display = df_display.rename(columns=rename_map)
    
    desired_order = ["Title", "Author", "Pub. Year", "GW Mentioned"]
    df_display = df_display[desired_order]
    
    fig, ax = plt.subplots(figsize=(12, max(4, 0.8 * len(df_display) + 1)))
    ax.axis('off')
    table = ax.table(
        cellText=df_display.values,
        rowLabels=df_display.index,
        colLabels=df_display.columns,
        loc='center',
        cellLoc='center'
    )
    table.scale(1, 1.5)
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    
    header_color = "#40466e"
    for key, cell in table.get_celld().items():
        row, col = key
        if row == 0:
            cell.set_facecolor(header_color)
            cell.get_text().set_color("white")
            cell.get_text().set_weight("bold")
        else:
            if col == -1:
                cell.set_facecolor("#f2f2f2")
            else:
                text = cell.get_text().get_text()
                if text == "✓":
                    cell.set_facecolor("#dff0d8")  # light green
                elif text == "✗":
                    cell.set_facecolor("#f2dede")  # light red
                else:
                    cell.set_facecolor("white")
        cell.get_text().set_ha("center")
        cell.get_text().set_va("center")
    
    plt.title("Fields - Found or Not (F1=1) with Average Accuracy", pad=5)
    plt.tight_layout()
    save_path = os.path.join(output_dir, "resume_fields_found_with_avg.png")
    plt.savefig(save_path, bbox_inches="tight")
    plt.close()
    print(f"Saved improved checkmark table with average row to {save_path}")