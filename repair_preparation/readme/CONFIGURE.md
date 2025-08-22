## 1) Create a Preparation area
1. Go to **Inventory ▸ Configuration ▸ Locations**.
2. Create an **internal** location, e.g. **WH/Preparation**, under your warehouse **Stock** location.

## 2) Create a Preparation picking type
1. Go to **Inventory ▸ Configuration ▸ Operation Types**.
2. Create an **Internal Transfer** type named **Preparation**.
3. Set:
   - **Default Source Location** = *Your Warehouse / Stock*
   - **Default Destination Location** = *Your Warehouse / Preparation*

## 3) Route & rule (Stock → Preparation)
1. Go to **Inventory ▸ Configuration ▸ Routes** and create **Route to Preparation**.
2. Enable **Selectable on warehouse**.
3. Add a **Pull Rule**:
   - **Action**: *Pull From*
   - **Operation Type**: *Preparation* (created above)
   - **Source Location**: *Your Warehouse / Stock*
   - **Destination Location**: *Your Warehouse / Preparation*
   - **Warehouse**: your warehouse
