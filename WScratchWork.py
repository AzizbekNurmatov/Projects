import pandas as pd

# Prepare the Master List
master_list = pd.DataFrame({
    "Name": ["Pirates Voyage", "WonderWorks", "Broadway Show", "Seafood Shack", "Ocean Grill", "Family Diner"],
    "Category": ["Show", "Attraction", "Show", "Restaurant", "Restaurant", "Restaurant"],
    "Retail Adult": [73, 30, 85, 25, 40, 15],
    "Retail Child": [33, 20, 50, 15, 25, 10],
    "CMA Adult": [35, 15, 40, 12, 20, 8],
    "CMA Child": [20, 10, 25, 8, 15, 5],
    "Notes": [
        "Dinner included",
        "Indoor science fun",
        "VIP seating available",
        "Fresh seafood specials",
        "Oceanfront dining",
        "Kid-friendly menu"
    ]
})

# Prepare Booking & Calculation example
booking_calc = pd.DataFrame({
    "Field": [
        "Customer Name", "Agent Name", "Date & Time",
        "Attraction 1", "Adults 1", "Children 1",
        "Attraction 2", "Adults 2", "Children 2",
        "Attraction 3", "Adults 3", "Children 3",
        "Retail Total", "CMA Total", "Savings", "Gift Needed", "Guest Pays Before Min", "Refundable Deductible", "Final Payment Due"
    ],
    "Example Input / Output": [
        "Sarah Johnson", "Mike", "5/22/2025 2:30 PM",
        "Pirates Voyage", 2, 2,
        "Family Diner", 2, 2,
        "WonderWorks", 0, 3,
        292, 132, 160, 0, 132, 0, 132
    ]
})

# Prepare Booking Log sample
booking_log = pd.DataFrame({
    "Timestamp": ["5/22/2025 2:30 PM"],
    "Customer Name": ["Sarah Johnson"],
    "Agent Name": ["Mike"],
    "Attractions": ["Pirates Voyage, Family Diner, WonderWorks"],
    "Adults": [4],
    "Children": [7],
    "Retail Total": [292],
    "CMA Total": [132],
    "Gift Value": [0],
    "Refundable Deductible": [0],
    "Final Payment": [132],
    "Notes": ["Great presentation"]
})

# Save to Excel to simulate sheet tabs (for reference)
path = "/mnt/data/Travel_Leisure_Sample_Template.xlsx"
with pd.ExcelWriter(path) as writer:
    master_list.to_excel(writer, sheet_name="Master List", index=False)
    booking_calc.to_excel(writer, sheet_name="Booking & Calculations", index=False)
    booking_log.to_excel(writer, sheet_name="Booking Log", index=False)

path
