// Gera os PDFs a partir dos HTML de build/out. Uso: node render.js [arquivo.html ...]
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const out = path.join(__dirname, 'out');
  const files = process.argv.slice(2).length
    ? process.argv.slice(2)
    : fs.readdirSync(out).filter(f => f.endsWith('.html')).map(f => path.join(out, f));
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  for (const f of files) {
    const page = await browser.newPage();
    await page.goto('file://' + path.resolve(f), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const nome = path.basename(f, '.html');
    const rotulo = nome.replace(/_/g, ' ').replace('Simulado UERJ', 'Simulado estilo UERJ').replace(' Resolucao', ' · Resolução comentada').replace(' Caderno', ' · Caderno de questões');
    await page.pdf({
      path: f.replace(/\.html$/, '.pdf'),
      format: 'A4',
      printBackground: true,
      displayHeaderFooter: true,
      headerTemplate: '<span></span>',
      footerTemplate: `<div style="font-family:Inter,sans-serif;font-size:7px;color:#6b7280;width:100%;padding:0 17mm;display:flex;justify-content:space-between"><span>Iteramnese · ${rotulo.replace(/^Simulado estilo UERJ (\d+)/, 'Simulado $1 estilo UERJ')}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
      margin: { top: '18mm', bottom: '20mm', left: '17mm', right: '17mm' },
    });
    await page.close();
    console.log('ok', path.basename(f));
  }
  await browser.close();
})();
