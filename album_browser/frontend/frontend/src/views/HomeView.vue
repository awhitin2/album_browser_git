<template>
  <div class="home">
    <div class="list-group" v-for='item in albums' :key='item.index'>
      <album-list-item  :index = 'item.index' 
                        :albumName = 'item.albumName' 
                        :artistName = 'item.artistName'
                        :imgSrcSmall = 'item.imgSrcSmall' 
                        :favorited = 'item.favorited'>
      </album-list-item>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

import AlbumListItem from "@/components/AlbumListItem.vue";

export default {
  name: "HomeView",
  components: {
    AlbumListItem,
  },
  data() {
    return {
      albums: []
    };
  },
  methods : {
        getAlbums() {
            const path = 'http://localhost:5000/albums';
            axios.get(path)
            .then((res) => {
                console.log(res.data)
                console.log(typeof res.data)
                this.albums = res.data.albums;
                console.log(this.albums)
            })
            .catch((err)=> {
                console.error(err)
            })
        }
    },
    created(){
        this.getAlbums();
    }

};
</script>
