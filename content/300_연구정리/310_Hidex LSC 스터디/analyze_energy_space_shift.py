import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path

def ch_to_energy(ch):
    """Hidex log-amp formula: E = 10^((Ch+173)/362) - 3 [keV]"""
    return 10**((np.asarray(ch, dtype=float) + 173) / 362) - 3

def main():
    # 1. Load Data
    csv_path = Path("analysis/peak_parameters.csv")
    if not csv_path.exists():
        print(f"[ERROR] {csv_path} not found.")
        return
    
    df = pd.read_csv(csv_path)
    
    # 2. Energy Space Transformation
    # Convert QPE Channel to QPE Energy
    df['QPE_E'] = ch_to_energy(df['QPE'])
    
    regions = ["Pb210", "Po210", "BG"]
    # Only local_max as requested
    for r in regions:
        df[f"{r}_max_E"] = ch_to_energy(df[f"{r}_max"])

    # 3. Create Visualization (3 Subplots)
    fig = make_subplots(
        rows=3, cols=1,
        subplot_titles=(
            "Pb-210 Region: Local Max Energy vs QPE",
            "Po-210 Region: Local Max Energy vs QPE",
            "Background Region: Local Max Energy vs QPE (Sample vs Blank)"
        ),
        vertical_spacing=0.1
    )
    
    # Representative colors for REPs
    reps = sorted(df['Rep'].dropna().unique())
    colors_rep = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
    rep_color_map = dict(zip(reps, colors_rep))
    
    results_md = []

    for i, r in enumerate(regions):
        row = i + 1
        col_e = f"{r}_max_E"
        
        if r == "BG":
            # Distinct symbols for Sample vs Blank, colors for REPs
            for rep in reps:
                # Sample
                sdf = df[(~df['Is_Blank']) & (df['Rep'] == rep)].dropna(subset=['QPE_E', col_e])
                if not sdf.empty:
                    fig.add_trace(go.Scatter(
                        x=sdf['QPE_E'], y=sdf[col_e],
                        mode='markers',
                        name=f"Sample {rep}",
                        marker=dict(color=rep_color_map[rep], symbol='circle', size=8),
                        legendgroup=f"Sample_{rep}",
                        hovertemplate=f"Sample {rep}<br>QPE: %{{x:.2f}} keV<br>{r} max: %{{y:.2f}} keV<extra></extra>"
                    ), row=row, col=1)
                
                # Blank
                bdf = df[(df['Is_Blank']) & (df['Rep'] == rep)].dropna(subset=['QPE_E', col_e])
                if not bdf.empty:
                    fig.add_trace(go.Scatter(
                        x=bdf['QPE_E'], y=bdf[col_e],
                        mode='markers',
                        name=f"Blank {rep}",
                        marker=dict(color=rep_color_map[rep], symbol='x', size=8),
                        legendgroup=f"Blank_{rep}",
                        hovertemplate=f"Blank {rep}<br>QPE: %{{x:.2f}} keV<br>{r} max: %{{y:.2f}} keV<extra></extra>"
                    ), row=row, col=1)
            
            # Regression lines for groups
            group_configs = [
                (df[~df['Is_Blank']], "Sample", "blue", "solid"),
                (df[df['Is_Blank']], "Blank", "red", "dash"),
                (df, "All (Sample+Blank)", "black", "dot")
            ]
            for sub_df, label, color, dash in group_configs:
                valid = sub_df.dropna(subset=['QPE_E', col_e])
                if len(valid) >= 2:
                    slope, intercept = np.polyfit(valid['QPE_E'], valid[col_e], 1)
                    p = np.poly1d([slope, intercept])
                    x_range = np.array([valid['QPE_E'].min(), valid['QPE_E'].max()])
                    r2 = 1 - (np.sum((valid[col_e] - p(valid['QPE_E']))**2) / np.sum((valid[col_e] - valid[col_e].mean())**2))
                    
                    fig.add_trace(go.Scatter(
                        x=x_range, y=p(x_range),
                        mode='lines',
                        name=f"{label} Fit (slope={slope:.4f}, R²={r2:.3f})",
                        line=dict(color=color, dash=dash, width=2),
                        hoverinfo='skip'
                    ), row=row, col=1)
                    results_md.append({'region': r, 'group': label, 'slope': slope, 'intercept': intercept, 'r2': r2})

        else:
            # Pb210 and Po210 (Sample only)
            for rep in reps:
                sdf = df[(~df['Is_Blank']) & (df['Rep'] == rep)].dropna(subset=['QPE_E', col_e])
                if not sdf.empty:
                    fig.add_trace(go.Scatter(
                        x=sdf['QPE_E'], y=sdf[col_e],
                        mode='markers',
                        name=f"Sample {rep}",
                        marker=dict(color=rep_color_map[rep], symbol='circle', size=8),
                        legendgroup=f"Sample_{rep}",
                        hovertemplate=f"Sample {rep}<br>QPE: %{{x:.2f}} keV<br>{r} max: %{{y:.2f}} keV<extra></extra>"
                    ), row=row, col=1)
            
            valid = df[~df['Is_Blank']].dropna(subset=['QPE_E', col_e])
            if len(valid) >= 2:
                slope, intercept = np.polyfit(valid['QPE_E'], valid[col_e], 1)
                p = np.poly1d([slope, intercept])
                x_range = np.array([valid['QPE_E'].min(), valid['QPE_E'].max()])
                r2 = 1 - (np.sum((valid[col_e] - p(valid['QPE_E']))**2) / np.sum((valid[col_e] - valid[col_e].mean())**2))
                
                fig.add_trace(go.Scatter(
                    x=x_range, y=p(x_range),
                    mode='lines',
                    name=f"Sample Fit (slope={slope:.4f}, R²={r2:.3f})",
                    line=dict(color="black", dash="dash", width=2),
                    hoverinfo='skip'
                ), row=row, col=1)
                results_md.append({'region': r, 'group': 'Sample', 'slope': slope, 'intercept': intercept, 'r2': r2})

        # X-axis ticks with Energy & Channel
        # Pick 10 representative points for ticks
        valid_qpe = df.dropna(subset=['QPE', 'QPE_E']).sort_values('QPE_E')
        if not valid_qpe.empty:
            indices = np.linspace(0, len(valid_qpe)-1, 10, dtype=int)
            tick_df = valid_qpe.iloc[indices]
            fig.update_xaxes(
                tickvals=tick_df['QPE_E'],
                ticktext=[f"{e:.1f}keV<br>({ch:.0f}ch)" for e, ch in zip(tick_df['QPE_E'], tick_df['QPE'])],
                title_text="QPE (Energy & Original Channel)",
                row=row, col=1
            )
        fig.update_yaxes(title_text=f"{r} Peak Energy (keV)", row=row, col=1)

    fig.update_layout(
        height=1200,
        title_text="Energy Space Analysis: Local Max Energy vs QPE (REP Distinguished)",
        template="plotly_white",
        hovermode="closest"
    )

    # 4. Save Report
    output_dir = Path("analysis")
    output_dir.mkdir(exist_ok=True)
    report_path = output_dir / "260422_energy_space_shift_report.html"
    fig.write_html(str(report_path))
    print(f"[SUCCESS] Energy space shift report generated: {report_path}")

    # 5. Generate Findings MD (Theoretical vs Actual)
    findings_path = output_dir / "260422_energy_space_findings.md"
    with open(findings_path, "w", encoding="utf-8") as f:
        f.write("# 에너지 공간 시프트 경험식 필요성 검토 보고서\n\n")
        f.write("**생성**: analyze_energy_space_shift.py (2026-04-22)\n\n")
        f.write("## 1. 분석 개요\n")
        f.write("- **목적**: LSC의 기존 채널-에너지 환산식(`E = 10^((Ch+173)/362) - 3`)을 적용하여 에너지 공간으로 매핑했을 때, 각 Peak(local maximum)의 에너지 시프트가 QPE 에너지 감소에 비례하는지 검증.\n")
        f.write("- **데이터**: `max` (local maximum) 기준만 표시, REP별 구분, X축에 QPE 채널 병기.\n\n")
        
        f.write("## 2. 기존 환산식 기반 예상값 대비 실제 변동값 비교\n")
        f.write("선형 퀜칭 모델($E' = E/k$)이 환산식과 완전히 부합한다면, 피크 에너지는 QPE 에너지에 정비례해야 합니다.\n")
        f.write("- 이론적 모델: $E_{peak} = (E_{peak,ref} / E_{QPE,ref}) \\times E_{QPE}$\n")
        f.write("- 즉, Y절편(Intercept)은 0에 가까워야 하며, 기울기(Slope)는 기준 샘플의 비율($E_{peak,ref} / E_{QPE,ref}$)과 일치해야 합니다.\n\n")
        
        f.write("### [회귀 분석 결과 및 이론 비교]\n")
        f.write("| Region | Group | Actual Slope | Expected Slope | Diff (%) | Actual Intercept | R² |\n")
        f.write("|---|---|---|---|---|---|---|\n")
        
        for res in results_md:
            r = res['region']
            group = res['group']
            actual_slope = res['slope']
            actual_intercept = res['intercept']
            r2 = res['r2']
            
            # Reference Sample A01 (for Pb210, Po210) or B01 (for BG)
            ref_vial = 'B01' if r == 'BG' else 'A01'
            ref_df = df[df['Vial'] == ref_vial].dropna(subset=[f"{r}_max_E", 'QPE_E'])
            
            if not ref_df.empty:
                ref_peak_e = ref_df[f"{r}_max_E"].median()
                ref_qpe_e = ref_df['QPE_E'].median()
                expected_slope = ref_peak_e / ref_qpe_e if ref_qpe_e > 0 else 0
                diff_pct = (actual_slope - expected_slope) / expected_slope * 100 if expected_slope > 0 else 0
            else:
                expected_slope = 0
                diff_pct = 0
                
            f.write(f"| {r} | {group} | {actual_slope:.4f} | {expected_slope:.4f} | {diff_pct:+.2f}% | {actual_intercept:.2f} | {r2:.3f} |\n")
        
        f.write("\n## 3. 경험식 필요성 검토 및 결론\n")
        f.write("위 표의 실제 기울기와 Y절편을 이론적 예상치와 비교하면 다음을 알 수 있습니다:\n")
        f.write("1. **선형성(R²)**: 에너지 공간에서의 R² 값이 높다면, QPE 에너지와 피크 에너지는 강한 선형 관계를 가집니다.\n")
        f.write("2. **기울기 편향 (Diff %)**: 실제 기울기가 이론적 비율에서 크게 벗어난다면, 단순 비례 축소 모델($E/k$)만으로는 설명할 수 없는 추가적인 에너지 의존적 왜곡이 존재함을 의미합니다.\n")
        f.write("3. **경험식 도출 필요성**: 절편(Intercept)이 0에서 크게 벗어나거나 기울기 편향이 유의미하다면, $E' = E/k + \\delta$와 같은 **수정 경험식(Empirical Formula)**이나 이전에 검토했던 **TDCR 기반의 Zero-channel Offset 모델**을 다시 도입하여 물리적 오차를 보정해야 할 타당한 근거가 됩니다.\n")

    print(f"[SUCCESS] Findings summary generated: {findings_path}")

if __name__ == "__main__":
    main()
