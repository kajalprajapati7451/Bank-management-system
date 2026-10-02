import html as _html

import streamlit as st
from main import Bank


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="NovaBank",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# HELPERS (UI ONLY - no backend logic)
# =========================================================

def esc(value):
    """Escape user / backend text so characters like & < > never break the HTML."""
    return _html.escape(str(value))


def h(markup):
    """Strip indentation + blank lines so Streamlit's markdown never
    turns indented HTML into a code block."""
    return "\n".join(
        line.strip() for line in markup.strip().splitlines() if line.strip()
    )


def render(markup):
    st.markdown(h(markup), unsafe_allow_html=True)


def page_header(icon, title, subtitle):
    render(f"""
    <div class="page-head">
        <div class="page-icon">{icon}</div>
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """)


def notice(kind, message):
    """kind: success | error | warning"""
    icons = {"success": "✓", "error": "!", "warning": "⚠"}
    render(f"""
    <div class="notice notice-{kind}">
        <span class="notice-icon">{icons[kind]}</span>
        <span class="notice-text">{esc(message)}</span>
    </div>
    """)


def section_label(number, title, caption=""):
    render(f"""
    <div class="form-section">
        <span class="form-section-badge">{number}</span>
        <div>
            <div class="form-section-title">{title}</div>
            <div class="form-section-caption">{caption}</div>
        </div>
    </div>
    """)


def bank_card(badge, title, number_label, number, rows, footnote=None):
    """One premium card design shared by Create Account and Account Details."""
    rows_html = "".join(
        f'<div class="bc-row"><div class="bc-label">{label}</div>'
        f'<div class="bc-value{" bc-value-lg" if big else ""}">{esc(value)}</div></div>'
        for label, value, big in rows
    )
    foot_html = f'<div class="bc-foot">{footnote}</div>' if footnote else ""
    render(f"""
    <div class="bank-card">
        <div class="bc-circle bc-c1"></div>
        <div class="bc-circle bc-c2"></div>
        <div class="bc-content">
            <div class="bc-top">
                <span class="bc-badge">{badge}</span>
                <span class="bc-brand">🏦 NovaBank</span>
            </div>
            <h2 class="bc-title">{title}</h2>
            <div class="bc-label">{number_label}</div>
            <div class="bc-number">{esc(number)}</div>
            <div class="bc-grid">{rows_html}</div>
            {foot_html}
        </div>
    </div>
    """)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');

:root {
    --navy: #0b1530;
    --navy-2: #12224f;
    --royal: #2563eb;
    --royal-dark: #1d4ed8;
    --sky: #60a5fa;
    --sky-soft: #dbeafe;
    --bg: #f4f7fc;
    --card: #ffffff;
    --line: #e2e8f0;
    --text: #0f172a;
    --muted: #64748b;
    --green: #16a34a;
    --green-soft: #ecfdf3;
    --red: #dc2626;
    --red-soft: #fef2f2;
    --amber-soft: #fffbeb;
    --radius: 20px;
    --shadow: 0 10px 30px rgba(15, 23, 42, 0.07);
    --shadow-lg: 0 18px 45px rgba(15, 23, 42, 0.12);
}

/* ---------- BASE ---------- */

