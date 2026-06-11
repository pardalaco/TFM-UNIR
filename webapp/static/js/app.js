// Etiquetas mostradas en la barra de progreso, una por fase del pipeline.
// El índice (1-based) se corresponde con el "step" que devuelve /status.
const STEPS = [
  "Ejecutando Slither...",
  "Ejecutando Mythril...",
  "Normalizando resultados...",
  "Correlacionando hallazgos...",
  "Generando wrapper Echidna...",
  "Ejecutando Echidna (fuzzing)...",
  "Generando informe...",
];

let pollInterval = null;
let currentReport = null;
let currentJobId = null;

// ── Modal de ayuda ──
function openHelp() {
  document.getElementById('help-modal').classList.add('active');
}
function closeHelp() {
  document.getElementById('help-modal').classList.remove('active');
}
// Cierra el modal al hacer click en el overlay, pero no en su contenido.
document.getElementById('help-modal').addEventListener('click', e => {
  if (e.target.id === 'help-modal') closeHelp();
});

async function downloadReport() {
  if (!currentJobId) return;
  const name = (currentReport && currentReport.meta && currentReport.meta.contract) || 'reporte';
  const res = await fetch(`/result/${currentJobId}/pdf`);
  if (!res.ok) { alert('No se pudo generar el PDF del informe.'); return; }
  const blob = await res.blob();
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `${name}_report.pdf`;
  a.click();
  URL.revokeObjectURL(url);
}

function switchTab(tab) {
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
  document.querySelector(`.tab:nth-child(${tab === 'file' ? 1 : 2})`).classList.add('active');
  document.getElementById(`panel-${tab}`).classList.add('active');
}

// ── Subida de contrato (drag & drop o selector de archivo) ──
const dz = document.getElementById('drop-zone');
dz.addEventListener('dragover', e => { e.preventDefault(); dz.classList.add('drag'); });
dz.addEventListener('dragleave', () => dz.classList.remove('drag'));
dz.addEventListener('drop', e => {
  e.preventDefault(); dz.classList.remove('drag');
  const f = e.dataTransfer.files[0];
  if (f && f.name.endsWith('.sol')) uploadFile(f);
});
document.getElementById('file-input').addEventListener('change', e => {
  if (e.target.files[0]) uploadFile(e.target.files[0]);
});

async function uploadFile(file) {
  showProgress(file.name);
  const form = new FormData();
  form.append('file', file);
  const res = await fetch('/analyze', { method: 'POST', body: form });
  const { job_id } = await res.json();
  currentJobId = job_id;
  pollInterval = setInterval(() => poll(job_id), 2000);
}

async function analyzeCode() {
  const code = document.getElementById('code-editor').value.trim();
  const name = document.getElementById('code-name').value.trim() || 'MiContrato';
  if (!code) { alert('Pega el código Solidity antes de analizar.'); return; }
  showProgress(name + '.sol');
  const res = await fetch('/analyze-code', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ code, contract_name: name }),
  });
  const { job_id } = await res.json();
  currentJobId = job_id;
  pollInterval = setInterval(() => poll(job_id), 2000);
}

function showProgress(name) {
  document.getElementById('home-section').querySelector('.tabs-wrap').style.display = 'none';
  document.getElementById('progress-section').style.display = 'block';
  document.getElementById('prog-name').textContent = name;
  renderSteps(0);
}

// ── Polling de progreso y resultados ──
async function poll(job_id) {
  const res = await fetch(`/status/${job_id}`);
  const data = await res.json();
  const pct = Math.round((data.step / data.total) * 100);
  document.getElementById('prog-bar').style.width = pct + '%';
  document.getElementById('prog-pct').textContent = pct + '%';
  renderSteps(data.step);
  if (data.status === 'done') {
    clearInterval(pollInterval);
    const r = await (await fetch(`/result/${job_id}`)).json();
    showResults(r);
  } else if (data.status === 'error') {
    clearInterval(pollInterval);
    showError(data.error);
  }
}

