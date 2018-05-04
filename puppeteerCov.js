console.log('Running...');
const puppeteer = require('/home/x/.nvm/versions/node/v9.5.0/lib/node_modules/puppeteer');
var fs = require('fs');

var url="https://"+(process.argv[2]).toString();
var name=url.split('//')[1].split(".")[0];
console.log(`Extracting Coverage for ${url}`);

(async () => {
console.log(`Opening page in background browser context: /usr/bin/chromium`);
const browser = await puppeteer.launch({executablePath: '/usr/bin/chromium', headless: true});
const page = await browser.newPage();

await Promise.all([
  page.coverage.startJSCoverage(),
  page.coverage.startCSSCoverage()
]);
// Navigate to page
await page.goto(url);
// Disable both JavaScript and CSS coverage
const [jsCoverage, cssCoverage] = await Promise.all([
  page.coverage.stopJSCoverage(),
  page.coverage.stopCSSCoverage(),
]);

let totalBytes = 0;
let usedBytes = 0;
const coverage = [...jsCoverage, ...cssCoverage];
fs.writeFileSync(`${name}-Cov.json`, JSON.stringify(coverage, null, 2));
console.log(` -- Coverage data saved to file ${name}-Cov.json. Take a look -- `);
await browser.close();
console.log('Closing session...');
})();