html, body, .stApp, button, input, textarea, label {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.stApp {
    background:
        radial-gradient(900px 400px at 100% -5%, rgba(96, 165, 250, 0.16), transparent 60%),
        var(--bg);
}

header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

html, body { overflow-x: hidden; }


/* ---------- SIDEBAR ---------- */

section[data-testid="stSidebar"] {
    background: linear-gradient(185deg, #0b1530 0%, #12224f 60%, #1e3a8a 100%);
    border-right: 1px solid rgba(255, 255, 255, 0.06);
}

section[data-testid="stSidebar"] .block-container,
section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {
    padding-top: 1.5rem;
}

.side-brand {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 4px 6px 2px;
}

.side-logo {
    width: 44px;
    height: 44px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    background: linear-gradient(135deg, #3b82f6, #1d4ed8);
    box-shadow: 0 8px 20px rgba(37, 99, 235, 0.45);
}

.side-name {
    color: #fff;
    font-size: 22px;
    font-weight: 800;
    letter-spacing: -0.3px;
    line-height: 1.1;
}

.side-tag {
    color: #93a4c8;
    font-size: 12.5px;
    padding: 10px 6px 4px;
}

.side-divider {
    height: 1px;
    background: rgba(255, 255, 255, 0.1);
    margin: 18px 0;
}

.side-foot {
    color: #93a4c8;
    font-size: 13px;
    padding: 5px 6px;
}

section[data-testid="stSidebar"] div[role="radiogroup"] {
    gap: 6px;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label {
    width: 100%;
    padding: 12px 14px;
    border-radius: 12px;
    border: 1px solid transparent;
    cursor: pointer;
    transition: background 0.2s ease, transform 0.2s ease, border-color 0.2s ease;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label > div:first-child {
    display: none;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label p {
    color: #cbd5f5 !important;
    font-size: 15px;
    font-weight: 600;
    margin: 0;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background: rgba(255, 255, 255, 0.08);
    transform: translateX(3px);
}

section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.95), rgba(37, 99, 235, 0.9));
    border-color: rgba(255, 255, 255, 0.18);
    box-shadow: 0 8px 22px rgba(37, 99, 235, 0.4);
}

section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p {
    color: #ffffff !important;
}


/* ---------- HERO ---------- */

.hero {
    position: relative;
    overflow: hidden;
    border-radius: 28px;
    padding: 64px 52px;
    background: linear-gradient(135deg, #0b1530 0%, #1e40af 55%, #2563eb 100%);
    box-shadow: 0 24px 60px rgba(30, 64, 175, 0.32);
    color: #fff;
}

.orb { position: absolute; border-radius: 50%; pointer-events: none; }
.orb-1 { width: 380px; height: 380px; right: -90px; top: -120px;
         background: radial-gradient(circle, rgba(147, 197, 253, 0.55), transparent 68%); }
.orb-2 { width: 300px; height: 300px; left: -80px; bottom: -150px;
         background: radial-gradient(circle, rgba(59, 130, 246, 0.6), transparent 70%); }
.orb-3 { width: 150px; height: 150px; right: 38%; top: 12%;
         border: 1px solid rgba(255, 255, 255, 0.14); }
.orb-4 { width: 260px; height: 260px; right: 30%; bottom: -130px;
         border: 1px solid rgba(255, 255, 255, 0.1); }

.hero-inner {
    position: relative;
    z-index: 2;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 40px;
    flex-wrap: wrap;
}

.hero-copy { flex: 1 1 380px; min-width: 0; }

.brand-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.22);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    font-weight: 700;
    font-size: 15px;
}

.hero h1 {
    color: #fff;
    font-size: clamp(34px, 5.2vw, 58px);
    line-height: 1.06;
    font-weight: 800;
    letter-spacing: -1.5px;
    margin: 22px 0 16px;
    padding: 0;
}

.hero p {
    color: #dbe7ff;
    font-size: clamp(16px, 2vw, 19px);
    line-height: 1.65;
    max-width: 520px;
    margin: 0;
}

.hero-visual {
    position: relative;
    flex: 0 1 360px;
    height: 300px;
    min-width: 0;
}

.glass {
    position: absolute;
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.13);
    border: 1px solid rgba(255, 255, 255, 0.28);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    box-shadow: 0 18px 40px rgba(2, 6, 23, 0.28);
    color: #fff;
}

.glass-main { left: 0; top: 20px; width: 290px; max-width: 92%; padding: 24px; transform: rotate(-4deg); }
.glass-main small { color: #bcd2ff; font-size: 12.5px; font-weight: 600; }
.glass-main .amt { font-size: 32px; font-weight: 800; letter-spacing: -0.5px; margin: 6px 0 18px; }
.glass-main .chip { width: 42px; height: 30px; border-radius: 8px;
                    background: linear-gradient(135deg, #fde68a, #f59e0b); opacity: 0.9; }

.glass-note {
    right: 0; bottom: 14px;
    padding: 14px 18px;
    display: flex; align-items: center; gap: 12px;
    font-weight: 700; font-size: 14px;
    transform: rotate(3deg);
}

.glass-note .tick {
    width: 30px; height: 30px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    background: #22c55e; color: #fff; font-size: 15px;
}


/* ---------- CTA ROW (home) ---------- */

.cta-gap { height: 22px; }


/* ---------- SECTIONS ---------- */

.section-head { text-align: center; margin: 56px 0 28px; }
.section-head h2 { font-size: clamp(26px, 3.4vw, 36px); font-weight: 800; letter-spacing: -0.8px; color: var(--text); margin: 0 0 8px; padding: 0; }
.section-head p { color: var(--muted); font-size: 16px; margin: 0; }

.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(235px, 1fr));
    gap: 20px;
}

.feature {
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: var(--radius);
    padding: 28px 24px;
    box-shadow: var(--shadow);
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
}

.feature:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-lg);
    border-color: #bfdbfe;
}

