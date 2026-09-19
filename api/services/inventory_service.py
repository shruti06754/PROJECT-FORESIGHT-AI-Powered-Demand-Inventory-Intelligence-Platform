def generate_recommendation(row):
    stockout = str(row.get("Stockout_Risk", "")).lower()
    overstock = str(row.get("Overstock_Risk", "")).lower()

    if stockout == "high":
        return "Reorder stock immediately"
    elif stockout == "medium":
        return "Monitor stock and prepare reorder"
    elif overstock == "high":
        return "Reduce inventory and consider promotion"
    elif overstock == "medium":
        return "Monitor excess inventory"
    else:
        return "No immediate action required"


def build_inventory_recommendation(row):
    return {
        "date": str(row.get("Date", "")),
        "sku": str(row.get("SKU", "")),
        "product_name": str(row.get("Product_Name", "")),
        "category": str(row.get("Category", "")),
        "predicted_demand": row.get("Predicted_Demand"),
        "current_stock": row.get("Current_Stock"),
        "on_order": row.get("On_Order"),
        "stockout_risk": row.get("Stockout_Risk"),
        "overstock_risk": row.get("Overstock_Risk"),
        "stock_status": row.get("Stock_Status"),
        "action": row.get("Action"),
        "priority": row.get("Priority"),
        "health_level": row.get("Health_Level"),
        "inventory_health_score": row.get("Inventory_Health_Score"),
        "recommendation": generate_recommendation(row)
    }