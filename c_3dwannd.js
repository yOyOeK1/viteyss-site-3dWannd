
import { createApp } from 'vue';

import wanndStatus from './assets/wanndStatus.vue';
import WanndPoiColector from './assets/wanndPoiColector.vue';

async function setFocusCam( tra, v ){
    await tra.applyConstraints( v );
    return 1;
}


class c_3dwanndPage{

  constructor(){

    this.wanSta = createApp(wanndStatus);
    this.wanPoiCol = createApp( WanndPoiColector);

  }
  
  get getName(){
    return `3d Wannd`;
    
  }
  
  
  
  get getDefaultBackgroundColor(){
    return "#ffffff";
    
  }
  
  



  

  getHtml = () => {
    
    return `
    <link rel="stylesheet" href="${this.homeUrl}3dwannd.css">
    <!--<b>${this.getName}</b><br>
    <pre>   In Menu: ${this.getName}
    Home url: ${this.homeUrl}
    Ver: ${this.instanceOf.ver}
    Dir: ??
    More ditails in \`./site.json\`</pre>
<input type="button" id="btdziharDHStart" value="DH Start Streaming">
    -->
    <img src="${this.homeUrl}assets/marker_42.png" style="">
    <input type="button" id="btwanSetPOI" value="Set POI">
    <div id="3dwandAcu"></div>
    <div id="3dwanndClick"><b>click OK</b></div>
    <hr>
    <div id="vuewanStat"></div>
    <hr>
    <div id="vuewanPoiCol"></div>
    <hr>
    <br><br><br><br>
    `;

  }

  getHtmlAfterLoad = () =>{
    cl(`${this.getName} - getHtmlAfterLoad()`);

    //this.app = createApp( cameraControls ).mount('#dziharCamControl');
    this.wanSta.mount('#vuewanStat');
    this.wanPoiCol.mount('#vuewanPoiCol');

    setTimeout(()=>{
      sOutSend(`wsClientIdent:3dwannd`);
      $('#3dwanndClick').hide('slow');
    },1000);

    $('#btwanSetPOI').click((e)=>{
      console.log('click');
      sOutSend(`wsSendToWSID:ocvCam:{"topic":"bt/SetPOI","sender":"3dwannd", "payload":"click"}`);
    });


  }

  

  onPageLeft = () =>{
    //this.app.unmount();
   
    
  }

  get svgDyno(){
    return '';

  }

  svgDynoAfterLoad(){

  }

  onMessageCallBack = ( r ) => {
    //cl( `[cb] ${this.getName} - got msg \n\n`+JSON.stringify(r,null,4));

    this.wanSta._instance.ctx.newMsgOnWs( r );
    this.wanPoiCol._instance.ctx.newMsgOnWs( r );


    if( r.topic == '3dwannd/stats' ){
      $('#3dwandAcu').html(`accu: ${r.acuLevel}<br>
        ${r.avgP[0]}<br>
        ${r.avgP[1]}<br>
        ${r.avgP[2]}
        
        `);

    }else if( r.topic == 'bt/SetPOI' && r.status == 'done' && r.payload == 'click' ){
      $('#3dwanndClick').show('slow');
      setTimeout(()=>{
        $('#3dwanndClick').hide();
      },3000)
      console.log('click ok');
    }
    /*
    if( r.topic == 'dzihar/streamSwith' ){
      if( r.payload == 'on' ){
        this.mainStart( r.doIt );
        //this.app.update();

      } else {
        this.mainStop();
       // this.app.update();
      }

    }
    */

  }

}

export { c_3dwanndPage };