.feature-icon {
    width: 54px; height: 54px;
    border-radius: 16px;
    display: flex; align-items: center; justify-content: center;
    font-size: 25px;
    background: linear-gradient(135deg, #eff6ff, var(--sky-soft));
    border: 1px solid #bfdbfe;
    margin-bottom: 18px;
}

.feature h3 { font-size: 18px; font-weight: 700; color: var(--text); margin: 0 0 8px; padding: 0; }
.feature p { font-size: 14.5px; line-height: 1.65; color: var(--muted); margin: 0; }


/* ---------- PAGE HEADER ---------- */

.page-head { text-align: center; margin: 6px auto 28px; max-width: 640px; }
.page-icon {
    width: 62px; height: 62px; margin: 0 auto 16px;
    border-radius: 20px;
    display: flex; align-items: center; justify-content: center;
    font-size: 28px;
    background: linear-gradient(135deg, #1e40af, #2563eb);
    box-shadow: 0 12px 28px rgba(37, 99, 235, 0.35);
}
.page-head h1 { font-size: clamp(27px, 4vw, 38px); font-weight: 800; letter-spacing: -1px; color: var(--text); margin: 0 0 8px; padding: 0; }
.page-head p { color: var(--muted); font-size: 16px; margin: 0; }


/* ---------- FORM CARD ---------- */

div[data-testid="stForm"] {
    max-width: 640px;
    margin: 0 auto;
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 24px;
    padding: 34px 32px 28px;
    box-shadow: var(--shadow-lg);
}

.form-section { display: flex; align-items: center; gap: 14px; margin: 4px 0 14px; }
.form-section-badge {
    width: 34px; height: 34px; flex: 0 0 34px;
    border-radius: 11px;
    display: flex; align-items: center; justify-content: center;
    background: var(--sky-soft); color: var(--royal-dark);
    font-weight: 800; font-size: 15px;
}
.form-section-title { font-weight: 700; font-size: 16.5px; color: var(--text); }
.form-section-caption { font-size: 13px; color: var(--muted); }
.form-divider { height: 1px; background: var(--line); margin: 22px 0; }


/* ---------- INPUTS ---------- */

[data-testid="stWidgetLabel"] p { color: #334155; font-weight: 600; font-size: 14.5px; }

div[data-baseweb="input"],
div[data-baseweb="base-input"] {
    border-radius: 12px !important;
    background: #f8fafc !important;
    border-color: var(--line) !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
}

div[data-baseweb="input"]:focus-within {
    border-color: var(--royal) !important;
    background: #ffffff !important;
    box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.14);
}

div[data-baseweb="input"] input { font-size: 15.5px; }


/* ---------- BUTTONS ---------- */

.stButton > button,
.stFormSubmitButton > button {
    border-radius: 14px;
    font-weight: 700;
    font-size: 16px;
    min-height: 52px;
    padding: 0 22px;
    transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    transform: translateY(-2px);
}

.stButton > button[kind="primary"],
.stFormSubmitButton > button[kind="primaryFormSubmit"],
.stButton > button[data-testid="stBaseButton-primary"],
.stFormSubmitButton > button[data-testid="stBaseButton-primaryFormSubmit"] {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: #fff;
    border: none;
    box-shadow: 0 10px 24px rgba(37, 99, 235, 0.35);
}

.stButton > button[kind="primary"]:hover,
.stFormSubmitButton > button[kind="primaryFormSubmit"]:hover,
.stButton > button[data-testid="stBaseButton-primary"]:hover,
.stFormSubmitButton > button[data-testid="stBaseButton-primaryFormSubmit"]:hover {
    box-shadow: 0 14px 30px rgba(37, 99, 235, 0.45);
    color: #fff;
}

.stButton > button[kind="secondary"],
.stButton > button[data-testid="stBaseButton-secondary"] {
    background: #fff;
    color: var(--royal-dark);
    border: 1.5px solid #bfdbfe;
    box-shadow: var(--shadow);
}

.stButton > button[kind="secondary"]:hover,
.stButton > button[data-testid="stBaseButton-secondary"]:hover {
    border-color: var(--royal);
    color: var(--royal-dark);
}

/* Delete page: the one place red is used on a button */
.st-key-delete_form .stFormSubmitButton > button {
    background: linear-gradient(135deg, #ef4444, #dc2626) !important;
    box-shadow: 0 10px 24px rgba(220, 38, 38, 0.3) !important;
    color: #fff !important;
}


/* ---------- NOTICES ---------- */

.notice {
    max-width: 640px;
    margin: 22px auto 0;
    display: flex;
    align-items: flex-start;
    gap: 14px;
    padding: 16px 20px;
    border-radius: 16px;
    border: 1px solid;
    animation: pop 0.35s ease;
}
.notice-icon {
    flex: 0 0 28px; width: 28px; height: 28px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-weight: 800; font-size: 14px; color: #fff;
}
.notice-text { font-weight: 600; font-size: 15px; line-height: 1.5; overflow-wrap: anywhere; }
.notice-success { background: var(--green-soft); border-color: #bbf7d0; color: #166534; }
.notice-success .notice-icon { background: var(--green); }
.notice-error { background: var(--red-soft); border-color: #fecaca; color: #991b1b; }
.notice-error .notice-icon { background: var(--red); }
.notice-warning { background: var(--amber-soft); border-color: #fde68a; color: #92400e; }
.notice-warning .notice-icon { background: #d97706; }

@keyframes pop {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
}


/* ---------- DANGER CARD ---------- */

.danger-card {
    max-width: 640px;
    margin: 0 auto 20px;
    display: flex;
    gap: 16px;
    align-items: flex-start;
    padding: 20px 22px;
    border-radius: 18px;
    background: var(--red-soft);
    border: 1px solid #fecaca;
}
.danger-icon {
    flex: 0 0 44px; width: 44px; height: 44px;
    border-radius: 14px; background: #fee2e2;
    display: flex; align-items: center; justify-content: center; font-size: 22px;
}
.danger-card strong { color: #991b1b; font-size: 16.5px; display: block; margin-bottom: 4px; }
.danger-card span { color: #b91c1c; font-size: 14px; line-height: 1.55; }


/* ---------- SUMMARY CARDS (account details) ---------- */

.summary-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
    margin: 26px 0 8px;
}

.summary {
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 22px;
    box-shadow: var(--shadow);
    display: flex;
    align-items: center;
    gap: 16px;
    min-width: 0;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.summary:hover { transform: translateY(-3px); box-shadow: var(--shadow-lg); }
.summary-icon {
    flex: 0 0 48px; width: 48px; height: 48px;
    border-radius: 14px; background: var(--sky-soft);
    display: flex; align-items: center; justify-content: center; font-size: 22px;
}
.summary-label { color: var(--muted); font-size: 13.5px; font-weight: 600; }
.summary-value { color: var(--text); font-size: 25px; font-weight: 800; letter-spacing: -0.5px; overflow-wrap: anywhere; }
.summary-value.ok { color: var(--green); }


/* ---------- PREMIUM BANK CARD (shared) ---------- */

.bank-card {
    position: relative;
    overflow: hidden;
    max-width: 640px;
    margin: 26px auto 0;
    border-radius: 28px;
    padding: 34px;
    color: #fff;
    background: linear-gradient(135deg, #0b1530 0%, #1e3a8a 55%, #2563eb 100%);
    border: 1px solid rgba(255, 255, 255, 0.14);
    box-shadow: 0 24px 55px rgba(30, 64, 175, 0.34);
}
.bc-circle { position: absolute; border-radius: 50%; pointer-events: none; }
.bc-c1 { width: 300px; height: 300px; right: -90px; top: -110px; background: radial-gradient(circle, rgba(147, 197, 253, 0.5), transparent 68%); }
.bc-c2 { width: 220px; height: 220px; left: -70px; bottom: -110px; border: 1px solid rgba(255, 255, 255, 0.14); }
.bc-content { position: relative; z-index: 2; }
.bc-top { display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap; margin-bottom: 22px; }
.bc-badge {
    padding: 7px 14px; border-radius: 999px;
    background: rgba(34, 197, 94, 0.2); border: 1px solid rgba(134, 239, 172, 0.5);
    color: #bbf7d0; font-size: 12.5px; font-weight: 700; letter-spacing: 0.8px;
}
.bc-brand { font-weight: 700; font-size: 15px; color: #dbe7ff; }
.bc-title { color: #fff; font-size: clamp(22px, 3.4vw, 30px); font-weight: 800; letter-spacing: -0.5px; margin: 0 0 24px; padding: 0; overflow-wrap: anywhere; }
.bc-label { font-size: 12px; font-weight: 600; letter-spacing: 1.2px; color: #a9c2f5; margin-bottom: 8px; }
.bc-number {
    font-family: 'JetBrains Mono', ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
    font-size: clamp(18px, 4.6vw, 28px);
    font-weight: 700;
    letter-spacing: 2px;
    padding: 16px 18px;
    border-radius: 16px;
    background: rgba(255, 255, 255, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.28);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    text-align: center;
    word-break: break-all;
    overflow-wrap: anywhere;
    margin-bottom: 26px;
}
.bc-grid { display: grid; grid-template-columns: 1fr; gap: 20px; }
.bc-value { font-size: 17px; font-weight: 600; overflow-wrap: anywhere; }
.bc-value-lg { font-size: clamp(28px, 5vw, 38px); font-weight: 800; letter-spacing: -1px; }
.bc-foot {
    margin-top: 26px; padding: 13px 16px; border-radius: 14px;
    background: rgba(251, 191, 36, 0.14); border: 1px solid rgba(251, 191, 36, 0.35);
    color: #fde68a; font-size: 14px; font-weight: 600; line-height: 1.5;
}


/* ---------- FOOTER ---------- */

.footer {
    text-align: center;
    background: #ffffff;
    border-top: 1px solid var(--line);
    border-radius: 24px 24px 0 0;
    padding: 38px 16px 30px;
    margin-top: 64px;
}
.footer .f-brand { font-size: 22px; font-weight: 800; color: var(--text); letter-spacing: -0.4px; }
.footer .f-tag { color: #334155; font-weight: 600; margin: 8px 0 4px; font-size: 15px; }
.footer .f-stack { color: var(--muted); font-size: 14px; }
.footer .f-copy { color: #94a3b8; font-size: 13px; margin-top: 14px; }


/* =====================================================
   RESPONSIVE
   ===================================================== */

@media (max-width: 992px) {
    .hero { padding: 48px 34px; }
    .hero-visual { flex: 1 1 100%; height: 250px; }
    .summary-grid { grid-template-columns: 1fr; }
}

@media (max-width: 768px) {
    .block-container { padding: 1rem 1rem 1.5rem !important; }

    .hero { padding: 36px 24px; border-radius: 22px; }
    .hero-visual { height: 230px; }
    .glass-main { width: 250px; padding: 20px; }
    .glass-main .amt { font-size: 27px; }

    div[data-testid="stForm"] { padding: 24px 18px 20px; border-radius: 20px; }

    /* force Streamlit columns into one column */
    div[data-testid="stHorizontalBlock"] { flex-wrap: wrap !important; gap: 0.75rem !important; }
    div[data-testid="stColumn"],
    div[data-testid="column"] {
        flex: 1 1 100% !important;
        width: 100% !important;
        min-width: 100% !important;
    }

    .stButton > button,
    .stFormSubmitButton > button { width: 100%; min-height: 54px; }

    .bank-card { padding: 26px 20px; border-radius: 22px; }
    .section-head { margin: 40px 0 22px; }
    .footer { margin-top: 44px; padding: 30px 12px 24px; }
}

@media (max-width: 480px) {
    .hero { padding: 28px 18px; }
    .hero h1 { letter-spacing: -0.8px; }
    .hero-visual { height: 210px; }
    .glass-main { width: 220px; }
    .glass-note { padding: 11px 14px; font-size: 13px; }

    .bc-number { letter-spacing: 1px; padding: 14px 10px; }
    .summary { padding: 18px; }
    .notice { padding: 14px 16px; }
    .danger-card { flex-direction: column; }
    .feature { padding: 24px 20px; }
}

@media (prefers-reduced-motion: reduce) {
    * { transition: none !important; animation: none !important; }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# BANK OBJECT
# =========================================================

bank = Bank()


# =========================================================
# SIDEBAR
# =========================================================

NAV_ITEMS = [
    "🏠 Home",
    "📝 Create Account",
    "💰 Deposit Money",
    "💸 Withdraw Money",
    "👤 Account Details",
    "✏️ Update Details",
    "🗑️ Delete Account"
]

if "nav" not in st.session_state:
    st.session_state.nav = NAV_ITEMS[0]


def go_to(page):
    st.session_state.nav = page


with st.sidebar:

    render("""
    <div class="side-brand">
        <div class="side-logo">🏦</div>
        <div class="side-name">NovaBank</div>
    </div>
    <div class="side-tag">Digital Banking Management System</div>
    <div class="side-divider"></div>
    """)

    st.radio(
        "Navigation",
        NAV_ITEMS,
        key="nav",
        label_visibility="collapsed"
    )

    render("""
    <div class="side-divider"></div>
    <div class="side-foot">🔐 Secure Banking</div>
    <div class="side-foot">🐍 Python + Streamlit</div>
    <div class="side-foot">💾 JSON Database</div>
    """)

option = st.session_state.nav


# =========================================================
# HOME
# =========================================================

if option == "🏠 Home":

    render("""
    <div class="hero">
        <div class="orb orb-1"></div>
        <div class="orb orb-2"></div>
        <div class="orb orb-3"></div>
        <div class="orb orb-4"></div>
        <div class="hero-inner">
            <div class="hero-copy">
                <div class="brand-pill">🏦 NovaBank</div>
                <h1>Smart Banking. Simple Experience.</h1>
                <p>Manage your accounts, deposits and withdrawals securely with NovaBank.</p>
            </div>
            <div class="hero-visual">
                <div class="glass glass-main">
                    <small>Available balance</small>
                    <div class="amt">₹24,580.00</div>
                    <div class="chip"></div>
                </div>
                <div class="glass glass-note">
                    <span class="tick">✓</span>
                    <span>Deposit successful</span>
                </div>
            </div>
        </div>
    </div>
    <div class="cta-gap"></div>
    """)

    cta1, cta2 = st.columns(2)

    with cta1:
        st.button(
            "🚀 Create Your Account",
            type="primary",
            use_container_width=True,
            on_click=go_to,
            args=("📝 Create Account",),
            key="cta_create"
        )

    with cta2:
        st.button(
            "💰 Manage Your Money",
            use_container_width=True,
            on_click=go_to,
            args=("💰 Deposit Money",),
            key="cta_money"
        )

    render("""
    <div class="section-head">
        <h2>Why Choose NovaBank?</h2>
        <p>Everything you need to manage your money, in one clean place.</p>
    </div>
    <div class="feature-grid">
        <div class="feature">
            <div class="feature-icon">🔐</div>
            <h3>Secure Banking</h3>
            <p>Your account information is protected with account number and PIN authentication.</p>
        </div>
        <div class="feature">
            <div class="feature-icon">⚡</div>
            <h3>Fast &amp; Simple</h3>
            <p>Perform banking operations quickly through a clean interface.</p>
        </div>
        <div class="feature">
            <div class="feature-icon">💰</div>
            <h3>Easy Money Management</h3>
            <p>Deposit and withdraw money with simple controls.</p>
        </div>
        <div class="feature">
            <div class="feature-icon">📊</div>
            <h3>Account Overview</h3>
            <p>View your account details and balance from one dashboard.</p>
        </div>
    </div>
    """)


# =========================================================
# CREATE ACCOUNT
# =========================================================

elif option == "📝 Create Account":

    page_header(
        "📝",
        "Create Your NovaBank Account",
        "Open your account in just a few seconds."
    )

    with st.form("create_account_form"):

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
                "👤 Full Name",
                placeholder="Enter your full name"
            )

            age = st.number_input(
                "🎂 Age",
                min_value=1,
                max_value=100,
                value=18
            )

        with col2:

            email = st.text_input(
                "📧 Email",
                placeholder="example@gmail.com"
            )

            pin = st.text_input(
                "🔐 Create 4-Digit PIN",
                type="password",
                max_chars=4
            )

        submitted = st.form_submit_button(
            "🚀 Create Account",
            type="primary",
            use_container_width=True
        )

    if submitted:

        if not name.strip():

            notice("error", "Please enter your name.")

        elif age < 18:

            notice("error", "You must be at least 18 years old.")

        elif not email.strip():

            notice("error", "Please enter your email.")

        elif not pin.isdigit():

            notice("error", "PIN must contain only numbers.")

        elif len(pin) != 4:

            notice("error", "PIN must contain exactly 4 digits.")

        else:

            success, result = bank.create_account(
                name=name.strip(),
                age=age,
                email=email.strip(),
                pin=int(pin)
            )

            if success:

                notice("success", "🎉 Account created successfully!")

                bank_card(
                    badge="✓ ACCOUNT CREATED",
                    title=f"Welcome, {esc(name)} 👋",
                    number_label="YOUR ACCOUNT NUMBER",
                    number=result,
                    rows=[("INITIAL BALANCE", "₹0.00", True)],
                    footnote="⚠️ Please save your account number safely."
                )

            else:

                notice("error", result)


# =========================================================
# DEPOSIT
# =========================================================

elif option == "💰 Deposit Money":

    page_header(
        "💰",
        "Deposit Money",
        "Add money securely to your NovaBank account."
    )

    with st.form("deposit_form"):

        account_number = st.text_input(
            "🏦 Account Number",
            placeholder="Enter account number"
        )

        pin = st.text_input(
            "🔐 PIN",
            type="password",
            max_chars=4
        )

        amount = st.number_input(
            "💵 Deposit Amount",
            min_value=0.0,
            step=100.0
        )

        submitted = st.form_submit_button(
            "💰 Deposit Money",
            type="primary",
            use_container_width=True
        )

    if submitted:

        if not account_number.strip():

            notice("error", "Please enter account number.")

        elif not pin.isdigit() or len(pin) != 4:

            notice("error", "Please enter a valid 4-digit PIN.")

        elif amount <= 0:

            notice("error", "Amount must be greater than ₹0.")

        else:

            success, message = bank.deposit_money(
                account_number.strip(),
                int(pin),
                amount
            )

            if success:

                notice("success", message)

            else:

                notice("error", message)


# =========================================================
# WITHDRAW
# =========================================================

elif option == "💸 Withdraw Money":

    page_header(
        "💸",
        "Withdraw Money",
        "Withdraw money securely from your account."
    )

    with st.form("withdraw_form"):

        account_number = st.text_input(
            "🏦 Account Number",
            placeholder="Enter account number"
        )

        pin = st.text_input(
            "🔐 PIN",
            type="password",
            max_chars=4
        )

        amount = st.number_input(
            "💵 Withdrawal Amount",
            min_value=0.0,
            step=100.0
        )

        submitted = st.form_submit_button(
            "💸 Withdraw Money",
            type="primary",
            use_container_width=True
        )

    if submitted:

        if not account_number.strip():

            notice("error", "Please enter account number.")

        elif not pin.isdigit() or len(pin) != 4:

            notice("error", "Please enter a valid 4-digit PIN.")

        elif amount <= 0:

            notice("error", "Amount must be greater than ₹0.")

        else:

            success, message = bank.withdraw_money(
                account_number.strip(),
                int(pin),
                amount
            )

            if success:

                notice("success", message)

            else:

                notice("error", message)


# =========================================================
# ACCOUNT DETAILS
# =========================================================

elif option == "👤 Account Details":

    page_header(
        "👤",
        "Account Details",
        "View your personal and account information securely."
    )

    with st.form("details_form"):

        account_number = st.text_input(
            "🏦 Account Number",
            placeholder="Enter account number"
        )

        pin = st.text_input(
            "🔐 PIN",
            type="password",
            max_chars=4
        )

        submitted = st.form_submit_button(
            "🔎 View Account",
            type="primary",
            use_container_width=True
        )

    if submitted:

        if not account_number.strip():

            notice("error", "Please enter account number.")

        elif not pin.isdigit() or len(pin) != 4:

            notice("error", "Please enter a valid 4-digit PIN.")

        else:

            user = bank.show_details(
                account_number.strip(),
                int(pin)
            )

            if user:

                notice("success", "Account verified successfully!")

                render(f"""
                <div class="summary-grid">
                    <div class="summary">
                        <div class="summary-icon">💰</div>
                        <div>
                            <div class="summary-label">Balance</div>
                            <div class="summary-value">₹{user['balance']:,.2f}</div>
                        </div>
                    </div>
                    <div class="summary">
                        <div class="summary-icon">🎂</div>
                        <div>
                            <div class="summary-label">Age</div>
                            <div class="summary-value">{esc(user['age'])}</div>
                        </div>
                    </div>
                    <div class="summary">
                        <div class="summary-icon">🏦</div>
                        <div>
                            <div class="summary-label">Status</div>
                            <div class="summary-value ok">Active</div>
                        </div>
                    </div>
                </div>
                """)

                bank_card(
                    badge="✓ VERIFIED",
                    title=esc(user['name']),
                    number_label="ACCOUNT NUMBER",
                    number=user['account no.'],
                    rows=[
                        ("EMAIL", f"📧 {user['email']}", False),
                        ("AVAILABLE BALANCE", f"₹{user['balance']:,.2f}", True),
                    ]
                )

            else:

                notice("error", "❌ Invalid account number or PIN.")


# =========================================================
# UPDATE DETAILS
# =========================================================

elif option == "✏️ Update Details":

    page_header(
        "✏️",
        "Update Details",
        "Change your name, email or PIN."
    )

    with st.form("update_form"):

        section_label("1", "🔐 Account Verification", "Confirm it's you before making changes.")

        account_number = st.text_input(
            "🏦 Account Number"
        )

        pin = st.text_input(
            "🔐 Current PIN",
            type="password",
            max_chars=4
        )

        render('<div class="form-divider"></div>')

        section_label("2", "📝 Update Information", "Leave a field empty to keep it unchanged.")

        new_name = st.text_input(
            "👤 New Name",
            placeholder="Leave empty to keep current name"
        )

        new_email = st.text_input(
            "📧 New Email",
            placeholder="Leave empty to keep current email"
        )

        new_pin = st.text_input(
            "🔐 New PIN",
            type="password",
            max_chars=4,
            placeholder="Leave empty to keep current PIN"
        )

        submitted = st.form_submit_button(
            "💾 Update Details",
            type="primary",
            use_container_width=True
        )

    if submitted:

        if not account_number.strip():

            notice("error", "Please enter account number.")

        elif not pin.isdigit() or len(pin) != 4:

            notice("error", "Please enter a valid current PIN.")

        elif new_pin and (
            not new_pin.isdigit()
            or len(new_pin) != 4
        ):

            notice("error", "New PIN must contain exactly 4 digits.")

        else:

            success, message = bank.update_details(
                account_number=account_number.strip(),
                pin=int(pin),
                name=new_name.strip() if new_name.strip() else None,
                email=new_email.strip() if new_email.strip() else None,
                new_pin=int(new_pin) if new_pin else None
            )

            if success:

                notice("success", message)

            else:

                notice("error", message)


# =========================================================
# DELETE ACCOUNT
# =========================================================

elif option == "🗑️ Delete Account":

    page_header(
        "🗑️",
        "Delete Account",
        "Permanently remove your NovaBank account."
    )

    render("""
    <div class="danger-card">
        <div class="danger-icon">⚠️</div>
        <div>
            <strong>Account deletion is permanent.</strong>
            <span>Your account and its data will be removed and cannot be recovered.</span>
        </div>
    </div>
    """)

    with st.form("delete_form"):

        account_number = st.text_input(
            "🏦 Account Number"
        )

        pin = st.text_input(
            "🔐 PIN",
            type="password",
            max_chars=4
        )

        confirmation = st.checkbox(
            "I understand that this account will be permanently deleted."
        )

        submitted = st.form_submit_button(
            "🗑️ Delete Account",
            type="primary",
            use_container_width=True
        )

    if submitted:

        if not confirmation:

            notice("warning", "Please confirm account deletion.")

        elif not pin.isdigit() or len(pin) != 4:

            notice("error", "Please enter a valid 4-digit PIN.")

        else:

            success, message = bank.delete_account(
                account_number.strip(),
                int(pin)
            )

            if success:

                notice("success", message)

                st.balloons()

            else:

                notice("error", message)


# =========================================================
# FOOTER
# =========================================================

render("""
<div class="footer">
    <div class="f-brand">🏦 NovaBank</div>
    <div class="f-tag">Smart • Secure • Simple Banking Management System</div>
    <div class="f-stack">Python • Streamlit • JSON</div>
    <div class="f-copy">Secure Banking Management System © 2026</div>
</div>
""")