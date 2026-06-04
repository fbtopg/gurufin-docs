const fs = require('fs');

const entries = fs.readFileSync('/home/geonu/workspace/projects/gurufin-gitbook/quiz/qa_entries.js', 'utf-8').trim();

const tpl = `<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GuruSwap FX — Q&A Review</title>
<style>
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans KR',sans-serif;background:#fff;color:#111;min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:2rem;line-height:1.7}
#a{width:100%;max-width:720px}
.h{text-align:center;margin-bottom:2rem}
.h h1{font-size:1.4rem;font-weight:600;letter-spacing:-.02em}
.pr{margin-top:.5rem;font-size:.85rem;color:#666}
.pb{width:100%;height:3px;background:#eee;margin-top:.5rem}
.pb .f{height:100%;background:#111;transition:width .2s}
.qg{font-size:.8rem;color:#999;margin-bottom:.5rem;text-transform:uppercase;letter-spacing:.05em}
.q{font-size:1.15rem;font-weight:600;margin-bottom:1.5rem;white-space:pre-wrap}
.a{font-size:.95rem;white-space:pre-wrap;margin-bottom:2rem;line-height:1.8}
.a table{border-collapse:collapse;margin:.5rem 0 1rem;width:100%}
.a th,.a td{border:1px solid #ddd;padding:6px 10px;text-align:left;font-size:.9em}
.a code{background:#f5f5f5;padding:1px 5px;border-radius:3px;font-size:.88em}
.a pre{background:#f5f5f5;padding:.75rem;border-radius:4px;overflow-x:auto;margin:.5rem 0}
.a pre code{background:none;padding:0}
.a strong{font-weight:600}
.a hr{border:none;border-top:1px solid #eee;margin:1rem 0}
.br{display:flex;gap:.75rem;margin-bottom:1.5rem}
.bt{padding:.6rem 2rem;font-size:.95rem;font-weight:600;border:1px solid #111;background:#fff;color:#111;cursor:pointer;border-radius:4px;transition:all .15s}
.bt:hover{background:#111;color:#fff}
.bt.sel{background:#111;color:#fff}
.ju{margin-bottom:1.5rem}
.ju textarea{width:100%;min-height:100px;padding:.75rem;font-size:.9rem;font-family:inherit;border:1px solid #ccc;border-radius:4px;resize:vertical;line-height:1.6}
.ju textarea:focus{outline:none;border-color:#111}
.nr{display:flex;justify-content:space-between;align-items:center}
.nb{padding:.5rem 1.2rem;font-size:.85rem;border:1px solid #ddd;background:#fff;color:#666;cursor:pointer;border-radius:4px;transition:all .15s}
.nb:hover:not(:disabled){border-color:#111;color:#111}
.nb:disabled{opacity:.3;cursor:default}
#es{margin-top:1rem}
#eb{padding:.6rem 2rem;font-size:.95rem;font-weight:600;border:1px solid #111;background:#111;color:#fff;cursor:pointer;border-radius:4px}
#eb:hover{background:#333}
#out{margin-top:1.5rem;width:100%;min-height:200px;padding:1rem;font-size:.85rem;font-family:'Courier New',monospace;border:1px solid #eee;background:#fafafa;border-radius:4px;resize:vertical;line-height:1.6;white-space:pre-wrap}
</style>
</head>
<body>
<div id="a"></div>
<script>
const QA = ${entries};

let current = 0;
const decisions = QA.map(() => null);
const justifications = QA.map(() => '');

function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}

function md(t){
  let h=t.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  h=h.replace(/\\x60\\x60\\x60([\\s\\S]*?)\\x60\\x60\\x60/g,'<pre><code>$1</code></pre>');
  h=h.replace(/\\x60([^\\x60]+)\\x60/g,'<code>$1</code>');
  h=h.replace(/\\*\\*(.+?)\\*\\*/g,'<strong>$1</strong>');
  h=h.replace(/^\\|(.+)\\|\\n\\|[-|\\s:]+\\|\\n((?:\\|.+)\\|\\n*)/gm,function(m,hd,bd){
    const hs=hd.split('|').map(s=>s.trim()).filter(Boolean);
    const rs=bd.trim().split('\\n').map(l=>l.split('|').map(s=>s.trim()).filter(Boolean));
    let r='<table><thead><tr>';hs.forEach(c=>r+='<th>'+c+'</th>');
    r+='</tr></thead><tbody>';
    rs.forEach(row=>{r+='<tr>';row.forEach(c=>r+='<td>'+c+'</td>');r+='</tr>'});
    return r+'</tbody></table>';
  });
  h=h.replace(/\\n\\n/g,'</p><p>');
  h=h.replace(/\\n/g,'<br>');
  return '<p>'+h+'</p>';
}

function render(){
  const a=document.getElementById('a');
  const n=QA.length;
  const done=decisions.every(d=>d!==null);
  if(done){a.innerHTML=exportHtml();return}
  const q=QA[current];
  const ac=decisions.filter(d=>d!==null).length;
  const pct=(ac/n*100);
  const wc=decisions[current]==='맞음';
  const ww=decisions[current]==='틀림';
  a.innerHTML='<div class="h"><h1>GuruSwap FX — Q&A Review</h1>'+
    '<div class="pr">'+ac+' / '+n+' answered'+
    '<div class="pb"><div class="f" style="width:'+pct+'%"></div></div></div></div>'+
    '<div class="qg">Question '+(current+1)+' of '+n+'</div>'+
    '<div class="q">'+esc(q.q)+'</div>'+
    '<div class="a">'+md(q.a)+'</div>'+
    '<div class="br">'+
    '<button class="bt'+(wc?' sel':'')+'" onclick="vote(\\"맞음\\")">맞음</button>'+
    '<button class="bt'+(ww?' sel':'')+'" onclick="vote(\\"틀림\\")">틀림</button></div>'+
    (ww?'<div class="ju"><textarea id="ju" placeholder="왜 틀렸다고 생각하시나요? 이유를 적어주세요..." oninput="setJ('+current+',this.value)">'+esc(justifications[current])+'</textarea></div>':
    wc?'<p style="color:#888;font-size:.85rem;margin-bottom:1rem;">&#10004; 맞음으로 선택했습니다.</p>':'')+
    '<div class="nr">'+
    '<button class="nb" onclick="go(-1)"'+(current===0?' disabled':'')+'>&#8592; Previous</button>'+
    '<button class="nb" onclick="go(1)"'+(current===n-1?' disabled':'')+'>Next &#8594;</button></div>';
}

function exportHtml(){
  let md='';
  md+='# GuruSwap FX \\u2014 Q&A Review Results\\n\\n';
  md+='> Review completed on '+new Date().toISOString().split('T')[0]+'\\n\\n';
  md+='---\\n\\n';
  for(let i=0;i<QA.length;i++){
    const d=decisions[i],j=justifications[i];
    md+='## Q'+(i+1)+'. '+QA[i].q+'\\n\\n';
    md+=QA[i].a+'\\n\\n';
    md+='**Viewer Decision:** '+(d==='맞음'?'\\u2705 맞음':'\\u274c 틀림')+'\\n';
    if(d==='틀림'&&j.trim())md+='\\n**Justification:**\\n'+j+'\\n';
    md+='\\n---\\n\\n';
  }
  const co=decisions.filter(d=>d==='맞음').length;
  const wr=decisions.filter(d=>d==='틀림').length;
  md+='## Summary\\n\\nTotal: '+QA.length+' | \\u2705 맞음: '+co+' | \\u274c 틀림: '+wr+'\\n';
  return '<div class="h"><h1>Review Complete!</h1>'+
    '<p>'+co+' 맞음 &middot; '+wr+' 틀림 &middot; Total '+QA.length+' questions</p></div>'+
    '<div id="es"><button id="eb" onclick="copyMd()">Copy Markdown</button>'+
    '<textarea id="out" readonly>'+esc(md)+'</textarea></div>';
}

window.vote=function(v){decisions[current]=v;if(v==='맞음')justifications[current]='';render()};
window.setJ=function(i,v){justifications[i]=v};
window.go=function(d){const n=current+d;if(n>=0&&n<QA.length){current=n;render()}};
window.copyMd=function(){
  const t=document.getElementById('out').value;
  navigator.clipboard.writeText(t).then(function(){
    const b=document.getElementById('eb');b.textContent='Copied!';
    setTimeout(function(){b.textContent='Copy Markdown'},2000);
  });
};

render();
</script>
</body>
</html>`;

fs.writeFileSync('/home/geonu/workspace/projects/gurufin-gitbook/quiz/index.html', tpl);
console.log('Generated index.html with', entries.match(/{ q: /g).length, 'Q&A pairs');
