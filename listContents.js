const QuorumLightNodeSDK = require('quorum-light-node-sdk');

// list contents
(async () => {
  try {
    const result = await QuorumLightNodeSDK.chain.Content.list({
      groupId: process.argv[2],
      count: 100
    });
    console.log(result);
  } catch (err) {
    console.log(err);
  }
})();
