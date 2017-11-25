"use strict";

var url="https://"+(process.argv[2]).toString();
var name=url.split('//')[1].split(".")[0];

var _fs = require("fs");

var fs = _interopRequireWildcard(_fs);

var _chromeDebuggingClient = require("/home/w/.nvm/versions/node/v8.9.1/lib/node_modules/chrome-debugging-client");

function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }

(0, _chromeDebuggingClient.createSession)(async function (session) {
  let browser = await session.spawnBrowser('exact', {
 	executablePath: '/usr/bin/google-chrome-stable'
  });
  var api = await session.createAPIClient("localhost", browser.remoteDebuggingPort);
  var tabs = await api.listTabs();
  var tab = tabs[0];
  var client = await session.openDebuggingProtocol(tab.webSocketDebuggerUrl);
  await client.send("Profiler.enable");
  await client.send("Page.enable");
  await client.send("Profiler.startPreciseCoverage", {
    callCount: true
  });
  await client.send("Page.navigate", {
    url
  });
  await new Promise(function (resolve) {
    return client.on("Page.loadEventFired", resolve);
  });
  await new Promise(function (resolve) {
    return setTimeout(resolve, 1000);
  });
  var result = await client.send("Profiler.takePreciseCoverage");
  fs.writeFileSync(`${name}-JSCov.json`, JSON.stringify(result, null, 2));
}).catch(function (err) {
  console.error(err);
});

