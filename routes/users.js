var express = require("express");
var router = express.Router();

/* GET users listing. */
router.get("/", function (req, res, next) {
  const { spawn } = require("node:child_process");
  const sh = spawn("sh", ["gpio.sh"]);

  sh.stdout.on("data", (data) => {
    console.log(`stdout: ${data}`);
  });

  sh.stderr.on("data", (data) => {
    console.error(`stderr: ${data}`);
  });

  sh.on("close", (code) => {
    console.log(`child process exited with code ${code}`);
  });
  res.send("respond with a resource");
});

module.exports = router;
