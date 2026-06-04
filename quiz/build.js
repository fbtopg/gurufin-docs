const fs = require('fs');
const path = require('path');

// Read the QnA.md file
const qnaPath = '/home/geonu/workspace/projects/guruswap-gitbook/QnA.md';
const content = fs.readFileSync(qnaPath, 'utf-8');

// Split into question blocks
const blocks = content.split(/(?=### Q\d+\.\s)/);

const qaPairs = [];

for (const block of blocks) {
  const qMatch = block.match(/### Q(\d+)\.\s+(.+?)\n/);
  if (!qMatch) continue;

  const num = parseInt(qMatch[1]);
  const question = qMatch[2].trim();
  
  // Extract answer: everything after the first **A.** or the first paragraph after the question header
  const lines = block.split('\n');
  let answerLines = [];
  let started = false;
  
  for (let i = 1; i < lines.length; i++) {
    const line = lines[i];
    // Skip empty lines at start of answer
    if (!started && line.trim() === '') continue;
    
    // Stop at next question or section header
    if (line.match(/^### Q\d+\./) || line.match(/^## /) || (line.match(/^---$/) && started)) continue;
    
    started = true;
    answerLines.push(line);
  }
  
  if (started && answerLines.length > 0) {
    let answer = answerLines.join('\n');
    // Clean up leading **A.** if present
    answer = answer.replace(/^\*\*A\.\*\s*/, '');
    // Remove trailing empty lines
    answer = answer.trim();
    qaPairs.push({ num, q: question, a: answer });
  }
}

console.log(`Found ${qaPairs.length} Q&A pairs`);
for (const pair of qaPairs) {
  console.log(`Q${pair.num}: ${pair.q.substring(0, 50)}...`);
}

// Generate escaped strings for the QA array
const jsEntries = qaPairs.map(pair => {
  // Escape special characters for JS string
  const qEscaped = pair.q
    .replace(/\\/g, '\\\\')
    .replace(/"/g, '\\"')
    .replace(/\n/g, '\\n');
  const aEscaped = pair.a
    .replace(/\\/g, '\\\\')
    .replace(/"/g, '\\"')
    .replace(/\n/g, '\\n');
  return `  { q: "${qEscaped}", a: "${aEscaped}" },`;
});

fs.writeFileSync('/home/geonu/workspace/projects/gurufin-gitbook/quiz/qa_entries.js', jsEntries.join('\n'));
console.log(`\nWritten ${jsEntries.length} entries to qa_entries.js`);