function renderSteps(cur) {
  document.getElementById('prog-steps').innerHTML = STEPS.map((s, i) => {
    const n = i + 1;
    const cls = n < cur ? 'done' : n === cur ? 'active' : '';
    const ic  = n < cur ? '✓' : n === cur ? '↻' : '·';
    return `<div class="step-row ${cls}"><div class="step-icon">${ic}</div>${s}</div>`;
  }).join('');
}

function showResults(report) {
  currentReport = report;
  document.getElementById('home-section').style.display = 'none';
  document.getElementById('results-section').style.display = 'block';
  const s = report.summary;
  const score = s.risk_score;
  const color = score >= 7 ? '#f87171' : score >= 4 ? '#fbbf24' : '#4ade80';
  const circle = document.getElementById('score-circle');
  circle.style.borderColor = color;
  document.getElementById('score-num').textContent = score;
  document.getElementById('score-num').style.color = color;
  document.getElementById('res-contract-name').textContent = report.meta.contract + '.sol';
  document.getElementById('res-risk-label').textContent =
    score >= 7 ? '🔴 Riesgo Alto — Requiere atención inmediata' :
    score >= 4 ? '🟠 Riesgo Medio — Revisar antes del despliegue' :
                 '🟢 Riesgo Bajo — Sin vulnerabilidades críticas';
  document.getElementById('res-date').textContent = new Date().toLocaleDateString('es-ES');
  document.getElementById('st-total').textContent = s.total_findings;
  document.getElementById('st-confirmed').textContent = s.confirmed;
  document.getElementById('st-high').textContent = s.high_severity;

  document.getElementById('findings-body').innerHTML = report.findings.map(f => {
    const sc = f.severity === 'high' ? 'sev-high' : f.severity === 'medium' ? 'sev-medium' : 'sev-low';
    const st = f.status === 'confirmed' ? 'st-confirmed' : 'st-detected';
    const stars = '★'.repeat(f.confidence_score) + '☆'.repeat(3 - f.confidence_score);
    return `<tr>
      <td><code>${f.function}()</code></td>
      <td style="color:#818cf8">${f.swc_id}</td>
      <td>${f.vuln_type}</td>
      <td><span class="badge ${sc}">${f.severity.toUpperCase()}</span></td>
      <td><span class="stars">${stars}</span> <span style="color:#64748b">${f.confidence_score}/3</span></td>
      <td><span class="badge ${st}">${f.status}</span></td>
    </tr>`;
  }).join('') || '<tr><td colspan="6" style="text-align:center;padding:2rem;color:#374151">No se detectaron vulnerabilidades</td></tr>';

  document.getElementById('echidna-body').innerHTML = (report.echidna_results || []).map(r => {
    const res = r.echidna_status === 'passed'  ? '<span style="color:#4ade80">✅ passed</span>' :
                r.echidna_status === 'failed'  ? '<span style="color:#f87171">❌ failed</span>' :
                !r.echidna_testable            ? '<span style="color:#fbbf24">⚠ no testable automáticamente</span>' :
                                                 `<span style="color:#64748b">— ${r.echidna_status}</span>`;
    return `<tr>
      <td><code>${r.function}()</code></td>
      <td style="color:#818cf8">${r.swc_id}</td>
      <td>${r.echidna_testable ? 'Sí' : '<span style="color:#fbbf24">No</span>'}</td>
      <td>${res}</td>
    </tr>`;
  }).join('') || '<tr><td colspan="4" style="text-align:center;padding:2rem;color:#374151">Sin resultados de Echidna</td></tr>';
}

function showError(msg) {
  document.getElementById('home-section').style.display = 'none';
  document.getElementById('error-section').style.display = 'block';
  document.getElementById('error-msg').textContent = msg;
}

function reset() {
  document.getElementById('home-section').style.display = 'flex';
  document.getElementById('home-section').querySelector('.tabs-wrap').style.display = 'block';
  document.getElementById('progress-section').style.display = 'none';
  document.getElementById('results-section').style.display = 'none';
  document.getElementById('error-section').style.display = 'none';
  document.getElementById('file-input').value = '';
  document.getElementById('prog-bar').style.width = '0%';
}
