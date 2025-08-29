<template>
    wannd pois collector (  {{ xyzaS.length }} / {{ xyza.length }})<br>


    <button @click="addDataToStack()">[+]</button>
    
    <button 
        @click="sendMeshFromStack()"
        :disabled="!sendMeshFromStackPossible"
        >send mesh</button>
    
    <button @click="clearList()">[x]</button>
    <br>
    <WanndPOIItem
        v-for="( item,index ) in xyzaS"
        :x="item[0]" :y="item[1]" :z="item[2]" 
        :accu="item[3]" />


</template>

<script>
import { ref } from 'vue'
import WanndPOIItem from './wanndPOIItem.vue';


export default {  
    components:{
        WanndPOIItem
    },

  data(){
    let xyza = [];
    let xyzaS = [];
    let meshName = `M${Date.now()}`;
    let sendMeshFromStackPossible = false;

    
    return { xyza, xyzaS, sendMeshFromStackPossible, meshName }
  },
  methods:{
    newMsgOnWs( msg ){
        //console.log(" wanPoiCol    newMsgOnWs",msg);
        if( msg.topic != undefined && msg.topic == 'b3d/posUpdate'){
            if( this.xyza.length > 30 )
                this.xyza.pop(0);
            this.xyza.push( [ msg.avgP[0], msg.avgP[1],msg.avgP[2], msg.accu] );
        
        }
        
    },

    sendMeshFromStack(){
        console.log(' send coords ',this.xyzaS);
        let verts = [];
        let edges = [];
        let faces = [];
        let p = 0;
        for( let v of this.xyzaS ){
            verts.push( [ v[0],v[1],v[2] ] );
            faces.push( p++ );
        }

        let ts = {
            "topic": "b3d/build/mesh",
            "name": this.meshName,
            "verts": verts,
            "edges": edges,
            "faces": [faces]
        };
        //console.log(JSON.stringify(ts,null,4));
        let st = `wsSendToWSID:b3d:${JSON.stringify(ts)}`;
        //console.log(st);
        sOutSend(st);   

        this.clearList();
    },

    addDataToStack(){
        let p = this.xyza[ this.xyza.length-1  ];
        this.xyzaS.push( p );
        if( this.xyzaS.length >= 3)
            this.sendMeshFromStackPossible = true;
    },

    clearList(){
        this.xyza = [];
        this.xyzaS = [];
        this.sendMeshFromStackPossible = false;
    }

  }
}

</script>