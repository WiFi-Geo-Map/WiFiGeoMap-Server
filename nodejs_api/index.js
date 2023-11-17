// import list from './bssid.json' assert {type:"json"} ;
let list =require('./bssid.json') ;

const express = require('express');
const app = express();
const PORT = 8080;

app.use(express.json())

app.listen(
    PORT,
    ()=>console.log(`is it alive on port ${PORT}?`)
)

app.post('/wifi-api',(req,res)=>{
    //const {id} = req.params;
    const {bssid}=req.body;
    const room=list[bssid];
    // console.log(room);
    res.send({
        room: `${room}`
    })
})