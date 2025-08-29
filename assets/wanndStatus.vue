<template>
    <small>
        accu: {{accu.toFixed(5)}} lastUpdate: ( {{lastUpdate}}) <br>
        {{xyz[0].toFixed(5)}} | 
        {{xyz[1].toFixed(5)}} | 
        {{xyz[2].toFixed(5)}} 
    </small><br>



    <button @click="dummyData()">dummy Data</button>
    

</template>

<script>
import { ref } from 'vue'


export default {  
  data(){
    let xyz = ref([0,0,0]);
    let accu = ref(10.0);
    let lastT = ref( -1 );
    let lastUpdate = ref( -1 );

    let intervUpdate = -1;

    return { xyz, accu, lastT, lastUpdate, intervUpdate }
  },
  methods:{
    dummyData(){
        //console.log('wanSta DUMMY data');
        siteByKey.c_3dwanndPage.o.onMessageCallBack({
            "topic": "b3d/posUpdate",
            "accu": Math.random(),
            "avgP": [Math.random(),Math.random(),Math.random()]
        });


    },
    newMsgOnWs( msg ){
        //console.log(" wanSta    newMsgOnWs",msg);
        if( msg.topic == undefined || msg.topic.substr(0,3) != 'b3d')
            return 1;
        if( this.lastT == -1 ){
            this.lastUpdate = 'now first';
            this.lastT = Date.now();

            this.intervUpdate = setInterval(()=>{
                let tRes = ((Date.now() - this.lastT)/1000.00);
                if( tRes  > 3.00 ){
                    this.lastUpdate = parseInt(tRes)+" sec.";
                }else{
                    this.lastUpdate = tRes.toFixed(1)+" sec.";
                }
            },1000);

        }else{
            this.lastUpdate = ((Date.now() - this.lastT)/1000.00).toFixed(1)+" sec.";
            this.lastT = Date.now();
        }

        this.accu = msg.accu;
        this.xyz = msg.avgP;
        
    }

  }
}

</script>