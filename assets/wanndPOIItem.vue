<style>
.wanndPoiItem{
    min-width: 100vw;
    background-color: rgb(248, 244, 179);
}
.wanndPoiItem span{
    margin-left: 10px;
}
.wanndPoiItem span:first-child{
    background-color: rgb(204, 252, 58);
}

</style>
<template>
    <div class="wanndPoiItem">
        <small>
            <span>A:{{accu.toFixed(5)}}</span>
            <span>x:{{x.toFixed(5)}}</span> 
            <span>y:{{y.toFixed(5)}}</span>
            <span>z:{{z.toFixed(5)}}</span>
        </small><br>
    </div>

</template>

<script>
import { ref } from 'vue'


export default {  
    props:[ 'accu', 'x','y','z'],

    data(){


        return {  }
    },

    methods:{

    }
}

</script>