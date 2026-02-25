# Connect CSVs to the Dashboard

## Included dashboard
`Dashboard/User_Journey_Tableau_Dashboard.twbx`

## Connect for Tableau (.twbx)
1. Open the `.twbx`
2. In **Data** pane, choose **Replace Data Source**
3. Point each table to the matching CSV in `Data/clean/` (same table name prefix)
4. Refresh extracts if prompted

## Connect for Power BI (.pbix)
1. Open the `.pbix`
2. Go to **Transform data** → **Data source settings**
3. Change Source to the CSVs in `Data/clean/`
4. Apply changes and refresh

## Table name matching
- Table prefixes match CSV names: e.g., `orders_clean.csv` → Orders table
- If your dashboard uses different table names, update table mapping in **Power Query** (Power BI) or **Data Source** (Tableau)
