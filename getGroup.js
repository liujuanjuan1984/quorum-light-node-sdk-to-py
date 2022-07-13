const QuorumLightNodeSDK = require('quorum-light-node-sdk');

const groupId = process.argv[2];
const result = QuorumLightNodeSDK.cache.Group.get(groupId);
console.log(result);
