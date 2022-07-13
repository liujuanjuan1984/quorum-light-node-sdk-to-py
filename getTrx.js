const QuorumLightNodeSDK = require('quorum-light-node-sdk');

(async () => {
  try {
    const groupId = process.argv[2];
    const trxId = process.argv[3];
    const result = await QuorumLightNodeSDK.chain.Trx.get(groupId, trxId);
    console.log(result);
  } catch (err) {
    console.log(err);
  }
})();