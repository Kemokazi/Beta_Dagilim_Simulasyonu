import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta, norm

# Hacettepe Üniversitesi logosunu yükleme (logonun URL'sini veya dosya yolunu değiştirin)
st.image(
    "https://kkm.hacettepe.edu.tr/wp-content/uploads/2018/07/cropped-logo-hacettepe.png",
    width=100,
)

st.markdown(
    """
    <h1 style="text-align: center; font-size: 30px; color: darkblue;">Hacettepe Üniversitesi</h1>
    <h2 style="text-align: center; font-size: 25px; color: darkblue;">İstatistik Bölümü IST631 Kuramsal İstatistik</h2>
    <h3 style="text-align: center; font-size: 20px; color: black;">Merkezi Limit Teoremi: Beta Dağılımı Dinamik Simülasyonu</h3>
    <h4 style="text-align: center; font-size: 18px; color: black;">Kemal Sözer</h4>
    """,
    unsafe_allow_html=True,
)

# Parametre Girişleri
alpha = st.slider("Alpha (α) Parametresi", 0.5, 10.0, 2.0, 0.1)
beta_param = st.slider("Beta (β) Parametresi", 0.5, 10.0, 5.0, 0.1)
n = st.slider("Örneklem Büyüklüğü (n)", 5, 500, 30, 5)
num_samples = st.slider("Örnek Sayısı", 100, 10000, 1000, 100)

# Simülasyon ve Grafik
def beta_clt_simulation(alpha, beta_param, n, num_samples):
    # Örneklem Ortalamalarını Hesaplama
    sample_means = [np.mean(beta.rvs(alpha, beta_param, size=n)) for _ in range(num_samples)]
    
    # Grafik
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(sample_means, bins=30, density=True, alpha=0.6, color='blue', label="Örneklem Ortalamaları")
    
    # Teorik Normal Dağılım
    mu = alpha / (alpha + beta_param)
    sigma = np.sqrt((alpha * beta_param) / ((alpha + beta_param)**2 * (alpha + beta_param + 1)))
    norm_dist = norm(loc=mu, scale=sigma / np.sqrt(n))
    x = np.linspace(min(sample_means), max(sample_means), 100)
    ax.plot(x, norm_dist.pdf(x), color='red', label="Teorik Normal Dağılım")
    
    # Grafik Özelleştirme
    ax.set_title(f"CLT Simülasyonu (n={n}, α={alpha}, β={beta_param}, Örnek Sayısı={num_samples})")
    ax.set_xlabel("Örneklem Ortalaması")
    ax.set_ylabel("Yoğunluk")
    ax.legend()
    ax.grid()

    return fig

# Grafik Çizimi
fig = beta_clt_simulation(alpha, beta_param, n, num_samples)
st.pyplot(fig)
