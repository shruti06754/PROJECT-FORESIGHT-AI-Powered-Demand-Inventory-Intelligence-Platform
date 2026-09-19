import requests
import pandas as pd
import streamlit as st
import plotly.express as px


# ============================================================
# CONFIG
# ============================================================

API_URL = "https://foresight-ai-demand-inventory.onrender.com"

st.set_page_config(
    page_title="FORESIGHT",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PROFESSIONAL UI CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ==============================
       GLOBAL
    ============================== */

    .stApp {
        background: #f5f7fb;
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1500px;
    }

    /* ==============================
       MAIN TEXT
    ============================== */

    h1, h2, h3, h4, h5, h6 {
        color: #111827 !important;
    }

    p, span, label {
        color: #374151;
    }

    /* ==============================
       SIDEBAR
    ============================== */
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0E1117 !important;
    }

    [data-testid="stSidebar"] > div:first-child {
        background-color: #0E1117 !important;
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #FFFFFF !important;
    }

    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {
        color: #E5E7EB !important;
    }

    /* ==============================
       SELECTBOX / INPUT
    ============================== */

    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        border: 1px solid #d1d5db !important;
        color: #111827 !important;
    }

    div[data-baseweb="select"] span {
        color: #111827 !important;
    }

    div[data-baseweb="select"] input {
        color: #111827 !important;
    }

    /* Date input */
    div[data-testid="stDateInput"] input {
        background-color: #ffffff !important;
        color: #111827 !important;
        border: 1px solid #d1d5db !important;
    }

    /* ==============================
       HEADER
    ============================== */

    .foresight-title {
        font-size: 42px;
        font-weight: 800;
        color: #111827;
        letter-spacing: -1px;
        margin-bottom: 0;
    }

    .foresight-subtitle {
        font-size: 16px;
        color: #6b7280;
        margin-top: 3px;
        margin-bottom: 30px;
    }

    /* ==============================
       KPI CARDS
    ============================== */

    .kpi-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 20px 22px;
        min-height: 125px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.04);
    }

    .kpi-label {
        font-size: 14px;
        font-weight: 600;
        color: #6b7280;
        margin-bottom: 10px;
    }

    .kpi-value {
        font-size: 30px;
        font-weight: 800;
        color: #111827;
    }

    /* ==============================
       SECTION BOX
    ============================== */

    .section-box {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 20px;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    .section-heading {
        font-size: 21px;
        font-weight: 750;
        color: #111827;
        margin-bottom: 4px;
    }

    .section-description {
        font-size: 14px;
        color: #6b7280;
        margin-bottom: 15px;
    }

    /* ==============================
       BUTTON
    ============================== */

    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
    }

    /* ==============================
       DATAFRAME
    ============================== */

    div[data-testid="stDataFrame"] {
        border-radius: 10px;
        overflow: hidden;
        border: 1px solid #e5e7eb;
    }

    /* ==============================
       DIVIDER
    ============================== */

    hr {
        border-color: #e5e7eb !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FUNCTIONS
# ============================================================

@st.cache_data(ttl=60)
def get_api_data(endpoint):

    try:

        response = requests.get(
            f"{API_URL}{endpoint}",
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:

        st.error(f"❌ API connection failed: {e}")

        return None


def kpi_card(label, value, icon):

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">{icon} {label}</div>
            <div class="kpi-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def section_header(title, description=None):

    st.markdown(
        f"""
        <div class="section-heading">
            {title}
        </div>
        """,
        unsafe_allow_html=True
    )

    if description:

        st.markdown(
            f"""
            <div class="section-description">
                {description}
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="foresight-title">📊 FORESIGHT</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="foresight-subtitle">'
    'AI-Powered Demand & Inventory Intelligence Platform'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center; padding:10px 0 15px 0;">
            <div style="font-size:32px;">📊</div>
            <div style="
                color:white;
                font-size:24px;
                font-weight:800;
            ">
                FORESIGHT
            </div>
            <div style="
                color:#9ca3af;
                font-size:13px;
                margin-top:3px;
            ">
                Inventory Intelligence
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        "### 🧭 Navigation"
    )

    page = st.radio(
        "Select Module",
        [
            "Overview",
            "Demand Forecast",
            "Inventory",
            "Recommendations"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown(
        """
        <div style="
            padding:12px;
            border-radius:10px;
            background:#1f2937;
        ">
            <div style="color:#ffffff;font-weight:700;">
                FORESIGHT AI
            </div>
            <div style="
                color:#9ca3af;
                font-size:12px;
                margin-top:5px;
                line-height:1.6;
            ">
                Demand Forecasting<br>
                Inventory Risk Detection<br>
                Smart Reordering
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# OVERVIEW
# ============================================================

if page == "Overview":

    section_header(
        "Dashboard Overview",
        "Real-time overview of demand, inventory and supply-chain risks."
    )

    with st.spinner("Loading dashboard data..."):

        forecast_response = get_api_data(
            "/forecast?limit=10000"
        )

        inventory_response = get_api_data(
            "/inventory?limit=10000"
        )

        recommendation_response = get_api_data(
            "/recommendations?limit=10000"
        )

    if (
        forecast_response
        and inventory_response
        and recommendation_response
    ):

        forecast_df = pd.DataFrame(
            forecast_response["data"]
        )

        inventory_df = pd.DataFrame(
            inventory_response["data"]
        )

        recommendation_df = pd.DataFrame(
            recommendation_response["data"]
        )

        # ----------------------------------------------------
        # KPI
        # ----------------------------------------------------

        total_skus = (
            forecast_df["SKU"].nunique()
            if "SKU" in forecast_df.columns
            else 0
        )

        forecast_records = len(forecast_df)

        inventory_records = len(inventory_df)

        stockout_high = (
            recommendation_df["stockout_risk"]
            .astype(str)
            .str.lower()
            .eq("high")
            .sum()
            if "stockout_risk" in recommendation_df.columns
            else 0
        )

        overstock_high = (
            recommendation_df["overstock_risk"]
            .astype(str)
            .str.lower()
            .eq("high")
            .sum()
            if "overstock_risk" in recommendation_df.columns
            else 0
        )

        st.markdown("### 📌 Key Performance Indicators")

        c1, c2, c3, c4, c5 = st.columns(5)

        with c1:
            kpi_card(
                "Unique SKUs",
                f"{total_skus:,}",
                "📦"
            )

        with c2:
            kpi_card(
                "Forecast Records",
                f"{forecast_records:,}",
                "📈"
            )

        with c3:
            kpi_card(
                "Inventory Records",
                f"{inventory_records:,}",
                "🏭"
            )

        with c4:
            kpi_card(
                "High Stockout Risk",
                f"{stockout_high:,}",
                "🔴"
            )

        with c5:
            kpi_card(
                "High Overstock Risk",
                f"{overstock_high:,}",
                "🟠"
            )

        st.write("")

        # ----------------------------------------------------
        # FORECAST
        # ----------------------------------------------------

        section_header(
            "📈 Demand Forecast Trend",
            "Total predicted demand across all SKUs."
        )

        if (
            not forecast_df.empty
            and "Date" in forecast_df.columns
            and "Predicted_Demand" in forecast_df.columns
        ):

            forecast_df["Date"] = pd.to_datetime(
                forecast_df["Date"]
            )

            daily_demand = (
                forecast_df
                .groupby("Date")["Predicted_Demand"]
                .sum()
                .reset_index()
            )

            fig = px.line(
                daily_demand,
                x="Date",
                y="Predicted_Demand",
                markers=True
            )

            fig.update_layout(
                template="plotly_white",
                hovermode="x unified",
                margin=dict(
                    l=20,
                    r=20,
                    t=20,
                    b=20
                ),
                xaxis_title="Date",
                yaxis_title="Predicted Demand"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        # ----------------------------------------------------
        # RISK
        # ----------------------------------------------------

        st.markdown("### ⚠️ Inventory Risk Analysis")

        c1, c2 = st.columns(2)

        with c1:

            section_header(
                "🔴 Stockout Risk",
                "SKUs that may run out of stock."
            )

            if "stockout_risk" in recommendation_df.columns:

                data = (
                    recommendation_df[
                        "stockout_risk"
                    ]
                    .astype(str)
                    .str.title()
                    .value_counts()
                    .reindex(
                        [
                            "High",
                            "Medium",
                            "Low"
                        ],
                        fill_value=0
                    )
                    .reset_index()
                )

                data.columns = [
                    "Risk",
                    "Count"
                ]

                fig = px.bar(
                    data,
                    x="Risk",
                    y="Count",
                    text="Count"
                )

                fig.update_layout(
                    template="plotly_white"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

        with c2:

            section_header(
                "🟠 Overstock Risk",
                "SKUs carrying excessive inventory."
            )

            if "overstock_risk" in recommendation_df.columns:

                data = (
                    recommendation_df[
                        "overstock_risk"
                    ]
                    .astype(str)
                    .str.title()
                    .value_counts()
                    .reindex(
                        [
                            "High",
                            "Medium",
                            "Low"
                        ],
                        fill_value=0
                    )
                    .reset_index()
                )

                data.columns = [
                    "Risk",
                    "Count"
                ]

                fig = px.bar(
                    data,
                    x="Risk",
                    y="Count",
                    text="Count"
                )

                fig.update_layout(
                    template="plotly_white"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


# ============================================================
# DEMAND FORECAST
# ============================================================

elif page == "Demand Forecast":

    section_header(
        "📈 Demand Forecast",
        "Analyze predicted demand by SKU and date range."
    )

    response = get_api_data(
        "/forecast?limit=10000"
    )

    if response:

        forecast_df = pd.DataFrame(
            response["data"]
        )

        if not forecast_df.empty:

            forecast_df["Date"] = pd.to_datetime(
                forecast_df["Date"]
            )

            st.markdown("### 🔎 Forecast Filters")

            f1, f2, f3 = st.columns(3)

            sku_list = sorted(
                forecast_df["SKU"]
                .dropna()
                .astype(str)
                .unique()
            )

            with f1:

                selected_sku = st.selectbox(
                    "SKU",
                    ["All"] + sku_list
                )

            min_date = forecast_df["Date"].min().date()
            max_date = forecast_df["Date"].max().date()

            with f2:

                start_date = st.date_input(
                    "Start Date",
                    value=min_date,
                    min_value=min_date,
                    max_value=max_date
                )

            with f3:

                end_date = st.date_input(
                    "End Date",
                    value=max_date,
                    min_value=min_date,
                    max_value=max_date
                )

            if start_date > end_date:

                st.error(
                    "Start Date cannot be greater than End Date."
                )

            else:

                filtered = forecast_df.copy()

                if selected_sku != "All":

                    filtered = filtered[
                        filtered["SKU"]
                        .astype(str)
                        == selected_sku
                    ]

                filtered = filtered[
                    (filtered["Date"].dt.date >= start_date)
                    &
                    (filtered["Date"].dt.date <= end_date)
                ]

                # ------------------------------------------------
                # KPI
                # ------------------------------------------------

                avg_demand = (
                    filtered["Predicted_Demand"].mean()
                    if not filtered.empty
                    else 0
                )

                total_demand = (
                    filtered["Predicted_Demand"].sum()
                    if not filtered.empty
                    else 0
                )

                c1, c2, c3 = st.columns(3)

                with c1:
                    kpi_card(
                        "Forecast Records",
                        f"{len(filtered):,}",
                        "📊"
                    )

                with c2:
                    kpi_card(
                        "Average Demand",
                        f"{avg_demand:,.2f}",
                        "📈"
                    )

                with c3:
                    kpi_card(
                        "Total Predicted Demand",
                        f"{total_demand:,.2f}",
                        "🎯"
                    )

                st.write("")

                # ------------------------------------------------
                # CHART
                # ------------------------------------------------

                section_header(
                    "📈 Predicted Demand",
                    "Demand forecast after applying the selected filters."
                )

                if not filtered.empty:

                    chart_df = (
                        filtered
                        .groupby("Date")[
                            "Predicted_Demand"
                        ]
                        .sum()
                        .reset_index()
                    )

                    fig = px.line(
                        chart_df,
                        x="Date",
                        y="Predicted_Demand",
                        markers=True
                    )

                    fig.update_layout(
                        template="plotly_white",
                        hovermode="x unified"
                    )

                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )

                else:

                    st.info(
                        "No forecast data available for selected filters."
                    )

                # ------------------------------------------------
                # TABLE
                # ------------------------------------------------

                section_header(
                    "📋 Forecast Data"
                )

                st.dataframe(
                    filtered,
                    use_container_width=True,
                    hide_index=True
                )


# ============================================================
# INVENTORY
# ============================================================

elif page == "Inventory":

    section_header(
        "📦 Inventory Management",
        "Monitor stock levels and incoming inventory."
    )

    response = get_api_data(
        "/inventory?limit=10000"
    )

    if response:

        inventory_df = pd.DataFrame(
            response["data"]
        )

        if not inventory_df.empty:

            inventory_df.columns = [
                str(col).lower()
                for col in inventory_df.columns
            ]

            # ------------------------------------------------
            # FILTER
            # ------------------------------------------------

            st.markdown("### 🔎 Inventory Filters")

            if "sku" in inventory_df.columns:

                sku_list = sorted(
                    inventory_df["sku"]
                    .dropna()
                    .astype(str)
                    .unique()
                )

                selected_sku = st.selectbox(
                    "Search / Select SKU",
                    ["All"] + sku_list
                )

            else:

                selected_sku = "All"

            filtered = inventory_df.copy()

            if (
                selected_sku != "All"
                and "sku" in filtered.columns
            ):

                filtered = filtered[
                    filtered["sku"]
                    .astype(str)
                    == selected_sku
                ]

            # ------------------------------------------------
            # KPI
            # ------------------------------------------------

            current_stock = (
                filtered["current_stock"].sum()
                if "current_stock" in filtered.columns
                else 0
            )

            on_order = (
                filtered["on_order"].sum()
                if "on_order" in filtered.columns
                else 0
            )

            c1, c2, c3 = st.columns(3)

            with c1:
                kpi_card(
                    "Inventory Records",
                    f"{len(filtered):,}",
                    "📦"
                )

            with c2:
                kpi_card(
                    "Current Stock",
                    f"{int(current_stock):,}",
                    "🏭"
                )

            with c3:
                kpi_card(
                    "On Order",
                    f"{int(on_order):,}",
                    "🚚"
                )

            st.write("")

            # ------------------------------------------------
            # CHARTS
            # ------------------------------------------------

            st.markdown("### 📊 Inventory Overview")

            c1, c2 = st.columns(2)

            with c1:

                section_header(
                    "Current Stock",
                    "Top 15 SKUs by current inventory."
                )

                if (
                    "sku" in filtered.columns
                    and "current_stock" in filtered.columns
                ):

                    stock = (
                        filtered
                        .groupby("sku")[
                            "current_stock"
                        ]
                        .sum()
                        .sort_values(
                            ascending=False
                        )
                        .head(15)
                        .reset_index()
                    )

                    fig = px.bar(
                        stock,
                        x="sku",
                        y="current_stock"
                    )

                    fig.update_layout(
                        template="plotly_white"
                    )

                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )

            with c2:

                section_header(
                    "On Order",
                    "Top 15 SKUs by incoming inventory."
                )

                if (
                    "sku" in filtered.columns
                    and "on_order" in filtered.columns
                ):

                    order = (
                        filtered
                        .groupby("sku")[
                            "on_order"
                        ]
                        .sum()
                        .sort_values(
                            ascending=False
                        )
                        .head(15)
                        .reset_index()
                    )

                    fig = px.bar(
                        order,
                        x="sku",
                        y="on_order"
                    )

                    fig.update_layout(
                        template="plotly_white"
                    )

                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )

            # ------------------------------------------------
            # TABLE
            # ------------------------------------------------

            section_header(
                "📋 Inventory Data"
            )

            st.dataframe(
                filtered,
                use_container_width=True,
                hide_index=True
            )


# ============================================================
# RECOMMENDATIONS
# ============================================================

elif page == "Recommendations":

    section_header(
        "🤖 AI Inventory Recommendations",
        "Prioritized inventory actions based on demand and risk signals."
    )

    response = get_api_data(
        "/recommendations?limit=10000"
    )

    if response:

        recommendation_df = pd.DataFrame(
            response["data"]
        )

        if not recommendation_df.empty:

            # ------------------------------------------------
            # FILTERS
            # ------------------------------------------------

            st.markdown("### 🔎 Recommendation Filters")

            f1, f2, f3 = st.columns(3)

            sku_list = sorted(
                recommendation_df["sku"]
                .dropna()
                .astype(str)
                .unique()
            )

            with f1:

                selected_sku = st.selectbox(
                    "SKU",
                    ["All"] + sku_list
                )

            with f2:

                stockout_filter = st.selectbox(
                    "Stockout Risk",
                    [
                        "All",
                        "High",
                        "Medium",
                        "Low"
                    ]
                )

            with f3:

                overstock_filter = st.selectbox(
                    "Overstock Risk",
                    [
                        "All",
                        "High",
                        "Medium",
                        "Low"
                    ]
                )

            # ------------------------------------------------
            # APPLY
            # ------------------------------------------------

            filtered = recommendation_df.copy()

            if selected_sku != "All":

                filtered = filtered[
                    filtered["sku"]
                    .astype(str)
                    == selected_sku
                ]

            if stockout_filter != "All":

                filtered = filtered[
                    filtered["stockout_risk"]
                    .astype(str)
                    .str.lower()
                    == stockout_filter.lower()
                ]

            if overstock_filter != "All":

                filtered = filtered[
                    filtered["overstock_risk"]
                    .astype(str)
                    .str.lower()
                    == overstock_filter.lower()
                ]

            # ------------------------------------------------
            # KPI
            # ------------------------------------------------

            high_stockout = (
                filtered["stockout_risk"]
                .astype(str)
                .str.lower()
                .eq("high")
                .sum()
            )

            high_overstock = (
                filtered["overstock_risk"]
                .astype(str)
                .str.lower()
                .eq("high")
                .sum()
            )

            c1, c2, c3 = st.columns(3)

            with c1:
                kpi_card(
                    "Recommendations",
                    f"{len(filtered):,}",
                    "🤖"
                )

            with c2:
                kpi_card(
                    "High Stockout",
                    f"{high_stockout:,}",
                    "🔴"
                )

            with c3:
                kpi_card(
                    "High Overstock",
                    f"{high_overstock:,}",
                    "🟠"
                )

            st.write("")

            # ------------------------------------------------
            # RISK CHARTS
            # ------------------------------------------------

            st.markdown("### ⚠️ Risk Analysis")

            c1, c2 = st.columns(2)

            with c1:

                stockout = (
                    filtered["stockout_risk"]
                    .astype(str)
                    .str.title()
                    .value_counts()
                    .reindex(
                        [
                            "High",
                            "Medium",
                            "Low"
                        ],
                        fill_value=0
                    )
                    .reset_index()
                )

                stockout.columns = [
                    "Risk",
                    "Count"
                ]

                fig = px.bar(
                    stockout,
                    x="Risk",
                    y="Count",
                    text="Count",
                    title="Stockout Risk Distribution"
                )

                fig.update_layout(
                    template="plotly_white"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            with c2:

                overstock = (
                    filtered["overstock_risk"]
                    .astype(str)
                    .str.title()
                    .value_counts()
                    .reindex(
                        [
                            "High",
                            "Medium",
                            "Low"
                        ],
                        fill_value=0
                    )
                    .reset_index()
                )

                overstock.columns = [
                    "Risk",
                    "Count"
                ]

                fig = px.bar(
                    overstock,
                    x="Risk",
                    y="Count",
                    text="Count",
                    title="Overstock Risk Distribution"
                )

                fig.update_layout(
                    template="plotly_white"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            # ------------------------------------------------
            # ACTION TABLE
            # ------------------------------------------------

            section_header(
                "🎯 Recommended Actions",
                "AI-generated actions for inventory planning."
            )

            display_columns = [
                "sku",
                "product_name",
                "predicted_demand",
                "current_stock",
                "stockout_risk",
                "overstock_risk",
                "priority",
                "health_level",
                "recommendation"
            ]

            available_columns = [
                col
                for col in display_columns
                if col in filtered.columns
            ]

            if not filtered.empty:

                st.dataframe(
                    filtered[available_columns],
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.info(
                    "No recommendations match the selected filters."
                )

