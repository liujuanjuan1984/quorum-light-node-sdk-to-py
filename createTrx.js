const QuorumLightNodeSDK = require('quorum-light-node-sdk');

(async () => {
  try {
    const result = await QuorumLightNodeSDK.chain.Trx.create({
      groupId: process.argv[2],
      object: JSON.parse(process.argv[3]),
      privateKey: process.argv[4],
    });
    console.log(result);
  } catch (err) {
    console.log(err);
  }
})();