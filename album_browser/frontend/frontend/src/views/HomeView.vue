<template>
  <div>
      <!-- Bootstrap CSS -->
    <link rel="stylesheet" 
          href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/darkly/bootstrap.min.css" 
          integrity="sha384-nNK9n28pDUDDgIiIqZ/MiyO3F4/9vsMtReZK39klb/MtkZI3/LtjSjlmyVPS3KdN" 
          crossorigin="anonymous">
    <!-- Bootstrap Icons -->
    <link rel="stylesheet" 
          href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" />      
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
      <div class="container-fluid">
        <a class="navbar-brand" 
            href="#"><span 
            class="mb-0 h2">Top 100 Albums</span></a>
        <form class="form-inline ml-auto">
          <input class="form-control mr-sm-2" v-model='input' type="search" placeholder="Search" aria-label="Search">
        </form>
        <b-button type="button" 
                class="btn btn-success" 
                v-b-modal="'liked-modal'">Liked
        </b-button>
      </div>
    </nav>
    <div v-if='!filteredAlbums.length && input !==""' class="card">
      <div class="card-body">
        <h4 class='text-center'>No matching results for "{{input}}"</h4>
      </div>
    </div>
    <div class="list-container">
      <div class="list-group" v-for='item in filteredAlbums' :key='item.index'>
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
  <liked-modal></liked-modal> 
  </div>
</template>

<script>

import axios from 'axios'
import uniqueId from 'lodash.uniqueid';
import AlbumListItem from "@/components/AlbumListItem.vue";
import LikedModal from "@/components/LikedModal.vue";

export default {
  name: "HomeView",
  components: {
    AlbumListItem,
    LikedModal,
  },
  data() {
    return {
      albums: [],
      modalId: uniqueId('modal-'),
      input: '',
    };
  },
  computed: {
    // Returns a sorted list of album info objects that match the search input
    // Objects are ranked and sorted high to low according 
    // the number of search terms they contain
    filteredAlbums: function() {
      const sorted = [];
      const inputs = this.input.toLowerCase().split(' ')

      for (const album of this.albums) {
        album.searchRank = 0
        for (const input of inputs) {
          if (input != '') {
            if (album.albumName.toLowerCase().includes(input) ||
              album.artistName.toLowerCase().includes(input)) {
              album.searchRank ++
            }
          }
        }
        if (album.searchRank > 0 || this.input === '') {
          sorted.push(album)
          }
      }      
      return sorted.sort((a,b) => (b.searchRank-a.searchRank))
    },
  },
  methods : {
    // Fetches albums from server
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
