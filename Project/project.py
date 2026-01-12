import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =====================
# PAGE CONFIG
# =====================
st.set_page_config(
    page_title="Analisis Kinerja Akademik Siswa",
    layout="wide"
)

# =====================
# LOAD DATA
# =====================
@st.cache_data
def load_data():
    return pd.read_csv("performa_siswa.csv", sep=";")  # sesuaikan nama file CSV

df = load_data()


# =====================
# TITLE
# =====================
st.title("Analisis Perbedaan Kinerja Akademik Siswa")
st.subheader("Berdasarkan Jenis Sekolah (Negeri dan Swasta)")
st.write(
    "Dashboard ini menyajikan analisis perbedaan kinerja akademik siswa "
    "berdasarkan jenis sekolah menggunakan visualisasi dasar."
)

# =====================
# SIDEBAR FILTER
# =====================
st.sidebar.header("Filter Data")

school_filter = st.sidebar.multiselect(
    "Jenis Sekolah",
    df["school_type"].unique(),
    df["school_type"].unique()
)

gender_filter = st.sidebar.multiselect(
    "Gender",
    df["gender"].unique(),
    df["gender"].unique()
)


filtered_df = df[
    (df["school_type"].isin(school_filter)) &
    (df["gender"].isin(gender_filter))
]

# =====================
# KPI
# =====================
col1, col2, col3 = st.columns(3)

col1.metric("Jumlah Siswa", len(filtered_df))
col2.metric("Rata-rata Overall Score", round(filtered_df["overall_score"].mean(), 2))
col3.metric("Rata-rata Jam Belajar", round(filtered_df["study_hours"].mean(), 2))

st.divider()

# =====================
# VISUAL 1: BAR CHART
# =====================
st.subheader("Rata-rata Overall Score per Jenis Sekolah")

avg_score = filtered_df.groupby("school_type")["overall_score"].mean()

fig, ax = plt.subplots()
avg_score.plot(kind="bar", ax=ax)
ax.set_xlabel("Jenis Sekolah")
ax.set_ylabel("Rata-rata Overall Score")
ax.set_title("Rata-rata Kinerja Akademik Siswa")

st.pyplot(fig)
st.caption("Insight: Terdapat perbedaan rata-rata kinerja akademik antara sekolah negeri dan swasta.")

# =====================
# VISUAL 2: BOXPLOT
# =====================
st.subheader("Distribusi Overall Score")

fig, ax = plt.subplots()
filtered_df.boxplot(column="overall_score", by="school_type", ax=ax)
ax.set_xlabel("Jenis Sekolah")
ax.set_ylabel("Overall Score")
ax.set_title("Distribusi Overall Score Berdasarkan Jenis Sekolah")
plt.suptitle("")

st.pyplot(fig)
st.caption("Insight: Boxplot menunjukkan perbedaan median dan sebaran nilai antar jenis sekolah.")

# =====================
# VISUAL 3: SCATTER PLOT
# =====================
st.subheader("Jam Belajar vs Kinerja Akademik")

fig, ax = plt.subplots()
for school in filtered_df["school_type"].unique():
    subset = filtered_df[filtered_df["school_type"] == school]
    ax.scatter(subset["study_hours"], subset["overall_score"], label=school)

ax.set_xlabel("Jam Belajar")
ax.set_ylabel("Overall Score")
ax.set_title("Hubungan Jam Belajar dengan Kinerja Akademik")
ax.legend()

st.pyplot(fig)
st.caption("Insight: Jam belajar yang lebih tinggi cenderung diikuti kinerja akademik yang lebih baik.")

# =====================
# VISUAL 4: HISTOGRAM
# =====================
st.subheader("Distribusi Overall Score")

fig, ax = plt.subplots()
ax.hist(filtered_df["overall_score"], bins=20)
ax.set_xlabel("Overall Score")
ax.set_ylabel("Jumlah Siswa")
ax.set_title("Distribusi Nilai Overall Score")

st.pyplot(fig)
st.caption("Insight: Sebaran nilai akademik siswa menunjukkan variasi performa.")

# =====================
# VISUAL 5: PIE CHART
# =====================
st.subheader("Proporsi Siswa Berdasarkan Jenis Sekolah")

school_count = filtered_df["school_type"].value_counts()

fig, ax = plt.subplots()
ax.pie(
    school_count,
    labels=school_count.index,
    autopct="%1.1f%%",
    startangle=90
)
ax.set_title("Proporsi Siswa Negeri dan Swasta")

st.pyplot(fig)
st.caption("Insight: Komposisi siswa berdasarkan jenis sekolah.")

# =====================
# VISUAL 6: HEATMAP (MATPLOTLIB)
# =====================
st.subheader("Korelasi Variabel Akademik")

corr_cols = [
    "math_score",
    "science_score",
    "english_score",
    "overall_score",
    "study_hours",
    "attendance_percentage"
]

corr = filtered_df[corr_cols].corr()

fig, ax = plt.subplots()
cax = ax.matshow(corr)
fig.colorbar(cax)

ax.set_xticks(range(len(corr_cols)))
ax.set_yticks(range(len(corr_cols)))
ax.set_xticklabels(corr_cols, rotation=45, ha="left")
ax.set_yticklabels(corr_cols)

st.pyplot(fig)
st.caption("Insight: Overall score memiliki korelasi kuat dengan nilai mata pelajaran dan kehadiran.")

