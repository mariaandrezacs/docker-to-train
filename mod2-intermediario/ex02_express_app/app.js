const express = require("express");
const app = express();
app.get("/", (req, res) => res.send("Express no Docker, funcionando!"));
app.listen(3000);