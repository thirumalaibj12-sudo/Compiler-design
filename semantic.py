<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Syntax Analyzer — Simulation</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    :root {
      --bg: #0f172a; --card: #1e293b; --border: #1f2937;
      --accent: #38bdf8; --accent2: #22d3ee; --text: #e5e7eb; --muted: #94a3b8;
      --shadow: 0 12px 40px rgba(0,0,0,0.4);
    }
    * { box-sizing: border-box; margin:0; padding:0; }
    body {
      font-family: "Inter", "Segoe UI", system-ui, sans-serif;
      background:
        radial-gradient(circle at 15% 15%, rgba(34,211,238,0.08), transparent 30%),
        radial-gradient(circle at 85% 5%, rgba(56,189,248,0.07), transparent 30%),
        var(--bg);
      color: var(--text);
      min-height: 100vh; padding: 28px 16px 40px;
    }
    .page { max-width: 1280px; margin: 0 auto; }

    /* ── HEADER ── */
    header { text-align: center; margin-bottom: 24px; }
    .pill {
      display: inline-flex; align-items: center; gap: 8px;
      padding: 7px 16px; border-radius: 999px;
      background: linear-gradient(90deg, rgba(34,211,238,.14), rgba(56,189,248,.1));
      color: var(--accent); font-weight: 700; font-size: 13px;
      border: 1px solid rgba(56,189,248,.22); margin-bottom: 10px;
    }
    h1 { font-size: 28px; letter-spacing: -.4px; margin-bottom: 6px; }
    .sub { color: var(--muted); font-size: 14px; }

    /* ── GRID ── */
    .grid { display: grid; grid-template-columns: 1fr; gap: 18px; }
    @media(min-width:900px){ .grid { grid-template-columns: 1.1fr .9fr; } }

    /* ── CARD ── */
    .card {
      background: linear-gradient(160deg, rgba(255,255,255,.025), rgba(255,255,255,0)),
                  var(--card);
      border: 1px solid var(--border); border-radius: 18px;
      box-shadow: var(--shadow); padding: 20px;
    }
    .card-title {
      font-size: 13px; font-weight: 700; color: var(--accent);
      letter-spacing: .8px; text-transform: uppercase; margin-bottom: 12px;
    }

    /* ── TEXTAREA ── */
    textarea {
      width: 100%; min-height: 260px; padding: 14px; border-radius: 12px;
      border: 1px solid var(--border); background: #080f1e; color: #e2e8f0;
      font-family: "JetBrains Mono", "Fira Code", monospace; font-size: 13px;
      resize: vertical; outline: none; tab-size: 4;
    }
    textarea:focus { box-shadow: 0 0 0 3px rgba(56,189,248,.12); border-color: rgba(56,189,248,.7); }

    /* ── CONTROLS ── */
    .controls { display: flex; gap: 10px; align-items: center; margin-top: 12px; flex-wrap: wrap; }
    .btn {
      background: linear-gradient(135deg, var(--accent), var(--accent2)); color: #071524;
      border: none; border-radius: 10px; padding: 10px 18px; font-weight: 700;
      cursor: pointer; box-shadow: 0 8px 20px rgba(56,189,248,.25); font-size: 13px;
    }
    .btn:hover { filter: brightness(1.1); }
    .btn-secondary {
      background: rgba(56,189,248,.1); border: 1px solid rgba(56,189,248,.3);
      color: var(--accent); border-radius: 10px; padding: 10px 14px;
      cursor: pointer; font-weight: 600; font-size: 13px;
    }
    .btn-clear {
      background: transparent; border: 1px solid var(--border); color: var(--muted);
      border-radius: 10px; padding: 10px 14px; cursor: pointer; font-size: 13px;
    }
    .status { color: var(--muted); font-size: 13px; }

    /* ── TABS ── */
    .tabs { display: flex; gap: 0; margin-bottom: 14px; }
    .tab {
      padding: 8px 18px; font-size: 13px; font-weight: 600; cursor: pointer;
      border: 1px solid var(--border); background: transparent; color: var(--muted);
      transition: all .15s;
    }
    .tab:first-child { border-radius: 10px 0 0 10px; }
    .tab:last-child { border-radius: 0 10px 10px 0; }
    .tab.active {
      background: linear-gradient(135deg, var(--accent), var(--accent2));
      color: #071524; border-color: var(--accent); font-weight: 700;
    }

    /* ── BADGES ── */
    .summary { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 10px; }
    .badge { padding: 5px 10px; border-radius: 999px; font-weight: 700; font-size: 12px; }
    .badge.KEYWORD { color: #fbbf24; background: rgba(251,191,36,.08); }
    .badge.IDENTIFIER { color: #38bdf8; background: rgba(56,189,248,.08); }
    .badge.INTEGER, .badge.FLOAT { color: #6ee7b7; background: rgba(167,243,208,.06); }
    .badge.STRING { color: #fb923c; background: rgba(251,146,0,.06); }
    .badge.OPERATOR { color: #a5b4fc; background: rgba(199,210,254,.06); }
    .badge.DELIMITER { color: #f472b6; background: rgba(244,114,182,.06); }
    .badge.COMMENT { color: #94a3b8; background: rgba(148,163,184,.06); }
    .badge.PREPROCESSOR { color: #c084fc; background: rgba(192,132,252,.06); }
    .badge.UNKNOWN { color: #f87171; background: rgba(239,68,68,.06); }

    /* ── TABLE ── */
    .table-wrap { max-height: 500px; overflow: auto; border-radius: 10px; border: 1px solid var(--border); }
    table { width: 100%; border-collapse: collapse; }
    thead { position: sticky; top: 0; background: #071427; z-index: 1; }
    th, td { padding: 9px 12px; font-size: 13px; text-align: left; border-bottom: 1px solid var(--border); }
    th { color: var(--muted); text-transform: uppercase; font-weight: 700; letter-spacing: .6px; }
    td.val { font-family: "JetBrains Mono", monospace; color: #cbd5e1; }
    .empty { text-align: center; color: var(--muted); padding: 40px 12px; font-size: 14px; }

    /* ── AST TREE ── */
    .ast-wrap {
      max-height: 500px; overflow: auto; border-radius: 10px; border: 1px solid var(--border);
      background: #080f1e; padding: 16px; font-family: "JetBrains Mono", monospace; font-size: 12px;
    }
    .ast-node { line-height: 1.7; white-space: nowrap; }
    .ast-connector { color: #475569; }
    .ast-type { color: #38bdf8; font-weight: 700; }
    .ast-value { color: #fbbf24; }
    .ast-loc { color: #475569; font-size: 11px; }
    .ast-toggle { cursor: pointer; user-select: none; }
    .ast-toggle:hover .ast-type { text-decoration: underline; }

    /* ── ERRORS ── */
    .errors-wrap {
      max-height: 200px; overflow: auto; border-radius: 10px;
      border: 1px solid rgba(239,68,68,.3); background: rgba(239,68,68,.04);
      padding: 12px; margin-bottom: 14px;
    }
    .error-item { color: #f87171; font-size: 13px; font-family: "JetBrains Mono", monospace; margin-bottom: 4px; }

    /* ── SUMMARY PANEL ── */
    .parse-summary {
      display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
      gap: 10px; margin-bottom: 14px;
    }
    .stat-card {
      background: rgba(56,189,248,.04); border: 1px solid var(--border);
      border-radius: 12px; padding: 14px; text-align: center;
    }
    .stat-value { font-size: 26px; font-weight: 800; color: var(--accent); }
    .stat-label { font-size: 11px; color: var(--muted); text-transform: uppercase; letter-spacing: .6px; margin-top: 4px; }

    /* ── HIDDEN ── */
    .hidden { display: none !important; }

    /* ── FOOTER ── */
    footer {
      margin-top: 18px; padding-top: 12px; border-top: 1px solid var(--border);
      display: flex; justify-content: space-between; flex-wrap: wrap; gap: 8px;
      color: var(--muted); font-size: 13px;
    }
  </style>
</head>
<body>
  <div class="page">
    <header>
      <div class="pill">🔬 Syntax Analyzer</div>
      <h1>Syntax Analysis — Simulation</h1>
      <p class="sub">Browser-only lexer + parser. Paste C or Python code, then click <strong>Analyze</strong>.</p>
    </header>

    <div class="grid">
      <!-- ═══ LEFT: Source Code ═══ -->
      <div class="card">
        <div class="card-title">Source Code</div>
        <textarea id="code" spellcheck="false">#include <stdio.h>

// Sample program
int main() {
    int x = 10;
    float pi = 3.14;
    char *msg = "Hello, World!";

    if (x >= 5 && pi != 0) {
        printf("%s\n", msg);
        x++;
    }

    /* Multi-line
       comment */
    return 0;
}</textarea>

        <div class="controls">
          <button class="btn" id="run">⚡ Analyze</button>
          <button class="btn-secondary" id="demo-c">Demo C</button>
          <button class="btn-secondary" id="demo-py">Demo Python</button>
          <button class="btn-clear" id="clear">Clear</button>
          <span class="status" id="status">Ready</span>
        </div>
      </div>

      <!-- ═══ RIGHT: Results ═══ -->
      <div class="card">
        <div class="tabs">
          <button class="tab active" data-tab="tokens">Tokens</button>
          <button class="tab" data-tab="ast">AST</button>
          <button class="tab" data-tab="summary">Summary</button>
        </div>

        <!-- Errors (shown when present) -->
        <div class="errors-wrap hidden" id="errors-panel"></div>

        <!-- TAB: Tokens -->
        <div id="panel-tokens">
          <div class="summary" id="token-summary"></div>
          <div class="table-wrap">
            <table>
              <thead><tr><th>#</th><th>Type</th><th>Value</th><th>Ln</th><th>Col</th></tr></thead>
              <tbody id="token-tbody">
                <tr><td colspan="5" class="empty">Click <strong>Analyze</strong> to tokenize and parse code.</td></tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- TAB: AST -->
        <div id="panel-ast" class="hidden">
          <div class="ast-wrap" id="ast-container">
            <div class="empty">Click <strong>Analyze</strong> to generate the AST.</div>
          </div>
        </div>

        <!-- TAB: Summary -->
        <div id="panel-summary" class="hidden">
          <div class="parse-summary" id="summary-stats"></div>
          <div class="card-title" style="margin-top:10px">Node Type Breakdown</div>
          <div class="table-wrap">
            <table>
              <thead><tr><th>Node Type</th><th>Count</th></tr></thead>
              <tbody id="node-tbody">
                <tr><td colspan="2" class="empty">No data yet.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <footer>
      <div>Syntax Analyzer — Browser Edition</div>
      <div>Powered by JavaScript • No server required</div>
    </footer>
  </div>

<script>
// ═══════════════════════════════════════════════════════════
//  LEXER (tokenizer) — translated from Python
// ═══════════════════════════════════════════════════════════
const KEYWORDS = new Set([
  "auto","break","case","char","const","continue","default","do",
  "double","else","enum","extern","float","for","goto","if",
  "int","long","register","return","short","signed","sizeof","static",
  "struct","switch","typedef","union","unsigned","void","volatile","while",
  "print","input","def","class","import","from","as","try","except",
  "finally","raise","with","yield","lambda","pass","True","False","None",
  "and","or","not","in","is","elif"
]);
const MULTI_OPS = new Set(["==","!=","<=",">=","&&","||","++","--","+=","-=","*=","/=","<<",">>","->","**","//"]);
const SINGLE_OPS = new Set([..."+-*/%=<>!&|^~?:@"]);
const DELIMITERS = new Set([..."(){}[];,."]);

function tokenize(source) {
  const tokens = [];
  let pos = 0, line = 1, col = 1;
  const cur = () => pos < source.length ? source[pos] : null;
  const peek = () => pos + 1 < source.length ? source[pos + 1] : null;
  const adv = () => { if (source[pos] === '\n') { line++; col = 1; } else col++; pos++; };
  const add = (type, value, l, c) => tokens.push({ type, value, line: l, column: c });

  while (pos < source.length) {
    while (cur() !== null && (cur() === ' ' || cur() === '\t' || cur() === '\r')) adv();
    const ch = cur(); if (ch === null) break;

    if (ch === '\n') { add('NEWLINE', '\\n', line, col); adv(); continue; }

    if (ch === '#') {
      const sl = line, sc = col; let d = '';
      while (cur() !== null && cur() !== '\n') { d += cur(); adv(); }
      add('PREPROCESSOR', d, sl, sc); continue;
    }
    if (ch === '/' && peek() === '/') {
      const sl = line, sc = col; let cmt = '';
      while (cur() !== null && cur() !== '\n') { cmt += cur(); adv(); }
      add('COMMENT', cmt, sl, sc); continue;
    }
    if (ch === '/' && peek() === '*') {
      const sl = line, sc = col; let cmt = '/*'; adv(); adv();
      while (cur() !== null) {
        if (cur() === '*' && peek() === '/') { cmt += '*/'; adv(); adv(); break; }
        cmt += cur(); adv();
      }
      add('COMMENT', cmt, sl, sc); continue;
    }
    if (ch >= '0' && ch <= '9') {
      const sl = line, sc = col; let n = '', isF = false;
      while (cur() !== null && ((cur() >= '0' && cur() <= '9') || cur() === '.')) {
        if (cur() === '.') { if (isF) break; isF = true; }
        n += cur(); adv();
      }
      add(isF ? 'FLOAT' : 'INTEGER', n, sl, sc); continue;
    }
    if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') || ch === '_') {
      const sl = line, sc = col; let w = '';
      while (cur() !== null && /[a-zA-Z0-9_]/.test(cur())) { w += cur(); adv(); }
      add(KEYWORDS.has(w) ? 'KEYWORD' : 'IDENTIFIER', w, sl, sc); continue;
    }
    if (ch === '"' || ch === "'") {
      const sl = line, sc = col, q = ch; let s = q; adv();
      while (cur() !== null && cur() !== q) {
        if (cur() === '\\') { s += cur(); adv(); }
        if (cur() !== null) { s += cur(); adv(); }
      }
      if (cur() === q) { s += cur(); adv(); }
      add('STRING', s, sl, sc); continue;
    }
    if (peek() !== null && MULTI_OPS.has(ch + peek())) {
      add('OPERATOR', ch + peek(), line, col); adv(); adv(); continue;
    }
    if (SINGLE_OPS.has(ch)) { add('OPERATOR', ch, line, col); adv(); continue; }
    if (DELIMITERS.has(ch)) { add('DELIMITER', ch, line, col); adv(); continue; }
    add('UNKNOWN', ch, line, col); adv();
  }
  return tokens;
}

// ═══════════════════════════════════════════════════════════
//  AST NODE
// ═══════════════════════════════════════════════════════════
class ASTNode {
  constructor(type, value = null, line = 0, column = 0) {
    this.type = type; this.value = value; this.line = line; this.column = column;
    this.children = [];
  }
  addChild(child) { if (child) this.children.push(child); return this; }
  countNodes() { let c = 1; for (const ch of this.children) c += ch.countNodes(); return c; }
  countByType(counts = {}) {
    counts[this.type] = (counts[this.type] || 0) + 1;
    for (const ch of this.children) ch.countByType(counts);
    return counts;
  }
}

// ═══════════════════════════════════════════════════════════
//  PARSER — translated from Python
// ═══════════════════════════════════════════════════════════
class Parser {
  constructor(tokens) {
    this.tokens = tokens.filter(t => t.type !== 'NEWLINE' && t.type !== 'COMMENT');
    this.pos = 0;
    this.errors = [];
    this.ast = new ASTNode('PROGRAM');
  }
  cur() { return this.pos < this.tokens.length ? this.tokens[this.pos] : null; }
  peekTok(off = 1) { const i = this.pos + off; return i < this.tokens.length ? this.tokens[i] : null; }
  adv() { const t = this.cur(); this.pos++; return t; }
  addError(msg, token) {
    const t = token || this.cur();
    if (t) this.errors.push({ message: msg, line: t.line, column: t.column, value: t.value });
    else this.errors.push({ message: msg, line: 0, column: 0, value: 'EOF' });
  }
  expect(type, value) {
    const t = this.cur();
    if (!t) { this.addError(`Expected ${type}${value ? " '" + value + "'" : ''}, got EOF`); return null; }
    if (t.type !== type || (value !== undefined && t.value !== value)) {
      this.addError(`Expected ${type}${value ? " '" + value + "'" : ''}, got '${t.value}'`, t);
      return null;
    }
    return this.adv();
  }
  match(type, value) {
    const t = this.cur();
    if (!t || t.type !== type) return false;
    if (value !== undefined && t.value !== value) return false;
    return true;
  }
  matchAnyKw(kws) { const t = this.cur(); return t && t.type === 'KEYWORD' && kws.includes(t.value); }

  // ── GRAMMAR ──
  parse() {
    while (this.cur()) {
      if (this.match('PREPROCESSOR')) {
        const t = this.cur();
        this.ast.addChild(new ASTNode('PREPROCESSOR', t.value, t.line, t.column));
        this.adv(); continue;
      }
      const stmt = this.parseStatement();
      if (stmt) this.ast.addChild(stmt);
      else { if (this.cur()) { this.addError(`Unexpected token '${this.cur().value}'`); this.adv(); } }
    }
    return this.ast;
  }

  parseStatement() {
    const t = this.cur(); if (!t) return null;
    const cTypes = ["int","float","double","char","void","long","short","signed","unsigned",
                    "auto","static","extern","register","const","volatile"];
    if (t.type === 'KEYWORD' && cTypes.includes(t.value)) return this.parseDeclOrFunc();
    if (this.match('KEYWORD','struct')) return this.parseStruct();
    if (this.match('KEYWORD','enum')) return this.parseEnum();
    if (this.match('KEYWORD','typedef')) return this.parseTypedef();
    if (this.match('KEYWORD','return')) return this.parseReturn();
    if (this.match('KEYWORD','if')) return this.parseIf();
    if (this.match('KEYWORD','while')) return this.parseWhile();
    if (this.match('KEYWORD','do')) return this.parseDoWhile();
    if (this.match('KEYWORD','for')) return this.parseFor();
    if (this.match('KEYWORD','switch')) return this.parseSwitch();
    if (this.match('KEYWORD','break')) return this.parseBreak();
    if (this.match('KEYWORD','continue')) return this.parseContinue();
    if (this.match('KEYWORD','goto')) return this.parseGoto();
    if (this.match('KEYWORD','def')) return this.parsePyDef();
    if (this.match('KEYWORD','class')) return this.parsePyClass();
    if (this.match('KEYWORD','import') || this.match('KEYWORD','from')) return this.parsePyImport();
    if (this.match('KEYWORD','elif')) return this.parseElif();
    if (this.match('KEYWORD','try')) return this.parsePyTry();
    if (this.match('KEYWORD','except')) return this.parsePyExcept();
    if (this.match('KEYWORD','finally')) return this.parsePyFinally();
    if (this.match('KEYWORD','with')) return this.parsePyWith();
    if (this.match('KEYWORD','raise')) return this.parsePyRaise();
    if (this.match('KEYWORD','pass')) return this.parsePyPass();
    if (this.match('KEYWORD','yield')) return this.parsePyYield();
    if (this.match('KEYWORD','print')) return this.parseExprStmt();
    if (this.match('DELIMITER','{')) return this.parseBlock();
    if (['IDENTIFIER','INTEGER','FLOAT','STRING','DELIMITER','OPERATOR','KEYWORD'].includes(t.type))
      return this.parseExprStmt();
    return null;
  }

  parseDeclOrFunc() {
    const st = this.cur(); const nL = st.line, nC = st.column;
    let ts = '';
    const cT = ["int","float","double","char","void","long","short","signed","unsigned",
                "auto","static","extern","register","const","volatile"];
    while (this.cur() && this.cur().type === 'KEYWORD' && cT.includes(this.cur().value)) {
      ts += (ts ? ' ' : '') + this.cur().value; this.adv();
    }
    while (this.match('OPERATOR','*')) { ts += '*'; this.adv(); }
    if (!this.match('IDENTIFIER')) {
      this.addError(`Expected identifier after type '${ts}'`);
      return new ASTNode('ERROR', ts, nL, nC);
    }
    const name = this.adv();
    if (this.match('DELIMITER','(')) return this.parseFuncDef(ts, name, nL, nC);
    const node = new ASTNode('VAR_DECL', ts, nL, nC);
    const vn = new ASTNode('VARIABLE', name.value, name.line, name.column);
    if (this.match('DELIMITER','[')) {
      this.adv();
      if (this.cur() && (this.cur().type === 'INTEGER' || this.cur().ty
