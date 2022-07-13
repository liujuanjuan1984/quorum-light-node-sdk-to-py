const QuorumLightNodeSDK = require('quorum-light-node-sdk');

const seedUrl =  decodeURIComponent(process.argv[2]);
const nodeToken = process.argv[3];
const result = QuorumLightNodeSDK.cache.Group.add(seedUrl, {
  nodeToken
});
console.log(result);
