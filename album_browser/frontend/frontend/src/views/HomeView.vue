<template>
  <div class="home">
    <div class="list-group" v-for='item in albums' :key='item.index'>
      <album-list-item  :index = 'item.index' 
                        :albumName = 'item.albumName' 
                        :albumLink = 'item.albumLink' 
                        :albumId = 'item.albumId'
                        :artistName = 'item.artistName'
                        :artistLink = 'item.artistLink'
                        :imgSrcSmall = 'item.imgSrcSmall' 
                        :imgSrcLarge = 'item.imgSrcLarge' 
                        :price = 'item.price'
                        :category = 'item.category'
                        :releaseDate = 'item.releaseDate'
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
            this.albums = res.data.albums;
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
