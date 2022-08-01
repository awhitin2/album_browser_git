
// Songs un-liked from the like Modal do not disappear without adding another song from elsewhere


<template>
  <b-modal  id='liked-modal'
            size = lg
            hide-header
            hide-footer
            title='Album Name'>

    <div class='container-fluid'>
      <div class = 'row align-items-center"'>
        <div class = 'col-3'></div>
        <div class = 'col'>
          <h4 class='text-center'>Liked Albums</h4>
        </div>
        <div class = 'col-3 float-right'>
          <button v-if='!noLikedAlbums' @click='unlikeAlbums' class='btn btn-warning' type="button text-right">Unlike All Albums</button>
        </div>
      </div>
      </div>
      
      <hr class='bg-light'>
      <h5 v-if='noLikedAlbums' 
          class='text-warning'>You have not liked any albums</h5>
      <br>
      <div class = 'row align-items-center'>
        <div class = 'col'>
          <div class="list-group" v-for='(artist, album, index) of likedAlbums'>
            <liked-album-list-item :index = 'index+1' 
                                  :albumName = 'album'
                                  :artistName = 'artist'>
            </liked-album-list-item>
          </div>
        </div>
      </div>
      <br>
      <br v-if='!noLikedAlbums'>
      <div class = 'row align-items-center'>
        <div class = 'col-3'></div>
        <div class = 'col'>
          <h4 class='text-center'>Liked Songs</h4>
        </div>
        <div class = 'col-3 float-right'>
          <button v-if='!noLikedSongs' @click='unlikeSongs' class='btn btn-warning' type="button text-right">Unlike All Songs</button>
        </div>
      </div>
      <hr class='bg-light'>
      <h5 v-if='noLikedSongs' 
          class='text-warning'>You have not liked any songs
      </h5>
      <br>
      <div class = 'row align-items-center'>
        <div class = 'col'>
          <div class="list-group" v-for='(artist, song, index) of likedSongs'>
            <liked-song-list-item :index = 'index+1' 
                                  :songName = 'song'
                                  :artistName = 'artist'>
            </liked-song-list-item>
          </div>
        </div>
      </div>
      <br>
    </div>
  </b-modal>
</template>


<script>
  import Vue from "vue";
  import LikedSongListItem from "@/components/LikedSongListItem.vue";
  import LikedAlbumListItem from "@/components/LikedAlbumListItem.vue";
  import { store } from '@/store.js'
  
  export default {
    name: "LikedModal",
    components: {
      LikedSongListItem,
      LikedAlbumListItem
    },
    data() {
      return {
        likedSongs: store.likedSongs,
        likedAlbums: store.likedAlbums,
        likedIcon: "bi bi-heart-fill text-danger",
        notLikedIcon: "bi bi-heart"
      };  
    },
    computed: {
        noLikedAlbums: function() {
            return Object.keys(store.likedAlbums).length === 0
		    },
        noLikedSongs: function() {
            return Object.keys(store.likedSongs).length === 0
		    }
    },
    methods: {
        unlikeSongs: function() {
            for (var song in store.likedSongs) Vue.delete(store.likedSongs, song);
        },
        unlikeAlbums: function() {
            for (var album in store.likedAlbums) Vue.delete(store.likedAlbums, album);
        }
    },
  }

</script>
